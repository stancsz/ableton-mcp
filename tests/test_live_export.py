import unittest
from pathlib import Path

from tools.live_export import ExportRequest, LiveExportError, capability_report, validate_request


class LiveExportContractTests(unittest.TestCase):
    def test_valid_main_wav_contract_is_serialized(self):
        result = validate_request(
            ExportRequest(
                output_path=Path(r"C:\exports\mix.wav"),
                render_start="1.1.1",
                render_length_bars=62.0,
                expected_duration_seconds=114.462,
            )
        )
        self.assertEqual("Main", result["rendered_track"])
        self.assertEqual("1.1.1", result["render_start"])
        self.assertEqual(62.0, result["render_length_bars"])

    def test_non_wav_is_rejected(self):
        with self.assertRaises(LiveExportError):
            validate_request(ExportRequest(Path(r"C:\exports\mix.mp3")))

    def test_invalid_range_is_rejected(self):
        with self.assertRaises(LiveExportError):
            validate_request(
                ExportRequest(Path(r"C:\exports\mix.wav"), render_start="8.1")
            )

    def test_capability_report_is_explicit_about_native_api(self):
        report = capability_report()
        self.assertFalse(report["native_live_object_model_export"])
        self.assertIn("ui_bridge_enabled", report)


if __name__ == "__main__":
    unittest.main()
