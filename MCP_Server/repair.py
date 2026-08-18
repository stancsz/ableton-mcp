"""Bounded, read-only repair diagnostics for Ableton MCP failures."""

from __future__ import annotations

import argparse
import ast
import json
import os
import socket
import sys
from pathlib import Path
from typing import Any

from .failure_log import (
    MAX_REPAIR_ATTEMPTS,
    append_repair_attempt,
    block_failure,
    get_failure,
    list_failures,
    resolve_failure,
)


ALLOWED_ACTIONS = ("syntax_check", "socket_probe")
SOURCE_DIRS = (
    Path("MCP_Server"),
    Path("AbletonMCP_Remote_Script"),
    Path("skills") / "ableton-mcp-recovery" / "scripts",
    Path("tests"),
)


def _relative_name(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return path.name


def run_syntax_check(root: str | os.PathLike[str] | None = None) -> dict[str, Any]:
    """Parse project Python files without executing or rewriting them."""

    root_path = Path(root or Path.cwd()).resolve()
    checked_files = 0
    errors: list[dict[str, str]] = []

    for relative_dir in SOURCE_DIRS:
        source_dir = root_path / relative_dir
        if not source_dir.is_dir():
            continue
        for path in sorted(source_dir.rglob("*.py")):
            checked_files += 1
            try:
                source = path.read_text(encoding="utf-8")
                ast.parse(source, filename=str(path))
            except (OSError, SyntaxError, UnicodeError) as error:
                errors.append(
                    {
                        "file": _relative_name(path, root_path),
                        "error": f"{type(error).__name__}: {str(error)}"[:500],
                    }
                )

    return {
        "action": "syntax_check",
        "success": not errors,
        "root": _relative_name(root_path, root_path),
        "checked_files": checked_files,
        "errors": errors,
    }


def run_socket_probe(host: str, port: int, timeout: float = 2.0) -> dict[str, Any]:
    """Check whether the TCP endpoint accepts a connection without sending data."""

    try:
        with socket.create_connection((host, port), timeout=timeout):
            return {
                "action": "socket_probe",
                "success": True,
                "host": host,
                "port": port,
                "timeout_seconds": timeout,
                "details": "TCP connection accepted; no MCP or Ableton command was sent.",
            }
    except OSError as error:
        return {
            "action": "socket_probe",
            "success": False,
            "host": host,
            "port": port,
            "timeout_seconds": timeout,
            "details": f"{type(error).__name__}: {error}"[:500],
        }


def _record_context(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("context")
    return value if isinstance(value, dict) else {}


def _infer_endpoint(record: dict[str, Any], host: str | None, port: int | None) -> tuple[str, int]:
    context = _record_context(record)
    selected_host = host or context.get("host") or os.environ.get("ABLETON_HOST", "localhost")
    selected_port = port or context.get("port") or os.environ.get("ABLETON_PORT", "9877")
    try:
        selected_port = int(selected_port)
    except (TypeError, ValueError) as error:
        raise ValueError("Ableton port must be an integer") from error
    if not isinstance(selected_host, str) or not selected_host.strip():
        raise ValueError("Ableton host must be a non-empty string")
    if not 1 <= selected_port <= 65535:
        raise ValueError("Ableton port must be between 1 and 65535")
    return selected_host, selected_port


def run_repair(
    failure_id: str,
    action: str,
    *,
    root: str | os.PathLike[str] | None = None,
    failure_dir: str | os.PathLike[str] | None = None,
    host: str | None = None,
    port: int | None = None,
    timeout: float = 2.0,
) -> dict[str, Any]:
    """Run one allowlisted diagnostic and append its evidence to the record."""

    if action not in ALLOWED_ACTIONS:
        raise ValueError(f"Unsupported repair action: {action}")
    if timeout <= 0 or timeout > 30:
        raise ValueError("Repair timeout must be greater than 0 and no more than 30 seconds")

    record = get_failure(failure_id, failure_dir=failure_dir)
    if int(record.get("attempts", 0)) >= MAX_REPAIR_ATTEMPTS:
        raise RuntimeError(f"Repair attempt limit ({MAX_REPAIR_ATTEMPTS}) reached")

    if action == "syntax_check":
        result = run_syntax_check(root)
    else:
        selected_host, selected_port = _infer_endpoint(record, host, port)
        result = run_socket_probe(selected_host, selected_port, timeout)

    details = json.dumps(result, ensure_ascii=False, sort_keys=True)
    updated = append_repair_attempt(
        failure_id,
        action,
        success=bool(result.get("success")),
        details=details,
        failure_dir=failure_dir,
    )
    result["failure_id"] = failure_id
    result["attempts"] = updated.get("attempts", 0)
    return result


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run safe diagnostics for Ableton MCP failures")
    parser.add_argument(
        "--failure-dir",
        type=Path,
        default=None,
        help="Failure directory (default: ABLETON_MCP_FAILURE_DIR or .ableton-mcp/failures)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    listing = subparsers.add_parser("list", help="list queued failure records")
    listing.add_argument("--status")
    listing.add_argument("--json", action="store_true", dest="as_json")

    show = subparsers.add_parser("show", help="show one failure record")
    show.add_argument("--id", required=True, dest="failure_id")

    plan = subparsers.add_parser("plan", help="show the recorded bounded repair plan")
    plan.add_argument("--id", required=True, dest="failure_id")

    run = subparsers.add_parser("run", help="run one read-only repair diagnostic")
    run.add_argument("--id", required=True, dest="failure_id")
    run.add_argument("--action", choices=ALLOWED_ACTIONS, required=True)
    run.add_argument("--root", type=Path, default=Path.cwd())
    run.add_argument("--host")
    run.add_argument("--port", type=int)
    run.add_argument("--timeout", type=float, default=2.0)

    resolved = subparsers.add_parser("resolve", help="close a failure with explicit evidence")
    resolved.add_argument("--id", required=True, dest="failure_id")
    resolved.add_argument("--evidence", required=True)

    blocked = subparsers.add_parser("block", help="defer a failure that needs external action")
    blocked.add_argument("--id", required=True, dest="failure_id")
    blocked.add_argument("--reason", required=True)

    return parser


def _print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    try:
        if args.command == "list":
            records = list_failures(status=args.status, failure_dir=args.failure_dir)
            if args.as_json:
                _print_json(records)
            else:
                for record in records:
                    print(
                        f"{record.get('id')} [{record.get('status')}] "
                        f"{record.get('source')}/{record.get('operation')}: {record.get('message')}"
                    )
            return 0

        if args.command == "show":
            _print_json(get_failure(args.failure_id, failure_dir=args.failure_dir))
            return 0

        if args.command == "plan":
            record = get_failure(args.failure_id, failure_dir=args.failure_dir)
            _print_json(
                {
                    "failure_id": record.get("id"),
                    "status": record.get("status"),
                    "attempts": record.get("attempts", 0),
                    "max_attempts": MAX_REPAIR_ATTEMPTS,
                    "repair": record.get("repair", {}),
                }
            )
            return 0

        if args.command == "run":
            result = run_repair(
                args.failure_id,
                args.action,
                root=args.root,
                failure_dir=args.failure_dir,
                host=args.host,
                port=args.port,
                timeout=args.timeout,
            )
            _print_json(result)
            return 0 if result.get("success") else 1

        if args.command == "resolve":
            _print_json(
                resolve_failure(
                    args.failure_id,
                    args.evidence,
                    failure_dir=args.failure_dir,
                )
            )
            return 0

        if args.command == "block":
            _print_json(
                block_failure(
                    args.failure_id,
                    args.reason,
                    failure_dir=args.failure_dir,
                )
            )
            return 0
    except (FileNotFoundError, ValueError, RuntimeError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1

    return 2


if __name__ == "__main__":  # pragma: no cover - exercised through the CLI
    raise SystemExit(main())
