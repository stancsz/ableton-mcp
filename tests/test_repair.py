from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from MCP_Server.failure_log import get_failure, record_failure
from MCP_Server.repair import run_repair, run_syntax_check


class RepairTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.failure_dir = Path(self.temp_dir.name)
        self.repo_root = Path(__file__).resolve().parents[1]

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_syntax_check_is_read_only_and_covers_repo_sources(self) -> None:
        result = run_syntax_check(self.repo_root)
        self.assertTrue(result["success"], result)
        self.assertGreaterEqual(result["checked_files"], 5)

    def test_run_repair_records_evidence_and_enforces_limit(self) -> None:
        path = record_failure(
            "test",
            "connection",
            "connection refused",
            {"host": "localhost", "port": 9877},
            failure_dir=self.failure_dir,
        )
        assert path is not None
        failure_id = path.stem

        for attempt in range(3):
            result = run_repair(
                failure_id,
                "syntax_check",
                root=self.repo_root,
                failure_dir=self.failure_dir,
            )
            self.assertTrue(result["success"], result)
            self.assertEqual(attempt + 1, result["attempts"])

        with self.assertRaises(RuntimeError):
            run_repair(
                failure_id,
                "syntax_check",
                root=self.repo_root,
                failure_dir=self.failure_dir,
            )

        record = get_failure(failure_id, failure_dir=self.failure_dir)
        self.assertEqual(3, record["attempts"])
        self.assertEqual(3, len(record["repair_history"]))


if __name__ == "__main__":
    unittest.main()
