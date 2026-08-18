import json
import unittest

from MCP_Server import server


class FakeConnection:
    def __init__(self):
        self.calls = []

    def send_command(self, command_type, params):
        self.calls.append((command_type, params))
        return {
            "parameter_name": "Release",
            "value": 0.5,
            "display_value": "100 ms",
        }


class ServerDeviceParameterTests(unittest.TestCase):
    def test_tool_forwards_exact_payload_and_returns_readback(self):
        fake = FakeConnection()
        original = server.get_ableton_connection
        server.get_ableton_connection = lambda: fake
        try:
            result = server.set_device_parameter(None, 3, 0, 5, 0.5)
        finally:
            server.get_ableton_connection = original

        self.assertEqual(
            ("set_device_parameter", {
                "track_index": 3,
                "device_index": 0,
                "parameter_index": 5,
                "value": 0.5,
            }),
            fake.calls[0],
        )
        self.assertEqual(0.5, json.loads(result)["value"])


if __name__ == "__main__":
    unittest.main()
