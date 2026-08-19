import unittest

from test_remote_script_device_parameter import load_remote_script_module


class FakeArrangementClip:
    name = "tail"
    color = 0
    is_midi_clip = False
    is_audio_clip = True
    is_playing = False
    start_time = 10.0
    start_marker = 0.0

    def __init__(self):
        self.end_marker = 10.0
        self.gain = 0.0

    @property
    def end_time(self):
        return self.start_time + (self.end_marker - self.start_marker)

    @property
    def length(self):
        return self.end_time - self.start_time


class FakeTrack:
    name = "female"

    def __init__(self):
        self.arrangement_clips = [FakeArrangementClip()]


class FakeSong:
    def __init__(self):
        self.tracks = [FakeTrack()]


class ArrangementClipTrimTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remote_module = load_remote_script_module()

    def setUp(self):
        self.remote = object.__new__(self.remote_module.AbletonMCP)
        self.remote._song = FakeSong()
        self.remote.log_message = lambda message: None

    def test_trim_uses_global_arrangement_end_time(self):
        result = self.remote._set_arrangement_clip_end_time(0, 0, 15.0)

        self.assertEqual(20.0, result["old_end_time"])
        self.assertEqual(15.0, result["requested_end_time"])
        self.assertEqual(15.0, result["effective_end_time"])
        self.assertEqual(15.0, result["clip_end_time"])
        self.assertEqual(5.0, result["new_end_marker"])

    def test_extension_requires_explicit_restore_flag(self):
        with self.assertRaises(ValueError):
            self.remote._set_arrangement_clip_end_time(0, 0, 21.0)

        result = self.remote._set_arrangement_clip_end_time(
            0, 0, 20.0, allow_extend=True
        )
        self.assertEqual(20.0, result["effective_end_time"])

    def test_arrangement_clip_gain_is_written_and_read_back(self):
        result = self.remote._set_arrangement_clip_gain(0, 0, 2.0)

        self.assertEqual(0.0, result["old_gain_db"])
        self.assertEqual(2.0, result["requested_gain_db"])
        self.assertEqual(2.0, result["new_gain_db"])

    def test_arrangement_clip_gain_rejects_out_of_range_values(self):
        with self.assertRaises(ValueError):
            self.remote._set_arrangement_clip_gain(0, 0, 25.0)


if __name__ == "__main__":
    unittest.main()
