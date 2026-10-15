import importlib.util
from pathlib import Path
import unittest


class SmokeTest(unittest.TestCase):
    def test_demo_runs(self):
        path = Path(__file__).parents[1] / "src" / "main.py"
        spec = importlib.util.spec_from_file_location("project_main", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertIsNotNone(module.run_demo())


if __name__ == "__main__":
    unittest.main()
