"""Send one authorized audio file to Gemini 3.7 through the audio-capable API.

This deliberately bypasses the Antigravity managed-agent wrapper. Antigravity
currently accepts text and images only, while the standard Vertex/Gemini
generateContent endpoint accepts audio. Authentication uses the active local
gcloud account; the access token is never printed or written to disk.
"""

from __future__ import annotations

import argparse
import base64
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


def build_prompt(kind: str, focus: str | None) -> str:
    subject = "full mix" if kind == "full-track" else "audio stem"
    focus_text = f"\nAdditional requested focus: {focus}\n" if focus else ""
    return f"""Act as a rigorous mix engineer and listen to the entire attached {subject} before answering.
This is an audio review, not a metadata or filename task. Do not infer audible facts
from the filename, genre, prompt, or local measurements.{focus_text}

Return:
1. A one-sentence audible verdict.
2. The top five audible issues ordered by impact. For each: P0/P1/P2, exact MM:SS
   timestamp(s), what is actually audible, likely cause, and one testable Ableton action.
3. Checks for kick/bass/sub, vocal versus instrumental masking, dynamics/pumping,
   stereo/mono or phase, harshness, depth, and translation. Say unknown when the
   audio does not support a conclusion.
4. What is already working and should not be changed casually.

If you truly heard the audio, begin the response with HEARD_AUDIO. If you cannot
access or hear it, reply exactly AUDIO UNAVAILABLE and do not invent comments."""


def _response_text(payload: dict[str, Any]) -> str:
    parts: list[str] = []
    for candidate in payload.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                parts.append(part["text"])
    return "\n".join(parts).strip()


def _request(path: Path, project: str, model: str, location: str, prompt: str) -> dict[str, Any]:
    token = _gcloud_value("auth", "print-access-token")
    endpoint = (
        f"https://aiplatform.googleapis.com/v1/projects/{project}/locations/"
        f"{location}/publishers/google/models/{model}:generateContent"
    )
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
        ]
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
    parser.add_argument("--kind", choices=("full-track", "stem"), default="full-track")
    parser.add_argument("--focus", help="optional mix-review focus")
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

    project = resolve_project(args.project)
    payload = _request(path, project, args.model, args.location, build_prompt(args.kind, args.focus))
    text = _response_text(payload)
    usage = payload.get("usageMetadata", {})
    heard = text.startswith("HEARD_AUDIO") and bool(TIMESTAMP_RE.search(text))
    status = "PASS" if heard else "UNVERIFIED"

    report = "\n".join(
        [
            f"AUDIO_GROUNDING: {status}",
            f"MODEL: {payload.get('modelVersion', args.model)}",
            f"PROJECT: {project}",
            f"FILE: {path}",
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
