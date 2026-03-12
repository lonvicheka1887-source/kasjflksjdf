"""Basic unit tests for starter app."""

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from app.main import greet


class TestMain(unittest.TestCase):
    def test_greet_default(self) -> None:
        self.assertEqual(greet(), "Hello, world!")

    def test_greet_custom_name(self) -> None:
        self.assertEqual(greet("team"), "Hello, team!")


if __name__ == "__main__":
    unittest.main()
