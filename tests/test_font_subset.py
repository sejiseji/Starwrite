from __future__ import annotations

import string
import unittest
from pathlib import Path

from ui.localization import CONSTELLATION_NAMES_JA, METEOR_EVENT_NAMES_JA, STAR_NAMES_JA


FONT_PATH = Path("assets/starwrite_jp10.bdf")


def _font_encodings() -> set[int]:
    encodings: set[int] = set()
    for line in FONT_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("ENCODING "):
            encodings.add(int(line.split()[1]))
    return encodings


class FontSubsetTests(unittest.TestCase):
    def test_subset_font_covers_current_japanese_labels(self) -> None:
        labels = [
            *CONSTELLATION_NAMES_JA.values(),
            *METEOR_EVENT_NAMES_JA.values(),
            *STAR_NAMES_JA.values(),
            string.printable,
        ]
        required = {
            ord(char)
            for label in labels
            for char in label
            if char not in {"\t", "\n", "\r", "\x0b", "\x0c"}
        }
        required.add(12288)
        self.assertTrue(FONT_PATH.exists())
        self.assertTrue(required <= _font_encodings())


if __name__ == "__main__":
    unittest.main()
