"""Send one authorized audio file to Gemini 3.7 through the audio-capable API.

This deliberately bypasses the Antigravity managed-agent wrapper. Antigravity
currently accepts text and images only, while the standard Vertex/Gemini
generateContent endpoint accepts audio. Authentication uses the active local
gcloud account; the access token is never printed or written to disk.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_MODEL = "gemini-3.7-flash"
DEFAULT_LOCATION = "global"
DEFAULT_PROJECT = "stancsz-381415"
TIMESTAMP_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
DEFAULT_PROFILE = "compact"
# These are safety caps, not target lengths. Iterative checks should spend
# prediction tokens on one decision; the release pass is the only profile
# allowed enough room for a complete blocker/checks report.
DEFAULT_MAX_OUTPUT_TOKENS = {"taste": 420, "compact": 420, "release": 600}
# Gemini 3.x no longer treats the legacy numeric thinking budget as the
# reliable cost/latency control. LOW is the shortest complete route observed
# for this audio listener; callers can explicitly request MEDIUM/HIGH when a
# final review needs more reasoning.
DEFAULT_THINKING_LEVEL = {"taste": "LOW", "compact": "LOW", "release": "LOW"}
MAX_FOCUS_CHARS = 240


def _gcloud_command() -> str:
    """Find the gcloud executable without exposing credentials or config."""

    for name in ("gcloud.cmd", "gcloud"):
        found = shutil.which(name)
        if found:
            return found
    windows_path = Path(
        r"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
    )
    if windows_path.exists():
        return str(windows_path)
    raise RuntimeError("gcloud was not found; sign in with gcloud before using this route")


def _gcloud_value(*args: str) -> str:
    result = subprocess.run(
        [_gcloud_command(), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def resolve_project(explicit: str | None) -> str:
    project = explicit or os.environ.get("GOOGLE_CLOUD_PROJECT")
    if project:
        return project
    try:
        configured = _gcloud_value("config", "get-value", "project")
    except (OSError, subprocess.CalledProcessError, RuntimeError):
        configured = ""
    return configured if configured and configured != "(unset)" else DEFAULT_PROJECT


def audio_mime_type(path: Path) -> str:
    known = {
        ".wav": "audio/wav",
        ".mp3": "audio/mpeg",
        ".m4a": "audio/mp4",
        ".aac": "audio/aac",
        ".flac": "audio/flac",
        ".ogg": "audio/ogg",
    }
    return known.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def build_prompt(kind: str, focus: str | None, profile: str = DEFAULT_PROFILE) -> str:
    subjects = {
        "full-track": "full mix",
        "stem": "audio stem",
        "excerpt": "diagnostic mix excerpt",
    }
    subject = subjects.get(kind, "audio")
    focus_text = f"\nAdditional requested focus: {focus}\n" if focus else ""
    scope = (
        f"listen to the entire attached {subject}"
        if kind != "excerpt"
        else "listen only to the attached excerpt"
    )
    scope_instruction = (
        "Answer only that requested question; do not list unrelated mix problems."
        if focus
        else "Keep the answer limited to the audible character of this file."
    )
    if profile == "taste":
        excerpt_rule = (
            "Do not generalize beyond this excerpt."
            if kind == "excerpt"
            else "Do not replace listening with spectral or loudness speculation."
        )
        return f"""Act like a thoughtful human producer and {scope} before answering.
{scope_instruction} {excerpt_rule}{focus_text}

Return only this compact format:
HEARD_AUDIO
ANSWER: yes/no or A/B choice, then one plain-language sentence
WHY: MM:SS — audible reason; MM:SS — audible reason
ACTION: one mix action, or NONE if the change is already better

Complete all four lines before stopping; do not return a partial answer.

Judge musical comfort, emotional focus, texture, punch, and whether the result
feels intentional. Do not write a technical tutorial or repeat the prompt. If
you cannot hear the audio, reply exactly AUDIO UNAVAILABLE and do not invent
comments. Only compare versions when both are attached; otherwise judge this
file alone."""
    if profile == "release":
        return f"""Act as a rigorous mix engineer and {scope} before answering.
This is an audio review, not a metadata or filename task. Do not infer audible facts
from the filename, genre, prompt, or local measurements.{focus_text}

Return a complete, compact release-review report:
1. One-sentence audible verdict.
2. At most three audible blockers ordered by impact. For each: P0/P1/P2, exact
   MM:SS, audible evidence, likely cause, and one testable Ableton action.
3. One short line covering kick/bass/sub, vocals/masking, dynamics, stereo/mono,
   harshness, depth, and translation; say unknown when unsupported.
4. One short line for what is already working and should not be changed casually.
Do not add an introduction, conclusion, generic tutorial, or repeated explanation.

If you truly heard the audio, begin with HEARD_AUDIO. If you cannot hear it, reply
exactly AUDIO UNAVAILABLE and do not invent comments."""

    excerpt_rule = (
        "Do not generalize beyond this excerpt; assess only the requested issue."
        if kind == "excerpt"
        else "Keep the review specific to audible evidence in this file."
    )
    return f"""Act as a rigorous mix engineer and {scope} before answering.
This is an audio review, not a metadata task. {scope_instruction} {excerpt_rule}
Do not infer facts
from filename, genre, prompt, or local measurements.{focus_text}

Use this compact schema and keep it short:
HEARD_AUDIO
VERDICT: one sentence
ISSUES:
- P# | MM:SS | audible problem | one likely cause | one Ableton test
WORKING: one short sentence
CHECKS: low-end; vocals/masking; dynamics; stereo/mono; harshness. Use ? when
not supported by this audio.

Return at most three issues. If you cannot hear the audio, reply exactly AUDIO UNAVAILABLE
and do not invent comments."""


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def _normalise_focus(focus: str | None) -> str:
    return " ".join((focus or "").split())


def validate_focus(focus: str | None, profile: str) -> str:
    """Return a compact focus or reject a multi-brief listening request."""

    normalized = _normalise_focus(focus)
    if len(normalized) > MAX_FOCUS_CHARS:
        raise ValueError(
            f"focus must be at most {MAX_FOCUS_CHARS} characters; split it into separate checks"
        )
    if profile == "taste" and sum(normalized.count(mark) for mark in "?？") > 1:
        raise ValueError("taste focus must contain one question; run separate targeted checks")
    return normalized


def _cached_report_matches(
    report: str,
    *,
    audio_hash: str,
    model: str,
    profile: str,
    kind: str,
    focus: str | None,
    max_output_tokens: int | None = None,
    thinking_level: str | None = None,
    thinking_budget: int | None = None,
) -> bool:
    expected = {
        "AUDIO_SHA256": audio_hash,
        "MODEL_REQUESTED": model,
        "PROFILE": profile,
        "KIND": kind,
        "FOCUS": _normalise_focus(focus),
    }
    if max_output_tokens is not None:
        expected["MAX_OUTPUT_TOKENS"] = str(max_output_tokens)
    if thinking_level is not None:
        expected["THINKING_LEVEL"] = thinking_level
    if thinking_budget is not None:
        expected["THINKING_BUDGET"] = str(thinking_budget)
    values: dict[str, str] = {}
    for line in report.splitlines():
        key, separator, value = line.partition(": ")
        if separator and key in expected:
            values[key] = value
    return all(values.get(key) == value for key, value in expected.items())


def _response_text(payload: dict[str, Any]) -> str:
    parts: list[str] = []
    for candidate in payload.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                parts.append(part["text"])
    return "\n".join(parts).strip()


def _has_grounded_schema(text: str, profile: str) -> bool:
    """Reject audio responses that started correctly but were truncated."""

    if not text.startswith("HEARD_AUDIO") or not TIMESTAMP_RE.search(text):
        return False
    required = {
        "taste": ("ANSWER:", "WHY:", "ACTION:"),
        "compact": ("VERDICT:", "ISSUES:", "WORKING:", "CHECKS:"),
        "release": ("1.", "2.", "3.", "4."),
    }
    return all(marker in text for marker in required[profile])


def _request(
    path: Path,
    project: str,
    model: str,
    location: str,
    prompt: str,
    max_output_tokens: int,
    thinking_level: str | None,
    thinking_budget: int | None,
) -> dict[str, Any]:
    token = _gcloud_value("auth", "print-access-token")
    endpoint = (
        f"https://aiplatform.googleapis.com/v1/projects/{project}/locations/"
        f"{location}/publishers/google/models/{model}:generateContent"
    )
    generation_config: dict[str, Any] = {
        "maxOutputTokens": max_output_tokens,
        "candidateCount": 1,
    }
    if thinking_level is not None:
        generation_config["thinkingConfig"] = {
            "thinkingLevel": thinking_level,
            "includeThoughts": False,
        }
    elif thinking_budget is not None:
        generation_config["thinkingConfig"] = {
            "thinkingBudget": thinking_budget,
            "includeThoughts": False,
        }
    body = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt},
                    {
                        "inlineData": {
                            "mimeType": audio_mime_type(path),
                            "data": base64.b64encode(path.read_bytes()).decode("ascii"),
                        }
                    },
                ],
            }
        ],
        "generationConfig": generation_config,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "x-goog-user-project": project,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:4000]
        raise RuntimeError(f"Gemini API returned HTTP {error.code}: {detail}") from error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path, help="one authorized local WAV/MP3/audio file")
    parser.add_argument("--kind", choices=("full-track", "stem", "excerpt"), default="full-track")
    parser.add_argument("--focus", help="optional mix-review focus")
    parser.add_argument(
        "--profile",
        choices=("taste", "compact", "release"),
        default=DEFAULT_PROFILE,
        help="taste for one human-listening question; compact for triage; release for the final audit",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        help="override the profile output cap (default: 420 taste, 420 compact, 600 release)",
    )
    parser.add_argument(
        "--thinking-level",
        choices=("MINIMAL", "LOW", "MEDIUM", "HIGH"),
        help="explicit thinking level for endpoints that support it; omitted by default for this 3.7 route",
    )
    parser.add_argument(
        "--thinking-budget",
        type=int,
        help="legacy compatibility thinking cap; overrides the default LOW thinking level",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="force a new request even when the output is an exact matching report",
    )
    parser.add_argument("--project", help="Google Cloud project used for the authenticated request")
    parser.add_argument("--location", default=DEFAULT_LOCATION)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--output", type=Path, help="optional path for the text feedback report")
    args = parser.parse_args(argv)

    path = args.audio.resolve()
    if not path.is_file():
        parser.error(f"audio file does not exist: {path}")
    if audio_mime_type(path) == "application/octet-stream":
        parser.error(f"unsupported audio extension: {path.suffix or '(none)'}")
    if args.kind == "excerpt" and not args.focus:
        parser.error("--kind excerpt requires --focus so the short review stays scoped")
    if args.profile == "taste" and not args.focus:
        parser.error("--profile taste requires --focus so Gemini answers one concrete listening question")
    if args.max_output_tokens is not None and args.max_output_tokens <= 0:
        parser.error("--max-output-tokens must be positive")
    if args.thinking_level and args.thinking_budget is not None:
        parser.error("use either --thinking-level or legacy --thinking-budget, not both")

    project = resolve_project(args.project)
    try:
        focus = validate_focus(args.focus, args.profile)
    except ValueError as error:
        parser.error(str(error))
    audio_hash = file_sha256(path)
    max_output_tokens = args.max_output_tokens or DEFAULT_MAX_OUTPUT_TOKENS[args.profile]
    thinking_budget = args.thinking_budget
    if thinking_budget is not None and thinking_budget < 0:
        parser.error("--thinking-budget must be zero or greater")
    # Gemini 3.x should use thinkingLevel. Keep the numeric flag only as an
    # explicit backwards-compatible override for callers that need it.
    thinking_level = args.thinking_level
    if thinking_level is None and thinking_budget is None:
        thinking_level = DEFAULT_THINKING_LEVEL[args.profile]
    if thinking_level is not None:
        thinking_budget = None
    if args.output and args.output.is_file() and not args.no_cache:
        cached = args.output.read_text(encoding="utf-8", errors="replace")
        if _cached_report_matches(
            cached,
            audio_hash=audio_hash,
            model=args.model,
            profile=args.profile,
            kind=args.kind,
            focus=focus,
            max_output_tokens=max_output_tokens,
            thinking_level=thinking_level,
            thinking_budget=thinking_budget,
        ):
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            print(cached, end="" if cached.endswith("\n") else "\n")
            return 0 if "AUDIO_GROUNDING: PASS" in cached else 2

    try:
        payload = _request(
            path,
            project,
            args.model,
            args.location,
            build_prompt(args.kind, focus, args.profile),
            max_output_tokens,
            thinking_level,
            thinking_budget,
        )
    except RuntimeError as error:
        # Keep endpoint/configuration failures machine-readable. In particular,
        # an unsupported thinking level should not produce a Python traceback or
        # be mistaken for an audio-grounding failure.
        report = "\n".join(
            [
                "AUDIO_GROUNDING: UNVERIFIED",
                f"MODEL_REQUESTED: {args.model}",
                f"PROJECT: {project}",
                f"FILE: {path}",
                f"AUDIO_SHA256: {audio_hash}",
                f"PROFILE: {args.profile}",
                f"KIND: {args.kind}",
                f"FOCUS: {focus}",
                f"MAX_OUTPUT_TOKENS: {max_output_tokens}",
                f"THINKING_LEVEL: {thinking_level or 'UNSET'}",
                f"THINKING_BUDGET: {thinking_budget if thinking_budget is not None else 'UNSET'}",
                f"ERROR: {error}",
                "",
                "AUDIO UNAVAILABLE",
            ]
        )
        if args.output:
            args.output.write_text(report + "\n", encoding="utf-8")
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            print(report)
        return 2
    text = _response_text(payload)
    usage = payload.get("usageMetadata", {})
    heard = _has_grounded_schema(text, args.profile)
    status = "PASS" if heard else "UNVERIFIED"

    report = "\n".join(
        [
            f"AUDIO_GROUNDING: {status}",
            f"MODEL: {payload.get('modelVersion', args.model)}",
            f"MODEL_REQUESTED: {args.model}",
            f"PROJECT: {project}",
            f"FILE: {path}",
            f"AUDIO_SHA256: {audio_hash}",
            f"PROFILE: {args.profile}",
            f"KIND: {args.kind}",
            f"FOCUS: {focus}",
            f"MAX_OUTPUT_TOKENS: {max_output_tokens}",
            f"THINKING_LEVEL: {thinking_level or 'UNSET'}",
            f"THINKING_BUDGET: {thinking_budget if thinking_budget is not None else 'UNSET'}",
            f"USAGE: {json.dumps(usage, ensure_ascii=False)}",
            "",
            text or "AUDIO UNAVAILABLE",
        ]
    )
    if args.output:
        args.output.write_text(report + "\n", encoding="utf-8")
    else:
        # Windows consoles can default to cp1252, while Gemini responses may
        # contain Unicode symbols such as ≈. Keep the report printable without
        # turning a successful audio-grounded request into a false tool error.
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(report)
    return 0 if heard else 2


if __name__ == "__main__":
    sys.exit(main())
