import importlib.util
import sys
import types
import unittest
from pathlib import Path


def load_remote_script_module():
    framework = types.ModuleType("_Framework")
    control_surface_module = types.ModuleType("_Framework.ControlSurface")

    class ControlSurface:
        pass

    control_surface_module.ControlSurface = ControlSurface
    framework.ControlSurface = control_surface_module
    sys.modules.setdefault("_Framework", framework)
    sys.modules.setdefault("_Framework.ControlSurface", control_surface_module)

    path = Path(__file__).parents[1] / "AbletonMCP_Remote_Script" / "__init__.py"
    spec = importlib.util.spec_from_file_location("ableton_remote_script_parameter", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class FakeParameter:
    def __init__(self, name="Release", value=0.25, minimum=0.0, maximum=1.0):
        self.name = name
        self.value = value
        self.min = minimum
        self.max = maximum

    def str_for_value(self, value):
        return "%.2f" % value


class FakeDevice:
    def __init__(self, parameters):
        self.name = "Compressor"
        self.parameters = parameters


class FakeTrack:
    def __init__(self, devices):
        self.name = "3 bass"
        self.devices = devices


class FakeSong:
    def __init__(self):
        self.tracks = [FakeTrack([FakeDevice([FakeParameter()])])]
        self.master_track = FakeTrack([FakeDevice([FakeParameter(name="Threshold")])])
        self.master_track.name = "Master"


class DeviceParameterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remote_module = load_remote_script_module()

    def setUp(self):
        self.remote = object.__new__(self.remote_module.AbletonMCP)
        self.remote._song = FakeSong()
        self.remote.log_message = lambda message: None

    def test_writes_and_reads_back_one_parameter(self):
        result = self.remote._set_device_parameter(0, 0, 0, 0.75)

        self.assertEqual("3 bass", result["track_name"])
        self.assertEqual("Compressor", result["device_name"])
        self.assertEqual("Release", result["parameter_name"])
        self.assertEqual(0.75, result["value"])
        self.assertEqual("0.75", result["display_value"])

    def test_rejects_invalid_indices_and_values(self):
        for args in ((1, 0, 0, 0.5), (-2, 0, 0, 0.5), (0, 1, 0, 0.5), (0, 0, 1, 0.5)):
            with self.assertRaises(IndexError):
                self.remote._set_device_parameter(*args)

        with self.assertRaises(ValueError):
            self.remote._set_device_parameter(0, 0, 0, 1.1)
        with self.assertRaises(ValueError):
            self.remote._set_device_parameter(0, 0, 0, float("nan"))
        with self.assertRaises(ValueError):
            self.remote._set_device_parameter(0, 0, 0, float("inf"))

        with self.assertRaises(TypeError):
            self.remote._set_device_parameter("0", 0, 0, 0.5)

    def test_writes_master_parameter_with_minus_one_track_index(self):
        result = self.remote._set_device_parameter(-1, 0, 0, 0.9)

        self.assertEqual("Master", result["track_name"])
        self.assertEqual("Threshold", result["parameter_name"])
        self.assertEqual(0.9, result["value"])


if __name__ == "__main__":
    unittest.main()
