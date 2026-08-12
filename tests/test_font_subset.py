from __future__ import annotations

import string
import unittest
from pathlib import Path

from data.preset_letters import PRESET_LETTER_PACKS
from ui.localization import (
    CONSTELLATION_NAMES_JA,
    METEOR_EVENT_NAMES_JA,
    SKY_FEATURE_NAMES_JA,
    STAR_NAMES_JA,
)
from data.font_jp import GLYPHS


FONT_PATH = Path("assets/starwrite_jp10.bdf")
ASCII_PRINTABLE = "".join(
    char for char in string.printable if char not in {"\t", "\n", "\r", "\x0b", "\x0c"}
)
HIRAGANA = "".join(chr(code) for code in range(0x3040, 0x30A0))
KATAKANA = "".join(chr(code) for code in range(0x30A0, 0x3100))
KATAKANA_PHONETIC_EXTENSIONS = "".join(chr(code) for code in range(0x31F0, 0x3200))
FULLWIDTH_DIGITS = "０１２３４５６７８９"
FULLWIDTH_UPPERCASE = "".join(chr(code) for code in range(0xFF21, 0xFF3B))
FULLWIDTH_LOWERCASE = "".join(chr(code) for code in range(0xFF41, 0xFF5B))
JAPANESE_PUNCTUATION = "　。、，．・：；？！ー〜～（）「」『』【】〈〉《》〔〕…‥"
JAPANESE_OPERATORS = "＋−－×÷＝"


def _preset_letter_texts() -> list[str]:
    texts: list[str] = []
    for pack in PRESET_LETTER_PACKS.values():
        for letter in pack:
            texts.append(str(letter["original_text"]))
            texts.extend(str(value) for value in letter.get("translations", {}).values())
    return texts


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
            *SKY_FEATURE_NAMES_JA.values(),
            *STAR_NAMES_JA.values(),
            *_preset_letter_texts(),
            ASCII_PRINTABLE,
        ]
        required = {
            ord(char)
            for label in labels
            for char in label
        }
        self.assertTrue(FONT_PATH.exists())
        self.assertTrue(required <= _font_encodings())

    def test_subset_font_covers_baseline_japanese_ui_characters(self) -> None:
        labels = [
            ASCII_PRINTABLE,
            HIRAGANA,
            KATAKANA,
            KATAKANA_PHONETIC_EXTENSIONS,
            FULLWIDTH_DIGITS,
            FULLWIDTH_UPPERCASE,
            FULLWIDTH_LOWERCASE,
            JAPANESE_PUNCTUATION,
            JAPANESE_OPERATORS,
        ]
        required = {ord(char) for label in labels for char in label}
        self.assertTrue(required <= _font_encodings())

    def test_embedded_font_data_matches_required_subset(self) -> None:
        labels = [
            *CONSTELLATION_NAMES_JA.values(),
            *METEOR_EVENT_NAMES_JA.values(),
            *SKY_FEATURE_NAMES_JA.values(),
            *STAR_NAMES_JA.values(),
            *_preset_letter_texts(),
            ASCII_PRINTABLE,
            HIRAGANA,
            KATAKANA,
            KATAKANA_PHONETIC_EXTENSIONS,
            FULLWIDTH_DIGITS,
            FULLWIDTH_UPPERCASE,
            FULLWIDTH_LOWERCASE,
            JAPANESE_PUNCTUATION,
            JAPANESE_OPERATORS,
        ]
        required = {ord(char) for label in labels for char in label}
        self.assertTrue(required <= set(GLYPHS))


if __name__ == "__main__":
    unittest.main()
