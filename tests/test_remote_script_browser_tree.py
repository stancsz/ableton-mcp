import importlib.util
import sys
import types
import unittest
from pathlib import Path


def load_remote_script_module():
    """Load the Live script with a minimal stand-in for Ableton's framework."""
    framework = types.ModuleType("_Framework")
    control_surface_module = types.ModuleType("_Framework.ControlSurface")

    class ControlSurface:
        pass

    control_surface_module.ControlSurface = ControlSurface
    framework.ControlSurface = control_surface_module
    sys.modules.setdefault("_Framework", framework)
    sys.modules.setdefault("_Framework.ControlSurface", control_surface_module)

    path = Path(__file__).parents[1] / "AbletonMCP_Remote_Script" / "__init__.py"
    spec = importlib.util.spec_from_file_location("ableton_remote_script", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BrowserItem:
    def __init__(self, name, children=(), uri=None, is_device=False, is_loadable=False):
        self.name = name
        self.children = list(children)
        self.uri = uri or "query:" + name
        self.is_device = is_device
        self.is_loadable = is_loadable


class Browser:
    def __init__(self, instruments):
        self.instruments = instruments


class App:
    def __init__(self, browser):
        self.browser = browser


class RemoteScriptBrowserTreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remote_module = load_remote_script_module()

    def test_browser_tree_contains_nested_children_and_counts(self):
        leaf = BrowserItem("Drift", is_device=True, is_loadable=True)
        nested_folder = BrowserItem("Synths", children=[leaf])
        root = BrowserItem("Instruments", children=[nested_folder])

        remote = object.__new__(self.remote_module.AbletonMCP)
        remote.application = lambda: App(Browser(root))
        remote.log_message = lambda message: None

        result = remote.get_browser_tree("instruments")

        self.assertEqual(result["total_items"], 3)
        self.assertEqual(result["total_folders"], 2)
        self.assertFalse(result["truncated"])
        category = result["categories"][0]
        self.assertEqual(category["name"], "Instruments")
        self.assertEqual(category["children"][0]["name"], "Synths")
        self.assertEqual(category["children"][0]["children"][0]["name"], "Drift")


if __name__ == "__main__":
    unittest.main()
