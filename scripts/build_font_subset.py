from __future__ import annotations

import pprint
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SOURCE_BDF = ROOT / "assets" / "umplus_j10r.bdf"
SUBSET_BDF = ROOT / "assets" / "starwrite_jp10.bdf"
FONT_DATA = SRC / "data" / "font_jp.py"

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
SETUP_UI_JA = (
    "位置情報は取得しません"
    "表示言語を選択"
    "国を選択"
    "都市を選択"
    "空を確認"
    "戻る"
    "開始"
    "前へ"
    "次へ"
    "準備"
    "読み込みの為、画面が一時的に固まることがあります。"
    "そのまましばらくお待ちください。"
    "日本アメリカイギリスフランスドイツフィンランドオーストラリアニュージーランド"
    "ブラジル南アフリカシンガポールインドカナダ韓国台湾タイ"
    "東京福島札幌仙台新潟名古屋大阪広島福岡那覇"
    "ニューヨークロサンゼルスシカゴシアトルホノルルロンドンパリベルリン"
    "ヘルシンキタンペレシドニーメルボルンホバートオークランドサンパウロ"
    "ケープタウンデリートロントバンクーバーソウル台北バンコク"
)
MENU_UI_JA = (
    "表示情報補助星座スライダー左右場所変更イベント情報言語"
    "空の設定を変更"
    "言語・国・都市の選択へ戻ります。"
    "現在の星空表示は中断されます。"
    "はい"
    "いいえ"
)
COMMON_LETTER_KANJI = (
    "日本語生活仕事学校会社家族友達父母兄弟姉妹子供朝昼夕夜今日明日昨日今年去年"
    "時間分秒年月日春夏秋冬空星月雨雪風雲海山川街駅道電車電話部屋窓台所本音声"
    "手足顔目耳口心気持好き嫌少多大小高中低新古早遅近遠明暗白黒赤青帰行来見聞"
    "話読書食飲買売作使持待歩走立座寝起笑泣忘覚終始開閉入出上下午前後右左"
)


def _import_app_data():
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(SRC))
    from data.constellation_descriptions import CONSTELLATION_DESCRIPTIONS
    from data.moon_descriptions import MOON_DESCRIPTIONS, MOON_PHASE_DESCRIPTIONS
    from data.preset_letters import PRESET_LETTER_PACKS
    from data.sky_feature_descriptions import SKY_FEATURE_DESCRIPTIONS
    from data.star_descriptions import STAR_DESCRIPTIONS
    from ui.localization import (
        CONSTELLATION_NAMES_JA,
        METEOR_EVENT_NAMES_JA,
        SKY_FEATURE_NAMES_JA,
        STAR_NAMES_JA,
    )

    return (
        PRESET_LETTER_PACKS,
        CONSTELLATION_DESCRIPTIONS,
        SKY_FEATURE_DESCRIPTIONS,
        STAR_DESCRIPTIONS,
        CONSTELLATION_NAMES_JA,
        METEOR_EVENT_NAMES_JA,
        SKY_FEATURE_NAMES_JA,
        STAR_NAMES_JA,
        MOON_DESCRIPTIONS,
        MOON_PHASE_DESCRIPTIONS,
    )


def _required_text() -> str:
    (
        letter_packs,
        constellation_descriptions,
        sky_feature_descriptions,
        star_descriptions,
        constellation_names,
        meteor_event_names,
        sky_feature_names,
        star_names,
        moon_descriptions,
        moon_phase_descriptions,
    ) = _import_app_data()
    parts = [
        ASCII_PRINTABLE,
        HIRAGANA,
        KATAKANA,
        KATAKANA_PHONETIC_EXTENSIONS,
        FULLWIDTH_DIGITS,
        FULLWIDTH_UPPERCASE,
        FULLWIDTH_LOWERCASE,
        JAPANESE_PUNCTUATION,
        JAPANESE_OPERATORS,
        SETUP_UI_JA,
        MENU_UI_JA,
        COMMON_LETTER_KANJI,
        *constellation_names.values(),
        *meteor_event_names.values(),
        *sky_feature_names.values(),
        *star_names.values(),
        *moon_descriptions.values(),
    ]
    for descriptions in moon_phase_descriptions.values():
        parts.extend(str(value) for value in descriptions.values())
    for pack in letter_packs.values():
        for letter in pack:
            parts.append(str(letter["original_text"]))
            parts.extend(str(value) for value in letter.get("translations", {}).values())
    for descriptions in constellation_descriptions.values():
        for lines in descriptions.values():
            parts.extend(lines)
    for descriptions in sky_feature_descriptions.values():
        for lines in descriptions.values():
            parts.extend(lines)
    for descriptions in star_descriptions.values():
        for key in ("ja", "en"):
            parts.extend(descriptions.get(key, ()))
    return "".join(parts)


def _read_bdf_glyphs(path: Path) -> tuple[list[str], dict[int, list[str]], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header: list[str] = []
    glyphs: dict[int, list[str]] = {}
    footer: list[str] = ["ENDFONT"]
    index = 0
    while index < len(lines):
        if lines[index].startswith("CHARS "):
            header = lines[:index]
            index += 1
            break
        index += 1
    while index < len(lines):
        if lines[index] == "ENDFONT":
            break
        if not lines[index].startswith("STARTCHAR "):
            index += 1
            continue
        start = index
        encoding: int | None = None
        while index < len(lines) and lines[index] != "ENDCHAR":
            if lines[index].startswith("ENCODING "):
                encoding = int(lines[index].split()[1])
            index += 1
        block = lines[start : index + 1]
        if encoding is not None:
            glyphs[encoding] = block
        index += 1
    return header, glyphs, footer


def _write_subset_bdf(required: set[int]) -> None:
    header, source_glyphs, footer = _read_bdf_glyphs(SOURCE_BDF)
    if SUBSET_BDF.exists():
        _subset_header, subset_glyphs, _subset_footer = _read_bdf_glyphs(SUBSET_BDF)
        source_glyphs = {**source_glyphs, **subset_glyphs}
    required.add(ord("?"))
    missing = sorted(required - set(source_glyphs))
    if missing:
        values = ", ".join(f"U+{codepoint:04X}" for codepoint in missing[:24])
        extra = " ..." if len(missing) > 24 else ""
        raise SystemExit(f"missing glyphs in {SOURCE_BDF}: {values}{extra}")
    ordered = [codepoint for codepoint in sorted(source_glyphs) if codepoint in required]
    lines = [*header, f"CHARS {len(ordered)}"]
    for codepoint in ordered:
        lines.extend(source_glyphs[codepoint])
    lines.extend(footer)
    SUBSET_BDF.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _glyph_data_from_subset() -> dict[int, tuple[int, tuple[str, ...]]]:
    source = SUBSET_BDF.read_text(encoding="utf-8").splitlines()
    glyphs: dict[int, tuple[int, tuple[str, ...]]] = {}
    ascent = 9
    cell_w = 10
    cell_h = 13
    index = 0
    while index < len(source):
        if not source[index].startswith("STARTCHAR "):
            index += 1
            continue
        encoding = advance = width = height = xoff = yoff = None
        bitmap: list[int] = []
        index += 1
        while index < len(source) and source[index] != "ENDCHAR":
            line = source[index]
            if line.startswith("ENCODING "):
                encoding = int(line.split()[1])
            elif line.startswith("DWIDTH "):
                advance = int(line.split()[1])
            elif line.startswith("BBX "):
                _, w_value, h_value, xo_value, yo_value = line.split()
                width = int(w_value)
                height = int(h_value)
                xoff = int(xo_value)
                yoff = int(yo_value)
            elif line == "BITMAP":
                index += 1
                while index < len(source) and source[index] != "ENDCHAR":
                    bitmap.append(int(source[index], 16))
                    index += 1
                continue
            index += 1
        if None not in (encoding, advance, width, height, xoff, yoff):
            rows = [["0"] * cell_w for _ in range(cell_h)]
            y_start = max(0, min(cell_h - height, ascent - yoff - height))
            x_start = max(0, xoff)
            padded_bits = ((width + 7) // 8) * 8
            for row_index, row_value in enumerate(bitmap[:height]):
                dest_y = y_start + row_index
                if not 0 <= dest_y < cell_h:
                    continue
                for bit_index in range(width):
                    dest_x = x_start + bit_index
                    if 0 <= dest_x < cell_w and row_value & (1 << (padded_bits - 1 - bit_index)):
                        rows[dest_y][dest_x] = "7"
            glyphs[int(encoding)] = (min(int(advance), cell_w), tuple("".join(row) for row in rows))
        index += 1
    return glyphs


def _write_font_data(glyphs: dict[int, tuple[int, tuple[str, ...]]]) -> None:
    lines = [
        "from __future__ import annotations",
        "",
        "# Generated from assets/starwrite_jp10.bdf for Pyxel Web bitmap rendering.",
        "FONT_IMAGE_BANK = 2",
        "FONT_IMAGE_BANKS = (0, 1, 2)",
        "FONT_CELL_WIDTH = 10",
        "FONT_CELL_HEIGHT = 13",
        "FONT_COLUMNS = 25",
        "",
        "GLYPHS: dict[int, tuple[int, tuple[str, ...]]] = "
        + pprint.pformat(glyphs, width=120, sort_dicts=True),
        "",
    ]
    FONT_DATA.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    required = {ord(char) for char in _required_text()}
    _write_subset_bdf(required)
    _write_font_data(_glyph_data_from_subset())
    print(f"wrote {SUBSET_BDF.relative_to(ROOT)}")
    print(f"wrote {FONT_DATA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
