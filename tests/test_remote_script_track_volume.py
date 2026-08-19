import unittest

from test_remote_script_device_parameter import load_remote_script_module


class FakeVolumeParameter:
    min = 0.0
    max = 1.0

    def __init__(self, value=0.85):
        self.value = value

    def str_for_value(self, value):
        return {0.85: "0.0 dB", 0.9: "+2.0 dB"}.get(value, "sample")


class FakeMixer:
    def __init__(self):
        self.volume = FakeVolumeParameter()


class FakeTrack:
    name = "9 6 Vocals male"

    def __init__(self):
        self.mixer_device = FakeMixer()


class FakeSong:
    def __init__(self):
        self.tracks = [FakeTrack()]


class TrackVolumeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remote_module = load_remote_script_module()

    def setUp(self):
        self.remote = object.__new__(self.remote_module.AbletonMCP)
        self.remote._song = FakeSong()
        self.remote.log_message = lambda message: None

    def test_reads_normalized_value_and_display_samples(self):
        result = self.remote._get_track_volume_info(0)

        self.assertEqual("9 6 Vocals male", result["track_name"])
        self.assertEqual(0.85, result["value"])
        self.assertEqual("0.0 dB", result["current_display"])
        self.assertEqual("0.0 dB", result["samples"][4]["display"])
        self.assertEqual("+2.0 dB", result["samples"][5]["display"])

    def test_sets_value_and_reads_back(self):
        result = self.remote._set_track_volume_value(0, 0.9)

        self.assertEqual(0.85, result["old_value"])
        self.assertEqual(0.9, result["value"])

    def test_rejects_non_finite_or_out_of_range_value(self):
        with self.assertRaises(ValueError):
            self.remote._set_track_volume_value(0, float("nan"))
        with self.assertRaises(ValueError):
            self.remote._set_track_volume_value(0, 1.1)


if __name__ == "__main__":
    unittest.main()
