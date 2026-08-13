from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
OUTPUT = ROOT / "docs" / "preset_letters_review.md"


def _sentence_count(text: str) -> int:
    return len([part for part in re.split(r"[.!?。！？]+", text) if part.strip()])


def _quote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def main() -> None:
    sys.path.insert(0, str(SRC))
    from data.preset_letters import LETTER_INDEX, PRESET_LETTER_PACKS

    letters = [letter for pack in PRESET_LETTER_PACKS.values() for letter in pack]
    language_counts = Counter(letter["original_language"] for letter in letters)
    country_counts = Counter(letter["country_code"] for letter in letters)
    sentence_counts = Counter(_sentence_count(letter["original_text"]) for letter in letters)

    lines: list[str] = [
        "# Starwrite Preset Letters Review Dump",
        "",
        "This file is generated from `src/data/preset_letters.py` and `src/data/preset_letters_extra.py`.",
        "Use it to review tone, coherence, repetition, and translation quality.",
        "",
        "## Review Instructions",
        "",
        "- Keep each `id` stable when suggesting edits.",
        "- Flag any text that feels incoherent, overly templated, too similar to nearby entries, or tonally wrong.",
        "- Prefer small rewrites that preserve the ordinary-life fragment feeling.",
        "- Avoid making every message inspirational, dramatic, or polished.",
        "- Check both the original text and its translation as a pair.",
        "",
        "## Catalog Summary",
        "",
        f"- Total letters: {len(letters)}",
        f"- Indexed pack count: {sum(pack['count'] for pack in LETTER_INDEX['packs'])}",
        f"- Packs: {len(PRESET_LETTER_PACKS)}",
        f"- Original languages: {dict(sorted(language_counts.items()))}",
        f"- Sentence counts: {dict(sorted(sentence_counts.items()))}",
        f"- Top countries: {country_counts.most_common(20)}",
        "",
        "## Letters",
        "",
    ]

    for pack_id, pack in PRESET_LETTER_PACKS.items():
        lines.extend([f"### Pack `{pack_id}`", ""])
        for letter in pack:
            location = " / ".join(
                part
                for part in (letter["country_code"], letter.get("region"), letter.get("city"))
                if part
            )
            lines.extend(
                [
                    f"#### `{letter['id']}`",
                    "",
                    f"- Location: {location}",
                    f"- Original language: `{letter['original_language']}`",
                    f"- Constellations: {', '.join(letter['constellation_ids']) or '-'}",
                    f"- Anchor star IDs: {', '.join(str(value) for value in letter['anchor_star_ids']) or '-'}",
                    f"- Season tags: {', '.join(letter['season_tags']) or '-'}",
                    f"- Time tags: {', '.join(letter['time_tags']) or '-'}",
                    f"- Event tags: {', '.join(letter['event_tags']) or '-'}",
                    f"- Weight: {letter['weight']}",
                    "",
                    "**Original**",
                    "",
                    _quote(letter["original_text"]),
                    "",
                ]
            )
            for language, text in sorted(letter.get("translations", {}).items()):
                lines.extend(
                    [
                        f"**Translation `{language}`**",
                        "",
                        _quote(text),
                        "",
                    ]
                )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"letters={len(letters)}")


if __name__ == "__main__":
    main()
