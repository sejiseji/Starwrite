from __future__ import annotations

from typing import Literal

from astronomy.catalog import Constellation
from astronomy.events import MeteorShowerEvent
from data.sky_features import Asterism, SkyPath

Language = Literal["en", "ja"]

CONSTELLATION_NAMES_JA: dict[str, str] = {
    "ORI": "オリオン座",
    "CYG": "はくちょう座",
    "CAS": "カシオペヤ座",
    "UMA": "おおぐま座",
    "SCO": "さそり座",
    "LEO": "しし座",
    "TAU": "おうし座",
    "GEM": "ふたご座",
    "CMA": "おおいぬ座",
    "LYR": "こと座",
    "AQL": "わし座",
    "BOO": "うしかい座",
    "CRU": "みなみじゅうじ座",
    "CEN": "ケンタウルス座",
    "CAR": "りゅうこつ座",
    "VIR": "おとめ座",
    "PEG": "ペガスス座",
    "AND": "アンドロメダ座",
    "PER": "ペルセウス座",
    "AUR": "ぎょしゃ座",
    "DRA": "りゅう座",
    "CEP": "ケフェウス座",
    "AQR": "みずがめ座",
    "CAP": "やぎ座",
    "UMI": "こぐま座",
}

METEOR_EVENT_NAMES_JA: dict[str, str] = {
    "QUA": "しぶんぎ座流星群",
    "LYR": "こと座流星群",
    "ETA": "みずがめ座エータ流星群",
    "SDA": "みずがめ座デルタ南流星群",
    "CAP": "やぎ座アルファ流星群",
    "PER": "ペルセウス座流星群",
    "ORI": "オリオン座流星群",
    "STA": "おうし座南流星群",
    "NTA": "おうし座北流星群",
    "LEO": "しし座流星群",
    "GEM": "ふたご座流星群",
    "URS": "こぐま座流星群",
}

STAR_NAMES_JA: dict[int, str] = {
    11767: "ポラリス",
    32349: "シリウス",
    30438: "カノープス",
    69673: "アークトゥルス",
    91262: "ベガ",
    24608: "カペラ",
    24436: "リゲル",
    37279: "プロキオン",
    7588: "アケルナル",
    27989: "ベテルギウス",
    68702: "ハダル",
    97649: "アルタイル",
    60718: "アクルックス",
    21421: "アルデバラン",
    65474: "スピカ",
    80763: "アンタレス",
    37826: "ポルックス",
    25336: "ベラトリックス",
    27366: "サイフ",
    26311: "アルニラム",
    26727: "アルニタク",
    25930: "ミンタカ",
    26207: "メイサ",
    102098: "デネブ",
    100453: "サドル",
    102488: "ギェナー",
    97165: "デルタ・キグニ",
    95947: "アルビレオ",
    746: "カフ",
    3179: "シェダル",
    4427: "ガンマ・カシオペヤ",
    6686: "ルクバー",
    8886: "セギン",
    54061: "ドゥーベ",
    53910: "メラク",
    58001: "フェクダ",
    59774: "メグレズ",
    62956: "アリオト",
    65378: "ミザール",
    67301: "アルカイド",
    85927: "シャウラ",
    86228: "サルガス",
    78401: "ジュバ",
    78820: "アクラブ",
    80112: "アルニヤト",
    85696: "レサト",
    49669: "レグルス",
    57632: "デネボラ",
    50583: "アルギエバ",
    54872: "ゾスマ",
    54879: "チェルタン",
    25428: "エルナト",
    17702: "アルキオネ",
    20889: "ヒアドゥムI",
    36850: "カストル",
    31681: "アルヘナ",
    35550: "ワサト",
    32246: "メブスタ",
    34088: "メクブダ",
    30324: "ミルザム",
    34444: "ウェゼン",
    33579: "アダーラ",
    35904: "アルドラ",
    92420: "シェリアク",
    93194: "スラファト",
    92791: "デルタ・リラ",
    97278: "タラゼド",
    98036: "アルシャイン",
    95501: "デネブ・エル・オカブ",
    72105: "イザール",
    73555: "ネッカル",
    71075: "セギヌス",
    67927: "ムフリッド",
    62434: "ミモザ",
    61084: "ガクルックス",
    59747: "デルタ・クルキス",
    71683: "リギル・ケンタウルス",
    68933: "メンケント",
    68002: "シータ・ケンタウリ",
    45238: "ミアプラキドゥス",
    41037: "アビオル",
    45556: "アスピディスケ",
    61941: "ポリマ",
    63608: "ヴィンデミアトリックス",
    66249: "ヘゼ",
    57757: "ザヴィヤヴァ",
    113963: "マルカブ",
    113881: "シェアト",
    1067: "アルゲニブ",
    107315: "エニフ",
    677: "アルフェラッツ",
    5447: "ミラク",
    9640: "アルマク",
    3092: "デルタ・アンドロメダ",
    15863: "ミルファク",
    14576: "アルゴル",
    17448: "アティク",
    14328: "ガンマ・ペルセイ",
    28360: "メンカリナン",
    28380: "マハシム",
    23015: "ハッサレ",
    23416: "アルマーズ",
    87833: "エルタニン",
    85670: "ラスタバン",
    68756: "トゥバン",
    75458: "エダシク",
    105199: "アルデラミン",
    106032: "アルフィルク",
    116727: "エライ",
    109492: "ゼータ・ケフェイ",
    109074: "サダルメリク",
    106278: "サダルスウド",
    113136: "スカト",
    110395: "サダクビア",
    102618: "アルバリ",
    110003: "アンカ",
    107556: "デネブ・アルゲディ",
    100345: "ダビー",
    100064: "アルゲディ",
    106985: "ナシラ",
    104139: "プサイ・カプリコルニ",
    72607: "コカブ",
    75097: "フェルカド",
    85822: "イルドゥン",
    82080: "イプシロン・こぐま",
    77055: "ゼータ・こぐま",
    79822: "イータ・こぐま",
}

SKY_FEATURE_NAMES_JA: dict[str, str] = {
    "SUMMER_TRIANGLE": "夏の大三角",
    "WINTER_TRIANGLE": "冬の大三角",
    "BIG_DIPPER": "北斗七星",
    "SPRING_ARC": "春の大曲線",
    "MILKY_WAY": "天の川",
}


def normalize_language(value: object) -> Language:
    return "ja" if value == "ja" else "en"


def next_language(language: Language) -> Language:
    return "ja" if language == "en" else "en"


def constellation_name(constellation: Constellation, language: Language) -> str:
    if language == "ja":
        return CONSTELLATION_NAMES_JA.get(constellation.id, constellation.name)
    return constellation.name


def meteor_event_name(event: MeteorShowerEvent, language: Language) -> str:
    if language == "ja":
        return METEOR_EVENT_NAMES_JA.get(event.id.split("-", 1)[0], event.name)
    return event.name


def star_name(star_id: int, english_name: str, language: Language) -> str:
    if language == "ja":
        return STAR_NAMES_JA.get(star_id, english_name)
    return english_name


def sky_feature_name(feature: Asterism | SkyPath, language: Language) -> str:
    if language == "ja":
        return SKY_FEATURE_NAMES_JA.get(feature.id, feature.name)
    return feature.name
