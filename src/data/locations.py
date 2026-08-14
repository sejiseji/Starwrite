from __future__ import annotations

LOCATION_COUNTRIES: tuple[dict, ...] = (
    {
        "id": "JP",
        "name_en": "Japan",
        "name_ja": "日本",
        "cities": (
            {"id": "tokyo", "name_en": "Tokyo", "name_ja": "東京", "lat": 35.7, "lon": 139.7},
            {"id": "sapporo", "name_en": "Sapporo", "name_ja": "札幌", "lat": 43.1, "lon": 141.4},
            {"id": "naha", "name_en": "Naha", "name_ja": "那覇", "lat": 26.2, "lon": 127.7},
        ),
    },
    {
        "id": "US",
        "name_en": "United States",
        "name_ja": "アメリカ",
        "cities": (
            {"id": "new_york", "name_en": "New York", "name_ja": "ニューヨーク", "lat": 40.7, "lon": -74.0},
            {"id": "los_angeles", "name_en": "Los Angeles", "name_ja": "ロサンゼルス", "lat": 34.1, "lon": -118.2},
            {"id": "honolulu", "name_en": "Honolulu", "name_ja": "ホノルル", "lat": 21.3, "lon": -157.9},
        ),
    },
    {
        "id": "GB",
        "name_en": "United Kingdom",
        "name_ja": "イギリス",
        "cities": (
            {"id": "london", "name_en": "London", "name_ja": "ロンドン", "lat": 51.5, "lon": -0.1},
            {"id": "edinburgh", "name_en": "Edinburgh", "name_ja": "エディンバラ", "lat": 55.9, "lon": -3.2},
        ),
    },
    {
        "id": "FI",
        "name_en": "Finland",
        "name_ja": "フィンランド",
        "cities": (
            {"id": "helsinki", "name_en": "Helsinki", "name_ja": "ヘルシンキ", "lat": 60.2, "lon": 24.9},
            {"id": "tampere", "name_en": "Tampere", "name_ja": "タンペレ", "lat": 61.5, "lon": 23.8},
        ),
    },
    {
        "id": "AU",
        "name_en": "Australia",
        "name_ja": "オーストラリア",
        "cities": (
            {"id": "sydney", "name_en": "Sydney", "name_ja": "シドニー", "lat": -33.9, "lon": 151.2},
            {"id": "melbourne", "name_en": "Melbourne", "name_ja": "メルボルン", "lat": -37.8, "lon": 145.0},
            {"id": "perth", "name_en": "Perth", "name_ja": "パース", "lat": -31.9, "lon": 115.9},
        ),
    },
    {
        "id": "NZ",
        "name_en": "New Zealand",
        "name_ja": "ニュージーランド",
        "cities": (
            {"id": "auckland", "name_en": "Auckland", "name_ja": "オークランド", "lat": -36.9, "lon": 174.8},
            {"id": "wellington", "name_en": "Wellington", "name_ja": "ウェリントン", "lat": -41.3, "lon": 174.8},
        ),
    },
    {
        "id": "BR",
        "name_en": "Brazil",
        "name_ja": "ブラジル",
        "cities": (
            {"id": "sao_paulo", "name_en": "Sao Paulo", "name_ja": "サンパウロ", "lat": -23.6, "lon": -46.6},
            {"id": "rio", "name_en": "Rio de Janeiro", "name_ja": "リオデジャネイロ", "lat": -22.9, "lon": -43.2},
        ),
    },
    {
        "id": "ZA",
        "name_en": "South Africa",
        "name_ja": "南アフリカ",
        "cities": (
            {"id": "cape_town", "name_en": "Cape Town", "name_ja": "ケープタウン", "lat": -33.9, "lon": 18.4},
            {"id": "johannesburg", "name_en": "Johannesburg", "name_ja": "ヨハネスブルグ", "lat": -26.2, "lon": 28.0},
        ),
    },
    {
        "id": "CL",
        "name_en": "Chile",
        "name_ja": "チリ",
        "cities": (
            {"id": "santiago", "name_en": "Santiago", "name_ja": "サンティアゴ", "lat": -33.4, "lon": -70.7},
            {"id": "punta_arenas", "name_en": "Punta Arenas", "name_ja": "プンタアレナス", "lat": -53.2, "lon": -70.9},
        ),
    },
    {
        "id": "EG",
        "name_en": "Egypt",
        "name_ja": "エジプト",
        "cities": (
            {"id": "cairo", "name_en": "Cairo", "name_ja": "カイロ", "lat": 30.0, "lon": 31.2},
            {"id": "aswan", "name_en": "Aswan", "name_ja": "アスワン", "lat": 24.1, "lon": 32.9},
        ),
    },
)


def location_label(item: dict, language: str) -> str:
    return str(item["name_ja"] if language == "ja" else item["name_en"])
