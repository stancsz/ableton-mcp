from __future__ import annotations

import json
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from MCP_Server.failure_log import (
    append_repair_attempt,
    get_failure,
    list_failures,
    record_failure,
    resolve_failure,
)


class FailureLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.failure_dir = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_record_is_atomic_sanitized_and_structural(self) -> None:
        path = record_failure(
            "mcp_server",
            "send_command",
            "Bearer super-secret C:\\Users\\stanc\\private.wav api_key=another-secret",
            {
                "command_type": "get_session_info",
                "host": "localhost",
                "port": 9877,
                "path": "C:\\Users\\stanc\\private.wav",
                "user_prompt": "do not persist this",
            },
            failure_dir=self.failure_dir,
        )

        self.assertIsNotNone(path)
        assert path is not None
        self.assertTrue(path.is_file())
        self.assertEqual([], list(self.failure_dir.glob("*.tmp")))

        record = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual("open", record["status"])
        self.assertEqual("get_session_info", record["context"]["command_type"])
        self.assertNotIn("path", record["context"])
        self.assertNotIn("user_prompt", record["context"])
        raw = path.read_text(encoding="utf-8")
        self.assertNotIn("super-secret", raw)
        self.assertNotIn("another-secret", raw)
        self.assertNotIn("C:\\Users\\stanc", raw)

    def test_concurrent_records_do_not_overwrite_each_other(self) -> None:
        def write_one(index: int) -> Path | None:
            return record_failure(
                "test",
                f"operation-{index}",
                "simulated failure",
                {"attempt": index},
                failure_dir=self.failure_dir,
            )

        with ThreadPoolExecutor(max_workers=8) as executor:
            paths = list(executor.map(write_one, range(24)))

        self.assertEqual(24, len([path for path in paths if path is not None]))
        records = list_failures(failure_dir=self.failure_dir)
        self.assertEqual(24, len(records))
        self.assertEqual(24, len({record["id"] for record in records}))

    def test_repair_history_and_resolution_are_persisted(self) -> None:
        path = record_failure(
            "test",
            "syntax_check",
            "broken source",
            failure_dir=self.failure_dir,
        )
        assert path is not None
        failure_id = path.stem

        updated = append_repair_attempt(
            failure_id,
            "syntax_check",
            success=True,
            details="checked 4 files",
            failure_dir=self.failure_dir,
        )
        self.assertEqual(1, updated["attempts"])
        self.assertEqual("syntax_check", updated["repair_history"][0]["action"])

        resolved = resolve_failure(
            failure_id,
            "unit test and MCP smoke test passed",
            failure_dir=self.failure_dir,
        )
        self.assertEqual("resolved", resolved["status"])
        self.assertEqual("resolved", get_failure(failure_id, failure_dir=self.failure_dir)["status"])


if __name__ == "__main__":
    unittest.main()
