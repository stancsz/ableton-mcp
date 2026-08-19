"""Guarded Windows bridge for Ableton Live's Export Audio/Video dialog.

The public Live Object Model can inspect and edit a Set, but it does not expose
offline audio rendering.  This module keeps the export operation MCP-callable
while making the missing native capability explicit: it drives only the
foreground Live export dialog through pywin32, then validates the file that
actually appeared on disk.  A shortcut or a successful click is never enough.
"""

from __future__ import annotations

import os
import re
import time
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


_BAR_BEAT_TICK = re.compile(r"^\d+\.\d+\.\d+$")
_WM_SETTEXT = 0x000C
_BM_CLICK = 0x00F5
_KEYEVENTF_KEYUP = 0x0002
_SWP_NOSIZE = 0x0001
_SWP_NOMOVE = 0x0002
_SWP_SHOWWINDOW = 0x0040
_HWND_TOPMOST = -1
_EXPORT_TIMEOUT_SECONDS = 600.0


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

    pywin32 = _module_available("win32gui") and _module_available("win32api")
    return {
        "native_live_object_model_export": False,
        "ui_bridge_supported": os.name == "nt",
        "ui_bridge_enabled": os.environ.get("ABLETON_MCP_UI_EXPORT") == "1",
        "dependencies": {
            "pywin32": pywin32,
        },
        "bridge": "direct_win32_foreground_dialog" if pywin32 else None,
        "reason": (
            "Ableton exposes Export Audio/Video in the application UI, but not "
            "as a public Remote Script/Live Object Model render function."
        ),
    }


def export_audio(request: ExportRequest) -> dict[str, Any]:
    """Run the guarded desktop export bridge and validate the resulting WAV."""

    contract = validate_request(request)
    report = capability_report()
    if not report["ui_bridge_supported"]:
        raise LiveExportError("export_audio UI bridge is currently Windows-only")
    if not report["dependencies"]["pywin32"]:
        raise LiveExportError("pywin32 is required for the direct Windows export bridge")
    if not report["ui_bridge_enabled"]:
        raise LiveExportError(
            "UI export is disabled; set ABLETON_MCP_UI_EXPORT=1 for the guarded desktop bridge"
        )
    if request.sample_rate != 44100 or request.bit_depth != 24:
        raise LiveExportError(
            "the verified Live dialog bridge currently supports 44.1 kHz / 24-bit WAV only"
        )
    downloads = (
        Path(os.environ.get("USERPROFILE", str(Path.home()))) / "Downloads"
    ).resolve()
    if request.output_path.parent.resolve() != downloads:
        raise LiveExportError(
            "the verified Windows save bridge currently requires output_path in the user's Downloads folder"
        )

    output_path = request.output_path
    if output_path.exists():
        raise LiveExportError(f"refusing to overwrite existing output: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    _export_in_live(request)
    metadata = _validate_rendered_wav(request)
    return {
        "status": "exported",
        **contract,
        **metadata,
        "capabilities": report,
    }


def _export_in_live(request: ExportRequest) -> None:
    """Drive Live's dialog with direct Win32 input while it is foreground."""

    import win32api
    import win32con
    import win32gui

    # Keep a baseline so a broken Common Dialog filename update cannot make
    # the bridge wait for the requested path while silently rewriting the
    # previously selected WAV.  The requested path is guaranteed not to exist
    # by ``export_audio``; any other changed WAV is therefore a hard mismatch.
    baseline_wavs = {
        path: (path.stat().st_size, path.stat().st_mtime_ns)
        for path in request.output_path.parent.glob("*.wav")
        if path.is_file()
    }

    live = _find_window(lambda title: "Ableton Live" in title)
    if live is None:
        raise LiveExportError("could not find a running Ableton Live window")
    # A user-initiated fallback (or a previous bridge attempt) may already
    # have the exact render dialog open.  Do not dismiss that valid dialog and
    # then send a second shortcut; reuse it and continue with the same guarded
    # field/file validation below.
    dialog = _find_window(
        lambda title: title == "Export Audio/Video", win32gui=win32gui
    )
    if dialog is None:
        _dismiss_stale_dialogs(win32api, win32gui, win32con)
        _focus_window(live, win32gui)
        _hotkey(win32api, 0x11, 0x10, 0x52)  # Ctrl+Shift+R
        dialog = _wait_for_window(
            lambda title: title == "Export Audio/Video", timeout=2.0, win32gui=win32gui
        )
    if dialog is None:
        # Some Windows desktop states accept SendInput's scan-code path but
        # drop the older keybd_event virtual-key sequence.  pyautogui is an
        # optional local fallback only for this application-dialog boundary;
        # the MCP contract and post-render validation remain unchanged.
        try:
            import pyautogui

            pyautogui.PAUSE = 0.05
            pyautogui.hotkey("ctrl", "shift", "r")
        except ImportError:
            pass
        dialog = _wait_for_window(
            lambda title: title == "Export Audio/Video", timeout=5.0, win32gui=win32gui
        )
    if dialog is None:
        raise LiveExportError("Live did not open the Export Audio/Video dialog")
    _focus_window(dialog, win32gui)

    # The custom Live dialog has no child controls for reliable UIA readback.
    # On a freshly opened dialog, three tabs land on Render Start and the next
    # tab lands on Render Length. Main is the default rendered track; readback
    # of the finished WAV is the authoritative completion proof.
    left, top, _, _ = win32gui.GetWindowRect(dialog)
    for _ in range(3):
        _tap(win32api, 0x09)
    _replace_field(win32api, request.render_start or "1.1.1")
    _tap(win32api, 0x09)
    _replace_field(
        win32api,
        str(request.render_length_bars) if request.render_length_bars is not None else "",
    )

    if not _click_child(dialog, "Export", win32gui, win32con):
        _click_at(win32api, left + 118, top + 595)

    save_dialog = _wait_for_window(
        lambda title: title.startswith("Save Audio File As"),
        timeout=5.0,
        win32gui=win32gui,
    )
    if save_dialog is None:
        raise LiveExportError("Live did not open the audio file save dialog")
    _focus_window(save_dialog, win32gui)

    edits: list[int] = []
    win32gui.EnumChildWindows(
        save_dialog,
        lambda hwnd, _param: edits.append(hwnd)
        if win32gui.GetClassName(hwnd).lower() == "edit"
        else None,
        None,
    )
    if not edits:
        raise LiveExportError("could not find the filename field in Live's save dialog")
    # Live opens this dialog in Downloads. Set only the filename; writing a
    # full path into the common-dialog edit can leave Live's internal filename
    # cache pointing at a previous export even though the visible text changes.
    # WM_SETTEXT changes the visible field but not Live's internal filename
    # cache on this Windows common-dialog build. Paste into the real Edit child
    # so the host receives the same committed text as a human filename entry.
    _replace_field_via_paste(win32api, edits[0], request.output_path.name)
    # Prefer the dialog's bottom action button after the paste. Enter can
    # submit the selected file-list row on some common-dialog builds even
    # when the filename edit received the paste. The leftmost bottom button
    # is the visible Save/Open action; the rightmost one is Cancel.
    buttons: list[tuple[int, int, int, int]] = []
    dialog_left, dialog_top, dialog_right, dialog_bottom = win32gui.GetWindowRect(
        save_dialog
    )
    win32gui.EnumChildWindows(
        save_dialog,
        lambda hwnd, _param: buttons.append(win32gui.GetWindowRect(hwnd))
        if win32gui.GetClassName(hwnd).lower() == "button"
        and win32gui.GetWindowRect(hwnd)[1] > dialog_bottom - 100
        else None,
        None,
    )
    if buttons:
        left, top, right, bottom = min(buttons, key=lambda rect: rect[0])
        _click_at(win32api, (left + right) // 2, (top + bottom) // 2)
    else:
        edit_left, edit_top, edit_right, edit_bottom = win32gui.GetWindowRect(edits[0])
        _click_at(win32api, (edit_left + edit_right) // 2, (edit_top + edit_bottom) // 2)
        _tap(win32api, 0x0D)
    time.sleep(0.35)

    if _find_window(lambda title: title.startswith("Save Audio File As"), win32gui) is not None:
        retry_buttons: list[tuple[int, int, int, int]] = []
        win32gui.EnumChildWindows(
            save_dialog,
            lambda hwnd, _param: retry_buttons.append(win32gui.GetWindowRect(hwnd))
            if win32gui.GetClassName(hwnd).lower() == "button"
            and win32gui.GetWindowRect(hwnd)[1] > dialog_bottom - 100
            else None,
            None,
        )
        if retry_buttons:
            left, top, right, bottom = min(retry_buttons, key=lambda rect: rect[0])
            _click_at(win32api, (left + right) // 2, (top + bottom) // 2)
        else:
            # Last-resort geometry for a dialog that hides its child buttons.
            _click_at(win32api, dialog_right - 170, dialog_bottom - 38)

    confirm = _wait_for_window(
        lambda title: title == "Confirm Save As", timeout=1.5, win32gui=win32gui
    )
    if confirm is not None:
        _focus_window(confirm, win32gui)
        _click_child(confirm, "No", win32gui, win32con)
        raise LiveExportError(
            "Live requested overwrite confirmation; export bridge refused to overwrite"
        )

    deadline = time.monotonic() + _EXPORT_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        if request.output_path.exists() and request.output_path.stat().st_size > 44:
            # Live can leave the dialog closed a fraction before the last write.
            size = request.output_path.stat().st_size
            time.sleep(0.75)
            if request.output_path.exists() and request.output_path.stat().st_size == size:
                return
        unexpected = []
        for path in request.output_path.parent.glob("*.wav"):
            if not path.is_file() or path == request.output_path:
                continue
            current = (path.stat().st_size, path.stat().st_mtime_ns)
            if path not in baseline_wavs or current != baseline_wavs[path]:
                unexpected.append(path)
        if unexpected:
            names = ", ".join(str(path) for path in unexpected[:3])
            raise LiveExportError(
                "Live wrote an unexpected WAV path while the requested output "
                f"was absent; refusing to report success: {names}"
            )
        time.sleep(0.25)
    raise LiveExportError(
        "Live export did not produce a stable output within "
        f"{_EXPORT_TIMEOUT_SECONDS:.0f} seconds"
    )


def _dismiss_stale_dialogs(win32api: Any, win32gui: Any, win32con: Any) -> None:
    """Close dialogs left by an interrupted export without accepting overwrite."""

    confirm = _find_window(lambda title: title == "Confirm Save As", win32gui)
    if confirm is not None:
        _focus_window(confirm, win32gui)
        _click_child(confirm, "No", win32gui, win32con)
    save_dialog = _find_window(
        lambda title: title.startswith("Save Audio File As"), win32gui
    )
    if save_dialog is not None:
        _focus_window(save_dialog, win32gui)
        if not _click_child(save_dialog, "Cancel", win32gui, win32con):
            _tap(win32api, 0x1B)
    export_dialog = _find_window(
        lambda title: title == "Export Audio/Video", win32gui
    )
    if export_dialog is not None:
        _focus_window(export_dialog, win32gui)
        _tap(win32api, 0x1B)


def _validate_rendered_wav(request: ExportRequest) -> dict[str, Any]:
    try:
        with wave.open(str(request.output_path), "rb") as wav:
            channels = wav.getnchannels()
            sample_rate = wav.getframerate()
            sample_width = wav.getsampwidth()
            frames = wav.getnframes()
    except (OSError, wave.Error) as exc:
        raise LiveExportError(f"rendered file is not a readable WAV: {exc}") from exc

    duration = frames / sample_rate if sample_rate else 0.0
    expected_width = request.bit_depth // 8
    if channels != 2 or sample_rate != request.sample_rate or sample_width != expected_width:
        raise LiveExportError(
            "rendered WAV format mismatch: "
            f"channels={channels}, sample_rate={sample_rate}, bit_depth={sample_width * 8}"
        )
    if request.expected_duration_seconds is not None and abs(
        duration - request.expected_duration_seconds
    ) > 0.1:
        raise LiveExportError(
            "rendered WAV duration mismatch: "
            f"expected {request.expected_duration_seconds:.3f}s, got {duration:.3f}s"
        )
    return {
        "duration_seconds": round(duration, 6),
        "channels": channels,
        "sample_rate_hz": sample_rate,
        "bit_depth": sample_width * 8,
        "file_size_bytes": request.output_path.stat().st_size,
    }


def _find_window(predicate: Callable[[str], bool], win32gui: Any | None = None) -> int | None:
    if win32gui is None:
        import win32gui as win32gui_module

        win32gui = win32gui_module
    matches: list[int] = []
    win32gui.EnumWindows(
        lambda hwnd, _param: matches.append(hwnd)
        if win32gui.IsWindowVisible(hwnd) and predicate(win32gui.GetWindowText(hwnd))
        else None,
        None,
    )
    return matches[0] if matches else None


def _wait_for_window(
    predicate: Callable[[str], bool], *, timeout: float, win32gui: Any
) -> int | None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        found = _find_window(predicate, win32gui)
        if found is not None:
            return found
        time.sleep(0.05)
    return None


def _focus_window(hwnd: int, win32gui: Any) -> None:
    import win32api

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # SetForegroundWindow does not restore a minimized Live window. Restore it
    # first or the subsequent shortcut can land in the wrong desktop window.
    win32gui.ShowWindow(hwnd, 9)  # SW_RESTORE
    win32gui.SetWindowPos(
        hwnd,
        _HWND_TOPMOST,
        left,
        top,
        right - left,
        bottom - top,
        _SWP_NOMOVE | _SWP_NOSIZE | _SWP_SHOWWINDOW,
    )
    try:
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        # Windows can reject foreground changes from a background process.
        # Pressing and releasing Alt grants the calling thread the normal
        # foreground-transfer allowance; keep the fallback inside the bridge
        # instead of making an otherwise valid MCP export fail on focus alone.
        _tap(win32api, 0x12)  # Alt
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)
    # Windows can silently reject a foreground transfer without raising.  A
    # shortcut sent immediately after that no-op lands in the caller window
    # (or nowhere), which previously made otherwise valid exports fail at the
    # "Export Audio/Video" dialog boundary.  Re-grant foreground permission
    # when the readback proves that Live/dialog did not actually become active.
    if win32gui.GetForegroundWindow() != hwnd:
        _tap(win32api, 0x12)  # Alt
        time.sleep(0.05)
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.25)


def _tap(win32api: Any, virtual_key: int) -> None:
    win32api.keybd_event(virtual_key, 0, 0, 0)
    win32api.keybd_event(virtual_key, 0, _KEYEVENTF_KEYUP, 0)


def _hotkey(win32api: Any, modifier: int, second_modifier: int, key: int) -> None:
    for virtual_key in (modifier, second_modifier, key):
        win32api.keybd_event(virtual_key, 0, 0, 0)
        time.sleep(0.03)
    for virtual_key in (key, second_modifier, modifier):
        win32api.keybd_event(virtual_key, 0, _KEYEVENTF_KEYUP, 0)
        time.sleep(0.03)


def _replace_field(win32api: Any, text: str, *, commit: bool = True) -> None:
    win32api.keybd_event(0x11, 0, 0, 0)
    _tap(win32api, 0x41)  # Ctrl+A
    win32api.keybd_event(0x11, 0, _KEYEVENTF_KEYUP, 0)
    for char in text:
        vk_scan = win32api.VkKeyScan(char)
        if vk_scan == -1:
            raise LiveExportError(f"cannot type character in Live dialog: {char!r}")
        virtual_key = vk_scan & 0xFF
        shift_state = (vk_scan >> 8) & 0xFF
        if shift_state & 1:
            win32api.keybd_event(0x10, 0, 0, 0)
        _tap(win32api, virtual_key)
        if shift_state & 1:
            win32api.keybd_event(0x10, 0, _KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)
    if commit:
        _tap(win32api, 0x0D)


def _replace_field_via_paste(win32api: Any, hwnd: int, text: str) -> None:
    """Set a native edit field without lossy per-character key injection."""

    import win32clipboard
    import win32con
    import win32gui

    previous: str | None = None
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            previous = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32con.CF_UNICODETEXT)
    except Exception as exc:
        raise LiveExportError(f"could not prepare the filename clipboard text: {exc}") from exc
    finally:
        try:
            win32clipboard.CloseClipboard()
        except Exception:
            pass

    # The filename is hosted by a ComboBox on this Windows build. Updating
    # the parent first keeps the common-dialog's internal filename cache in
    # sync; the clipboard paste then follows the same input path as a human
    # entry and handles long names without dropped characters.
    parent = win32gui.GetParent(hwnd)
    if parent and win32gui.GetClassName(parent).lower() == "combobox":
        win32gui.SendMessage(parent, win32con.WM_SETTEXT, 0, text)
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    _click_at(win32api, (left + right) // 2, (top + bottom) // 2)
    try:
        win32gui.SetFocus(hwnd)
    except Exception:
        # A real click already transfers focus on the mixed DirectUI/Win32
        # common-dialog host. Some Windows builds reject SetFocus across
        # threads even though subsequent keyboard input is accepted.
        pass
    win32api.keybd_event(0x11, 0, 0, 0)  # Ctrl
    _tap(win32api, 0x41)  # A
    win32api.keybd_event(0x11, 0, _KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, 0, 0)  # Ctrl
    _tap(win32api, 0x56)  # V
    win32api.keybd_event(0x11, 0, _KEYEVENTF_KEYUP, 0)
    time.sleep(0.15)

    # Restore a text clipboard when possible; export should not permanently
    # replace the user's clipboard just because the MCP bridge ran.
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        if previous is not None:
            win32clipboard.SetClipboardText(previous, win32con.CF_UNICODETEXT)
    except Exception:
        pass
    finally:
        try:
            win32clipboard.CloseClipboard()
        except Exception:
            pass


def _click_child(hwnd: int, label: str, win32gui: Any, win32con: Any) -> bool:
    import win32api

    matches: list[int] = []
    win32gui.EnumChildWindows(
        hwnd,
        lambda child, _param: matches.append(child)
        if win32gui.GetWindowText(child).strip().lstrip("&").lower()
        == label.lstrip("&").lower()
        else None,
        None,
    )
    if not matches:
        return False
    # BM_CLICK is ignored by Live's mixed Win32/DirectUI common-dialog host on
    # some Windows builds. A real click at the child center is reliable once
    # the parent has been foregrounded.
    left, top, right, bottom = win32gui.GetWindowRect(matches[0])
    _click_at(win32api, (left + right) // 2, (top + bottom) // 2)
    return True


def _click_at(win32api: Any, x: int, y: int) -> None:
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(0x0002, 0, 0, 0, 0)
    win32api.mouse_event(0x0004, 0, 0, 0, 0)


def _module_available(name: str) -> bool:
    try:
        __import__(name)
    except ImportError:
        return False
    return True
