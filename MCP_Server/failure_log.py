"""Durable, privacy-conscious failure records for Ableton MCP.

The MCP server must never fail because it could not write a diagnostic record.
Records are intentionally small JSON documents written atomically to a local
directory.  The repair CLI can update the same document with bounded,
read-only verification attempts later.
"""

from __future__ import annotations

import argparse
import datetime as _datetime
import json
import logging
import os
import re
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Any, Mapping


logger = logging.getLogger("ableton-mcp-failures")

FAILURE_DIR_ENV = "ABLETON_MCP_FAILURE_DIR"
DEFAULT_FAILURE_DIR = Path(".ableton-mcp") / "failures"
MAX_REPAIR_ATTEMPTS = 3
MAX_MESSAGE_LENGTH = 2_000
MAX_CONTEXT_ITEMS = 32

_FAILURE_ID_RE = re.compile(r"^[0-9a-f]{32}$")
_TOKEN_RE = re.compile(
    r"(?i)(bearer\s+|(?:api[_ -]?key|token|password|secret|authorization)\s*[:=]\s*)[^\s,;]+"
)
_CREDENTIAL_URL_RE = re.compile(r"(?i)(https?://)([^/@\s:]+):([^/@\s]+)@")
_WINDOWS_PATH_RE = re.compile(r"(?<![A-Za-z0-9_])([A-Za-z]:\\[^\r\n\t,;]+)")
_UNIX_PATH_RE = re.compile(r"(?<![A-Za-z0-9_])/(?:Users|home|private|var|tmp|opt|mnt)/[^\r\n\t,;]+")

# Context is deliberately allowlisted.  In particular, prompts, track/clip
# names, notes, URIs, audio paths, and arbitrary exception payloads do not
# belong in a durable failure queue.
SAFE_CONTEXT_KEYS = frozenset(
    {
        "action",
        "attempt",
        "category",
        "clip_index",
        "command_type",
        "duration_ms",
        "error_type",
        "host",
        "max_attempts",
        "port",
        "python_version",
        "status",
        "timeout_seconds",
        "tool_name",
        "track_index",
    }
)


def _utc_now() -> str:
    return (
        _datetime.datetime.now(_datetime.timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def _sanitize_text(value: Any, max_length: int = MAX_MESSAGE_LENGTH) -> str:
    """Return bounded text with common credentials and local paths removed."""

    text = str(value).replace("\x00", " ").replace("\r", " ").replace("\n", " ")
    text = _CREDENTIAL_URL_RE.sub(r"\1<redacted>@", text)
    text = _TOKEN_RE.sub(lambda match: f"{match.group(1)}<redacted>", text)
    text = _WINDOWS_PATH_RE.sub("<path>", text)
    text = _UNIX_PATH_RE.sub("<path>", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_length:
        return text[: max_length - 3] + "..."
    return text


def _safe_identifier(value: Any, fallback: str) -> str:
    text = _sanitize_text(value, max_length=80)
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("_.-")
    return text or fallback


def _sanitize_context(context: Mapping[str, Any] | None) -> dict[str, Any]:
    if not context:
        return {}

    result: dict[str, Any] = {}
    for key, value in list(context.items())[:MAX_CONTEXT_ITEMS]:
        if key not in SAFE_CONTEXT_KEYS:
            continue
        if value is None or isinstance(value, (bool, int, float)):
            result[key] = value
        elif isinstance(value, str):
            result[key] = _sanitize_text(value, max_length=200)
        else:
            result[key] = _sanitize_text(value, max_length=200)
    return result


def _repair_hint(operation: str, error_type: str, message: str) -> dict[str, Any]:
    haystack = f"{operation} {error_type} {message}".lower()

    if any(term in haystack for term in ("connect", "socket", "timeout", "broken pipe")):
        return {
            "strategy": "connection",
            "safe_actions": ["socket_probe", "syntax_check"],
            "next_step": "Check the Remote Script and MCP endpoint, then run a read-only socket probe.",
            "requires_user_action": True,
        }
    if any(term in haystack for term in ("json", "response", "protocol")):
        return {
            "strategy": "protocol",
            "safe_actions": ["syntax_check"],
            "next_step": "Inspect the recorded operation and response path before retrying any state change.",
            "requires_user_action": True,
        }
    if any(term in haystack for term in ("track", "clip", "live api", "browser")):
        return {
            "strategy": "session_state",
            "safe_actions": ["syntax_check"],
            "next_step": "Inspect the current Live session state; do not replay a mutating command automatically.",
            "requires_user_action": True,
        }
    return {
        "strategy": "investigation",
        "safe_actions": ["syntax_check"],
        "next_step": "Inspect the failure record and source path before choosing a repair.",
        "requires_user_action": True,
    }


def failure_directory(root: str | os.PathLike[str] | None = None) -> Path:
    """Resolve the local failure directory.

    ``ABLETON_MCP_FAILURE_DIR`` wins when configured.  Otherwise the folder is
    relative to the current working directory so a repo checkout naturally
    gets ``.ableton-mcp/failures`` without making assumptions about packaging.
    """

    configured = os.environ.get(FAILURE_DIR_ENV)
    if configured:
        return Path(configured).expanduser()
    return Path(root) / DEFAULT_FAILURE_DIR if root is not None else Path.cwd() / DEFAULT_FAILURE_DIR


def _atomic_write_json(path: Path, payload: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=".failure-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
        temporary_path = None
        return path
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                logger.debug("Could not remove temporary failure record %s", temporary_path)


def _record_path(failure_id: str, directory: Path) -> Path:
    if not _FAILURE_ID_RE.fullmatch(failure_id):
        raise ValueError("Invalid failure id")
    return directory / f"{failure_id}.json"


def record_failure(
    source: str,
    operation: str,
    error: BaseException | str,
    context: Mapping[str, Any] | None = None,
    *,
    failure_dir: str | os.PathLike[str] | None = None,
) -> Path | None:
    """Persist one failure and return its path.

    This function is best-effort by design.  A permissions or disk-space
    problem is reported to the normal logger but is never allowed to mask the
    original Ableton/MCP failure.
    """

    try:
        error_type = type(error).__name__ if isinstance(error, BaseException) else "Error"
        message = _sanitize_text(error)
        failure_id = uuid.uuid4().hex
        record: dict[str, Any] = {
            "schema_version": 1,
            "id": failure_id,
            "created_at": _utc_now(),
            "source": _safe_identifier(source, "unknown"),
            "operation": _safe_identifier(operation, "unknown"),
            "error_type": _safe_identifier(error_type, "Error"),
            "message": message or "Unknown failure",
            "context": _sanitize_context(context),
            "status": "open",
            "attempts": 0,
        }
        record["repair"] = _repair_hint(
            record["operation"], record["error_type"], record["message"]
        )
        directory = failure_directory(failure_dir)
        return _atomic_write_json(_record_path(failure_id, directory), record)
    except Exception as log_error:  # pragma: no cover - exercised by OS failures
        logger.warning("Could not persist failure record: %s", _sanitize_text(log_error, 500))
        return None


def _read_record(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict) or not isinstance(value.get("id"), str):
            return None
        return value
    except (OSError, json.JSONDecodeError, TypeError):
        logger.warning("Ignoring unreadable failure record %s", path)
        return None


def list_failures(
    *,
    status: str | None = None,
    failure_dir: str | os.PathLike[str] | None = None,
) -> list[dict[str, Any]]:
    directory = failure_directory(failure_dir)
    if not directory.is_dir():
        return []

    records = []
    for path in directory.glob("*.json"):
        record = _read_record(path)
        if record is not None and (status is None or record.get("status") == status):
            records.append(record)
    return sorted(records, key=lambda item: str(item.get("created_at", "")), reverse=True)


def get_failure(
    failure_id: str,
    *,
    failure_dir: str | os.PathLike[str] | None = None,
) -> dict[str, Any]:
    directory = failure_directory(failure_dir)
    path = _record_path(failure_id, directory)
    record = _read_record(path)
    if record is None:
        raise FileNotFoundError(f"Failure record not found: {failure_id}")
    return record


def _write_record(record: Mapping[str, Any], failure_dir: str | os.PathLike[str] | None) -> Path:
    failure_id = record.get("id")
    if not isinstance(failure_id, str):
        raise ValueError("Failure record has no valid id")
    directory = failure_directory(failure_dir)
    return _atomic_write_json(_record_path(failure_id, directory), record)


def append_repair_attempt(
    failure_id: str,
    action: str,
    *,
    success: bool,
    details: str,
    failure_dir: str | os.PathLike[str] | None = None,
) -> dict[str, Any]:
    """Append one bounded repair attempt and return the updated record."""

    record = get_failure(failure_id, failure_dir=failure_dir)
    attempts = int(record.get("attempts", 0))
    if attempts >= MAX_REPAIR_ATTEMPTS:
        raise RuntimeError(f"Repair attempt limit ({MAX_REPAIR_ATTEMPTS}) reached")

    history = record.setdefault("repair_history", [])
    if not isinstance(history, list):
        history = []
        record["repair_history"] = history
    history.append(
        {
            "at": _utc_now(),
            "action": _safe_identifier(action, "unknown"),
            "success": bool(success),
            "details": _sanitize_text(details, max_length=1_000),
        }
    )
    record["attempts"] = attempts + 1
    repair = record.setdefault("repair", {})
    if isinstance(repair, dict):
        repair["last_action"] = _safe_identifier(action, "unknown")
        repair["last_success"] = bool(success)
    _write_record(record, failure_dir)
    return record


def resolve_failure(
    failure_id: str,
    evidence: str,
    *,
    failure_dir: str | os.PathLike[str] | None = None,
) -> dict[str, Any]:
    """Mark a record resolved only with explicit evidence."""

    evidence = _sanitize_text(evidence, max_length=1_000)
    if not evidence:
        raise ValueError("Resolution evidence is required")
    record = get_failure(failure_id, failure_dir=failure_dir)
    record["status"] = "resolved"
    record["resolution"] = {"at": _utc_now(), "evidence": evidence}
    _write_record(record, failure_dir)
    return record


def block_failure(
    failure_id: str,
    reason: str,
    *,
    failure_dir: str | os.PathLike[str] | None = None,
) -> dict[str, Any]:
    reason = _sanitize_text(reason, max_length=1_000)
    if not reason:
        raise ValueError("A block reason is required")
    record = get_failure(failure_id, failure_dir=failure_dir)
    record["status"] = "blocked"
    record["blocked"] = {"at": _utc_now(), "reason": reason}
    _write_record(record, failure_dir)
    return record


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record and inspect Ableton MCP failures")
    parser.add_argument(
        "--failure-dir",
        type=Path,
        default=None,
        help=f"Failure directory (default: ${{{FAILURE_DIR_ENV}}} or .ableton-mcp/failures)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    record = subparsers.add_parser("record", help="write a sanitized failure record")
    record.add_argument("--source", required=True)
    record.add_argument("--operation", required=True)
    record.add_argument("--error", required=True)
    record.add_argument("--context-json", default="{}")
    record.add_argument(
        "--context",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="safe structural context; repeat for multiple values (PowerShell-friendly)",
    )

    listing = subparsers.add_parser("list", help="list failure records")
    listing.add_argument("--status")
    listing.add_argument("--json", action="store_true", dest="as_json")

    show = subparsers.add_parser("show", help="show one failure record")
    show.add_argument("--id", required=True, dest="failure_id")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.command == "record":
        try:
            context = json.loads(args.context_json)
            if not isinstance(context, dict):
                raise ValueError("context-json must be a JSON object")
            for item in args.context:
                key, separator, value = item.partition("=")
                if not separator or not key:
                    raise ValueError("context entries must use KEY=VALUE")
                context[key] = value
        except (json.JSONDecodeError, ValueError) as error:
            print(f"Invalid context JSON: {error}", file=sys.stderr)
            return 2
        path = record_failure(
            args.source,
            args.operation,
            args.error,
            context,
            failure_dir=args.failure_dir,
        )
        if path is None:
            return 1
        record = _read_record(path)
        print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    if args.command == "list":
        records = list_failures(status=args.status, failure_dir=args.failure_dir)
        if args.as_json:
            print(json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True))
        else:
            for record in records:
                print(
                    f"{record.get('id')} [{record.get('status')}] "
                    f"{record.get('source')}/{record.get('operation')}: {record.get('message')}"
                )
        return 0

    if args.command == "show":
        try:
            print(
                json.dumps(
                    get_failure(args.failure_id, failure_dir=args.failure_dir),
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
            )
            return 0
        except (FileNotFoundError, ValueError) as error:
            print(str(error), file=sys.stderr)
            return 1

    return 2


if __name__ == "__main__":  # pragma: no cover - exercised through the CLI
    raise SystemExit(main())
