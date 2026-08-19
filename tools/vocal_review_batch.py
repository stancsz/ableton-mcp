"""Batch, read-only MCP preflight for the two vocal tracks.

This uses the existing AbletonMCP socket contract instead of opening Live's
UI. It gathers the facts needed before a vocal edit, so Gemini and UI
round-trips are spent only on an audible decision.
"""

from __future__ import annotations

import argparse
import json
import socket
from pathlib import Path
from typing import Any


def call(host: str, port: int, command: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """Send one Remote Script command and decode its JSON response."""

    with socket.create_connection((host, port), timeout=5.0) as sock:
        sock.settimeout(15.0)
        sock.sendall(json.dumps({"type": command, "params": params or {}}).encode())
        chunks: list[bytes] = []
        while True:
            chunk = sock.recv(8192)
            if not chunk:
                break
            chunks.append(chunk)
            try:
                return json.loads(b"".join(chunks).decode("utf-8"))
            except json.JSONDecodeError:
                continue
    raise RuntimeError(f"incomplete response for {command}")


def result_or_error(response: dict[str, Any]) -> dict[str, Any]:
    if response.get("status") != "success":
        raise RuntimeError(response.get("message", "Ableton command failed"))
    return response.get("result", {})


def collect(host: str, port: int, tracks: list[int]) -> dict[str, Any]:
    session = result_or_error(call(host, port, "get_session_info"))
    script = result_or_error(call(host, port, "get_script_info"))
    vocal_rows: list[dict[str, Any]] = []
    for track_index in tracks:
        volume = result_or_error(
            call(host, port, "get_track_volume_info", {"track_index": track_index})
        )
        info = result_or_error(call(host, port, "get_track_info", {"track_index": track_index}))
        clips = result_or_error(
            call(host, port, "get_arrangement_clips", {"track_index": track_index})
        ).get("clips", [])
        vocal_rows.append(
            {
                "track_index": track_index,
                "track_name": volume.get("track_name") or info.get("name"),
                "volume": volume,
                "device_names": [
                    device.get("name")
                    for device in info.get("devices", [])
                    if isinstance(device, dict) and device.get("name")
                ],
                "arrangement_clips": clips,
            }
        )
    return {
        "schema": "ableton_vocal_review_batch_v1",
        "session": {
            "tempo": session.get("tempo"),
            "song_length": session.get("song_length"),
            "track_count": session.get("track_count"),
            "return_track_count": session.get("return_track_count"),
        },
        "script": {
            "version": script.get("script_version"),
            "capabilities": script.get("capabilities", []),
        },
        "vocal_tracks": vocal_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9877)
    parser.add_argument("--tracks", nargs="+", type=int, default=[7, 8])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = collect(args.host, args.port, args.tracks)
    encoded = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
