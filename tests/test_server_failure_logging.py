from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from MCP_Server.server import AbletonConnection


class BrokenSocket:
    def settimeout(self, timeout: float) -> None:
        pass

    def sendall(self, payload: bytes) -> None:
        raise BrokenPipeError("simulated socket failure")


class ServerFailureLoggingTests(unittest.TestCase):
    def test_send_command_writes_a_structural_failure_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            previous = os.environ.get("ABLETON_MCP_FAILURE_DIR")
            os.environ["ABLETON_MCP_FAILURE_DIR"] = directory
            try:
                connection = AbletonConnection("localhost", 9877, sock=BrokenSocket())
                with self.assertRaises(Exception):
                    connection.send_command("set_tempo", {"tempo": 120})

                files = list(Path(directory).glob("*.json"))
                self.assertEqual(1, len(files))
                record = json.loads(files[0].read_text(encoding="utf-8"))
                self.assertEqual("send_command", record["operation"])
                self.assertEqual("set_tempo", record["context"]["command_type"])
                self.assertNotIn("tempo", record["context"])
            finally:
                if previous is None:
                    os.environ.pop("ABLETON_MCP_FAILURE_DIR", None)
                else:
                    os.environ["ABLETON_MCP_FAILURE_DIR"] = previous


if __name__ == "__main__":
    unittest.main()
