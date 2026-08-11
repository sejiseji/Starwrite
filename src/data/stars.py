from __future__ import annotations

import math

from astronomy.catalog import Star


def _hours_to_rad(hours: float) -> float:
    return math.radians(hours * 15.0)


def _deg_to_rad(degrees: float) -> float:
    return math.radians(degrees)


def star_from_hours(
    star_id: int,
    ra_hours: float,
    dec_degrees: float,
    magnitude: float,
    color_index: float | None,
) -> Star:
    return Star(star_id, _hours_to_rad(ra_hours), _deg_to_rad(dec_degrees), magnitude, color_index)


NAMED_STARS: tuple[Star, ...] = (
    star_from_hours(11767, 2.5303, 89.2641, 1.98, 0.60),  # Polaris
    star_from_hours(32349, 6.7525, -16.7161, -1.46, 0.00),  # Sirius
    star_from_hours(30438, 6.3992, -52.6957, -0.74, 0.16),  # Canopus
    star_from_hours(69673, 14.2610, 19.1824, -0.05, 1.23),  # Arcturus
    star_from_hours(91262, 18.6156, 38.7837, 0.03, 0.00),  # Vega
    star_from_hours(24608, 5.2782, 45.9980, 0.08, 0.80),  # Capella
    star_from_hours(24436, 5.2423, -8.2016, 0.13, -0.03),  # Rigel
    star_from_hours(37279, 7.6550, 5.2250, 0.40, 0.42),  # Procyon
    star_from_hours(7588, 1.6286, -57.2368, 0.46, -0.16),  # Achernar
    star_from_hours(27989, 5.9195, 7.4071, 0.50, 1.85),  # Betelgeuse
    star_from_hours(68702, 14.0637, -60.3730, 0.61, -0.23),  # Hadar
    star_from_hours(97649, 19.8464, 8.8683, 0.77, 0.22),  # Altair
    star_from_hours(60718, 12.4433, -63.0991, 0.77, -0.23),  # Acrux
    star_from_hours(21421, 4.5987, 16.5093, 0.85, 1.54),  # Aldebaran
    star_from_hours(65474, 13.4199, -11.1613, 0.98, -0.11),  # Spica
    star_from_hours(80763, 16.4901, -26.4319, 1.06, 1.83),  # Antares
    star_from_hours(37826, 7.5767, 31.8883, 1.14, 1.00),  # Pollux
    star_from_hours(25336, 5.4188, 6.3497, 1.64, -0.22),  # Bellatrix
    star_from_hours(27366, 5.7959, -9.6696, 2.06, -0.20),  # Saiph
    star_from_hours(26311, 5.6036, -1.2019, 1.69, -0.18),  # Alnilam
    star_from_hours(26727, 5.6793, -1.9426, 1.74, -0.20),  # Alnitak
    star_from_hours(25930, 5.5334, -0.2991, 2.23, -0.18),  # Mintaka
    star_from_hours(26207, 5.5856, 9.9342, 3.39, -0.18),  # Meissa
    star_from_hours(102098, 20.6905, 45.2803, 1.25, 0.09),  # Deneb
    star_from_hours(100453, 20.3705, 40.2567, 2.23, 0.67),  # Sadr
    star_from_hours(102488, 20.7702, 33.9703, 2.48, -0.03),  # Gienah
    star_from_hours(97165, 19.7494, 45.1308, 2.87, -0.03),  # Delta Cyg
    star_from_hours(95947, 19.5120, 27.9597, 3.08, 1.13),  # Albireo
    star_from_hours(746, 0.1529, 59.1498, 2.27, 0.38),  # Caph
    star_from_hours(3179, 0.6751, 56.5373, 2.24, 1.17),  # Schedar
    star_from_hours(4427, 0.9451, 60.7167, 2.15, -0.15),  # Gamma Cas
    star_from_hours(6686, 1.4302, 60.2353, 2.68, -0.13),  # Ruchbah
    star_from_hours(8886, 1.9066, 63.6700, 3.35, -0.08),  # Segin
    star_from_hours(54061, 11.0621, 61.7510, 1.79, 1.07),  # Dubhe
    star_from_hours(53910, 11.0307, 56.3824, 2.37, 0.00),  # Merak
    star_from_hours(58001, 11.8972, 53.6948, 2.44, 0.08),  # Phecda
    star_from_hours(59774, 12.2569, 57.0326, 3.31, 0.08),  # Megrez
    star_from_hours(62956, 12.9005, 55.9598, 1.76, -0.02),  # Alioth
    star_from_hours(65378, 13.3987, 54.9254, 2.23, 0.06),  # Mizar
    star_from_hours(67301, 13.7923, 49.3133, 1.86, -0.19),  # Alkaid
    star_from_hours(85927, 17.5601, -37.1038, 1.62, -0.23),  # Shaula
    star_from_hours(86228, 17.6220, -42.9978, 1.86, 1.50),  # Sargas
    star_from_hours(78401, 16.0056, -22.6217, 2.32, -0.07),  # Dschubba
    star_from_hours(78820, 16.0906, -19.8055, 2.56, -0.08),  # Acrab
    star_from_hours(80112, 16.3532, -25.5928, 2.89, -0.05),  # Alniyat
    star_from_hours(85696, 17.5127, -37.2958, 2.70, -0.22),  # Lesath
)

STAR_NAMES: dict[int, str] = {
    11767: "Polaris",
    32349: "Sirius",
    30438: "Canopus",
    69673: "Arcturus",
    91262: "Vega",
    24608: "Capella",
    24436: "Rigel",
    37279: "Procyon",
    7588: "Achernar",
    27989: "Betelgeuse",
    68702: "Hadar",
    97649: "Altair",
    60718: "Acrux",
    21421: "Aldebaran",
    65474: "Spica",
    80763: "Antares",
    37826: "Pollux",
    25336: "Bellatrix",
    27366: "Saiph",
    26311: "Alnilam",
    26727: "Alnitak",
    25930: "Mintaka",
    26207: "Meissa",
    102098: "Deneb",
    100453: "Sadr",
    102488: "Gienah",
    97165: "Delta Cygni",
    95947: "Albireo",
    746: "Caph",
    3179: "Schedar",
    4427: "Gamma Cassiopeiae",
    6686: "Ruchbah",
    8886: "Segin",
    54061: "Dubhe",
    53910: "Merak",
    58001: "Phecda",
    59774: "Megrez",
    62956: "Alioth",
    65378: "Mizar",
    67301: "Alkaid",
    85927: "Shaula",
    86228: "Sargas",
    78401: "Dschubba",
    78820: "Acrab",
    80112: "Alniyat",
    85696: "Lesath",
}


def _frac(value: float) -> float:
    return value - math.floor(value)


def synthetic_stars(count: int = 1800) -> tuple[Star, ...]:
    stars: list[Star] = []
    for i in range(count):
        a = _frac(math.sin((i + 1) * 12.9898) * 43758.5453)
        b = _frac(math.sin((i + 1) * 78.233) * 24634.6345)
        c = _frac(math.sin((i + 1) * 37.719) * 9617.517)
        ra = math.tau * a
        dec = math.asin(2.0 * b - 1.0)
        magnitude = 3.7 + 2.4 * c
        color_index = -0.2 + 1.8 * _frac(a + b + c)
        stars.append(Star(1_000_000 + i, ra, dec, magnitude, color_index))
    return tuple(stars)


STARS: tuple[Star, ...] = NAMED_STARS + synthetic_stars()
STARS_BY_ID: dict[int, Star] = {star.id: star for star in STARS}
