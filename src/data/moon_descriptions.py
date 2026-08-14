from __future__ import annotations

MOON_DESCRIPTIONS: dict[str, str] = {
    "ja": "地球を巡り、夜空と潮の満ち引きに寄り添う天体。",
    "en": "Earth's moon shapes tides and lights the night.",
}

MOON_PHASE_DESCRIPTIONS: dict[str, dict[str, str]] = {
    "new": {
        "name_ja": "新月",
        "name_en": "New Moon",
        "description_ja": "太陽と同じ方向にあり、ほとんど姿を見せない。",
        "description_en": "Near the Sun, it is almost hidden from view.",
        "title_ja": "月 （新月）",
        "title_en": "MOON (NEW MOON)",
    },
    "waxing_crescent": {
        "name_ja": "三日月",
        "name_en": "Waxing Crescent",
        "description_ja": "日没後の西空に、細い光の弧が現れる。",
        "description_en": "A slim arc appears low in the western dusk.",
        "title_ja": "月 （三日月）",
        "title_en": "MOON (WAXING CRESCENT)",
    },
    "first_quarter": {
        "name_ja": "上弦の月",
        "name_en": "First Quarter",
        "description_ja": "半月に見え、夕方から夜半まで空に残る。",
        "description_en": "Half lit, it stays up from dusk to midnight.",
        "title_ja": "月 （上弦の月）",
        "title_en": "MOON (FIRST QUARTER)",
    },
    "waxing_gibbous": {
        "name_ja": "満ちていく月",
        "name_en": "Waxing Gibbous",
        "description_ja": "満月へ向かい、明るい面が日ごとに広がる。",
        "description_en": "Its bright face grows wider toward full moon.",
        "title_ja": "月 （満ちていく月）",
        "title_en": "MOON (WAXING GIBBOUS)",
    },
    "full": {
        "name_ja": "満月",
        "name_en": "Full Moon",
        "description_ja": "見える面が照らされ、日暮れから朝まで空を渡る。",
        "description_en": "Fully lit, it crosses the sky all night.",
        "title_ja": "月 （満月）",
        "title_en": "MOON (FULL MOON)",
    },
    "waning_gibbous": {
        "name_ja": "欠けていく月",
        "name_en": "Waning Gibbous",
        "description_ja": "満月を過ぎ、明るい面が少しずつ狭まる。",
        "description_en": "After full moon, its lit face slowly narrows.",
        "title_ja": "月 （欠けていく月）",
        "title_en": "MOON (WANING GIBBOUS)",
    },
    "last_quarter": {
        "name_ja": "下弦の月",
        "name_en": "Last Quarter",
        "description_ja": "半月に見え、夜半から朝の空に現れる。",
        "description_en": "Half lit, it climbs from midnight into dawn.",
        "title_ja": "月 （下弦の月）",
        "title_en": "MOON (LAST QUARTER)",
    },
    "waning_crescent": {
        "name_ja": "有明の月",
        "name_en": "Waning Crescent",
        "description_ja": "夜明け前の東空に、細い光を残して浮かぶ。",
        "description_en": "A thin arc lingers in the eastern dawn sky.",
        "title_ja": "月 （有明の月）",
        "title_en": "MOON (WANING CRESCENT)",
    },
}


def moon_description(language: str) -> str:
    return MOON_DESCRIPTIONS.get(language, MOON_DESCRIPTIONS["en"])


def moon_phase_title(phase_key: str, language: str) -> str:
    phase = MOON_PHASE_DESCRIPTIONS.get(phase_key)
    if phase is None:
        return "月 （月相）" if language == "ja" else "MOON (PHASE)"
    key = "title_ja" if language == "ja" else "title_en"
    return phase[key]


def moon_phase_description(phase_key: str, language: str) -> str:
    phase = MOON_PHASE_DESCRIPTIONS.get(phase_key)
    if phase is None:
        return "月の満ち欠けを表示中。" if language == "ja" else "Showing the Moon's current phase."
    key = "description_ja" if language == "ja" else "description_en"
    return phase[key]
