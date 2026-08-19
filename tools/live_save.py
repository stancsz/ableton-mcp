"""Guarded MCP bridge for saving the foreground Ableton Live Set.

The public Live Object Model exposes the Set contents but does not expose a
portable save function.  Keep saving caller-facing MCP work while making the
small UI compatibility boundary explicit and verifiable.
"""

from __future__ import annotations

import os
import time
from typing import Any

from .live_export import _dismiss_stale_dialogs, _find_window, _focus_window, _tap


class LiveSaveError(RuntimeError):
    """Raised when a Live Set save cannot be proven."""


def title_has_unsaved_changes(title: str) -> bool:
    """Return whether Live's title indicates a dirty saved Set."""

    # Live places the asterisk before the application suffix, e.g.
    # ``My Set* - Ableton Live 12 Standard``.  Keep the test narrow so an
    # asterisk in an unrelated suffix does not look like a dirty Set.
    application_marker = " - Ableton Live"
    head = title.split(application_marker, 1)[0] if application_marker in title else title
    return "*" in head


def save_live_set(*, timeout_seconds: float = 8.0) -> dict[str, Any]:
    """Save the current named Live Set and verify the dirty marker clears."""

    if os.name != "nt":
        raise LiveSaveError("save_set currently requires Windows")

    import win32api
    import win32con
    import win32gui

    live = _find_window(lambda title: "Ableton Live" in title, win32gui)
    if live is None:
        raise LiveSaveError("could not find a running Ableton Live window")

    # A diagnostic/export attempt can leave Live's modal file dialogs visible
    # even after the caller's bridge process exits.  They prevent Ctrl+S from
    # reaching the Set, so clear only the known stale export dialogs before
    # focusing Live.  This is still the internal compatibility boundary of the
    # caller-facing MCP save operation.
    _dismiss_stale_dialogs(win32api, win32gui, win32con)

    before = win32gui.GetWindowText(live)
    if not title_has_unsaved_changes(before):
        return {"status": "already_saved", "title_before": before, "title_after": before}

    _focus_window(live, win32gui)
    win32api.keybd_event(0x11, 0, 0, 0)  # Ctrl
    try:
        _tap(win32api, 0x53)  # S
    finally:
        win32api.keybd_event(0x11, 0, 0x0002, 0)

    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        after = win32gui.GetWindowText(live)
        if not title_has_unsaved_changes(after):
            return {"status": "saved", "title_before": before, "title_after": after}

        save_as = _find_window(
            lambda title: title.startswith("Save Live Set As"), win32gui
        )
        if save_as is not None:
            raise LiveSaveError(
                "Live opened Save Live Set As; the current Set has no reusable save path"
            )
        time.sleep(0.1)

    after = win32gui.GetWindowText(live)
    raise LiveSaveError(
        "Live did not clear its unsaved marker within "
        f"{timeout_seconds:.1f} seconds (title={after!r})"
    )
