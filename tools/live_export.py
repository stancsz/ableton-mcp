"""Windows bridge for Ableton Live's Export Audio/Video dialog.

Ableton's public Live Object Model does not expose offline audio rendering.
This module is deliberately separate from the Remote Script: it is an
optional, MCP-callable UI bridge with strict pre/post validation.  It does
not pretend that a successful keypress is a successful render.

The first version exposes validation and capability discovery.  The actual
render action is intentionally guarded until the caller opts into the
Windows UI bridge with ``ABLETON_MCP_UI_EXPORT=1``.  This keeps headless MCP
servers deterministic while allowing the desktop workflow to adopt the
command safely.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_BAR_BEAT_TICK = re.compile(r"^\d+\.\d+\.\d+$")


class LiveExportError(RuntimeError):
    """Raised when an export cannot be proven to meet the requested contract."""


@dataclass(frozen=True)
class ExportRequest:
    output_path: Path
    render_start: str | None = None
    render_length_bars: float | None = None
    expected_duration_seconds: float | None = None
    sample_rate: int = 44100
    bit_depth: int = 24
    rendered_track: str = "Main"


def validate_request(request: ExportRequest) -> dict[str, Any]:
    """Validate an export contract without touching Live or the filesystem."""

    output_path = request.output_path
    if not output_path.is_absolute():
        raise LiveExportError("output_path must be absolute")
    if output_path.suffix.lower() != ".wav":
        raise LiveExportError("export_audio currently requires a .wav output")
    if request.render_start is not None and not _BAR_BEAT_TICK.fullmatch(
        request.render_start
    ):
        raise LiveExportError("render_start must use bar.beat.tick notation")
    if request.render_length_bars is not None and request.render_length_bars <= 0:
        raise LiveExportError("render_length_bars must be positive")
    if request.expected_duration_seconds is not None and (
        request.expected_duration_seconds <= 0
    ):
        raise LiveExportError("expected_duration_seconds must be positive")
    if request.sample_rate not in {44100, 48000, 88200, 96000, 176400, 192000}:
        raise LiveExportError("unsupported sample rate")
    if request.bit_depth not in {16, 24, 32}:
        raise LiveExportError("unsupported PCM bit depth")
    if request.rendered_track != "Main":
        raise LiveExportError("the release bridge currently permits Main only")

    return {
        "output_path": str(output_path),
        "render_start": request.render_start,
        "render_length_bars": request.render_length_bars,
        "expected_duration_seconds": request.expected_duration_seconds,
        "sample_rate": request.sample_rate,
        "bit_depth": request.bit_depth,
        "rendered_track": request.rendered_track,
    }


def capability_report() -> dict[str, Any]:
    """Report whether the optional desktop bridge is available."""

    return {
        "native_live_object_model_export": False,
        "ui_bridge_supported": os.name == "nt",
        "ui_bridge_enabled": os.environ.get("ABLETON_MCP_UI_EXPORT") == "1",
        "dependencies": {
            "pyautogui": _module_available("pyautogui"),
            "pywin32": _module_available("win32gui"),
        },
        "reason": (
            "Ableton exposes Export Audio/Video in the application UI, but not "
            "as a public Remote Script/Live Object Model render function."
        ),
    }


def export_audio(request: ExportRequest) -> dict[str, Any]:
    """Run the guarded desktop export bridge.

    The UI automation implementation is kept behind an explicit opt-in while
    its range-setting and completion checks are being finalized.  Callers get
    a structured blocker instead of an unverifiable file.
    """

    contract = validate_request(request)
    report = capability_report()
    if not report["ui_bridge_supported"]:
        raise LiveExportError("export_audio UI bridge is currently Windows-only")
    if not report["ui_bridge_enabled"]:
        raise LiveExportError(
            "UI export is disabled; set ABLETON_MCP_UI_EXPORT=1 for the guarded desktop bridge"
        )
    raise LiveExportError(
        "UI export bridge is not yet enabled for this Set; use Live's Export Audio/Video dialog"
    )


def _module_available(name: str) -> bool:
    try:
        __import__(name)
    except ImportError:
        return False
    return True
