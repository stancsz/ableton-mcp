"""Invoke the repository failure recorder from the skill directory."""

from __future__ import annotations

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from MCP_Server.failure_log import main  # noqa: E402


if __name__ == "__main__":  # pragma: no cover - thin CLI wrapper
    raise SystemExit(main())
