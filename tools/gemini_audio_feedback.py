"""Compatibility adapter; canonical implementation is maintained by MCS."""
import importlib.util
import os
import sys
from pathlib import Path

source = Path(__file__).resolve()
backend = next((parent for parent in source.parents if (parent / "MCP_Server").is_dir()), None)
if backend is None:
    raise RuntimeError("Cannot locate the Ableton backend repository")
root = Path(os.environ.get("MCS_ROOT", str(backend.parent / "music-creation-skills"))).expanduser().resolve()
target = root / 'tools/gemini_audio_feedback.py'
if not target.is_file():
    raise RuntimeError("MCS implementation unavailable; set MCS_ROOT to its repository")
spec = importlib.util.spec_from_file_location("mcs_compat_" + __name__.replace(".", "_"), target)
implementation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(implementation)
if __name__ == "__main__":
    raise SystemExit(implementation.main())
else:
    # Export the actual module so existing monkeypatches affect its own globals.
    sys.modules[__name__] = implementation
    globals().update({name: value for name, value in vars(implementation).items()
                      if name not in {"__name__", "__file__", "__spec__", "__package__"}})
