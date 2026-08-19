import unittest

from tools.live_save import title_has_unsaved_changes


class LiveSaveTests(unittest.TestCase):
    def test_detects_live_dirty_marker(self):
        self.assertTrue(
            title_has_unsaved_changes(
                "maybe-edm-mcp-fixed-checkpoint-2026-08-17* - Ableton Live 12 Standard"
            )
        )

    def test_ignores_clean_title(self):
        self.assertFalse(
            title_has_unsaved_changes(
                "maybe-edm-mcp-fixed-checkpoint-2026-08-17 - Ableton Live 12 Standard"
            )
        )

    def test_does_not_treat_application_suffix_as_dirty(self):
        self.assertFalse(title_has_unsaved_changes("Set - Ableton Live 12 Standard*"))


if __name__ == "__main__":
    unittest.main()
