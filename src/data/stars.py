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
    star_from_hours(49669, 10.1395, 11.9672, 1.35, -0.11),  # Regulus
    star_from_hours(57632, 11.8177, 14.5721, 2.14, 0.09),  # Denebola
    star_from_hours(50583, 10.3330, 19.8415, 2.28, 1.15),  # Algieba
    star_from_hours(54872, 11.2351, 20.5237, 2.56, 0.12),  # Zosma
    star_from_hours(54879, 11.2373, 15.4296, 3.33, 0.31),  # Chertan
    star_from_hours(25428, 5.4382, 28.6075, 1.65, -0.13),  # Elnath
    star_from_hours(17702, 3.7914, 24.1051, 2.87, -0.09),  # Alcyone
    star_from_hours(20889, 4.3823, 17.5425, 3.40, 0.98),  # Hyadum I
    star_from_hours(36850, 7.5766, 31.8886, 1.58, 0.03),  # Castor
    star_from_hours(31681, 6.6285, 16.3993, 1.93, 0.00),  # Alhena
    star_from_hours(35550, 7.3354, 21.9823, 3.53, 0.35),  # Wasat
    star_from_hours(32246, 6.7322, 25.1311, 3.06, 1.40),  # Mebsuta
    star_from_hours(34088, 7.0685, 20.5703, 4.01, 1.55),  # Mekbuda
    star_from_hours(30324, 6.3783, -17.9559, 1.98, -0.23),  # Mirzam
    star_from_hours(34444, 7.1399, -26.3932, 1.83, 0.68),  # Wezen
    star_from_hours(33579, 6.9771, -28.9721, 1.50, -0.21),  # Adhara
    star_from_hours(35904, 7.4016, -29.3031, 2.45, -0.07),  # Aludra
    star_from_hours(92420, 18.8347, 33.3627, 3.52, 0.00),  # Sheliak
    star_from_hours(93194, 18.9824, 32.6896, 3.24, -0.12),  # Sulafat
    star_from_hours(92791, 18.9084, 36.8986, 4.30, 0.08),  # Delta Lyrae
    star_from_hours(97278, 19.7710, 10.6133, 2.72, 1.51),  # Tarazed
    star_from_hours(98036, 19.9219, 6.4068, 3.71, 0.86),  # Alshain
    star_from_hours(95501, 19.4249, 3.1148, 3.36, -0.08),  # Deneb el Okab
    star_from_hours(72105, 14.7498, 27.0742, 2.37, 1.27),  # Izar
    star_from_hours(73555, 15.0324, 40.3906, 3.49, 1.10),  # Nekkar
    star_from_hours(71075, 14.5346, 38.3079, 3.03, 0.19),  # Seginus
    star_from_hours(67927, 13.9114, 18.3977, 2.68, 0.59),  # Muphrid
    star_from_hours(62434, 12.7953, -59.6888, 1.25, -0.23),  # Mimosa
    star_from_hours(61084, 12.5194, -57.1132, 1.63, 1.59),  # Gacrux
    star_from_hours(59747, 12.2524, -58.7489, 2.79, -0.19),  # Delta Crucis
    star_from_hours(71683, 14.6601, -60.8351, -0.27, 0.71),  # Rigil Kentaurus
    star_from_hours(68933, 14.1114, -36.3700, 2.06, 1.01),  # Menkent
    star_from_hours(68002, 13.9257, -47.2884, 2.30, -0.20),  # Theta Centauri
    star_from_hours(45238, 9.2200, -69.7172, 1.67, 0.20),  # Miaplacidus
    star_from_hours(41037, 8.3752, -59.5095, 1.86, 1.16),  # Avior
    star_from_hours(45556, 9.2848, -59.2752, 2.21, 1.20),  # Aspidiske
    star_from_hours(61941, 12.6943, -1.4494, 2.74, 0.36),  # Porrima
    star_from_hours(63608, 13.0363, 10.9591, 2.85, 0.94),  # Vindemiatrix
    star_from_hours(66249, 13.5782, -0.5958, 3.38, 0.37),  # Heze
    star_from_hours(57757, 11.8449, 1.7647, 3.59, 0.57),  # Zavijava
    star_from_hours(113963, 23.0793, 15.2053, 2.49, -0.04),  # Markab
    star_from_hours(113881, 23.0629, 28.0828, 2.42, 1.65),  # Scheat
    star_from_hours(1067, 0.2206, 15.1836, 2.83, -0.19),  # Algenib
    star_from_hours(107315, 21.7364, 9.8750, 2.39, 1.52),  # Enif
    star_from_hours(677, 0.1398, 29.0904, 2.06, -0.04),  # Alpheratz
    star_from_hours(5447, 1.1622, 35.6206, 2.07, 1.58),  # Mirach
    star_from_hours(9640, 2.0649, 42.3297, 2.10, 1.37),  # Almach
    star_from_hours(3092, 0.6555, 30.8610, 3.27, 0.78),  # Delta Andromedae
    star_from_hours(15863, 3.4054, 49.8612, 1.79, 0.48),  # Mirfak
    star_from_hours(14576, 3.1361, 40.9556, 2.09, -0.05),  # Algol
    star_from_hours(17448, 3.7387, 32.2883, 3.84, 0.12),  # Atik
    star_from_hours(14328, 3.0799, 53.5064, 2.93, 0.72),  # Gamma Persei
    star_from_hours(28360, 5.9921, 44.9474, 1.90, 0.03),  # Menkalinan
    star_from_hours(28380, 5.9954, 37.2126, 2.62, 0.08),  # Mahasim
    star_from_hours(23015, 4.9499, 33.1661, 2.69, 1.49),  # Hassaleh
    star_from_hours(23416, 5.0328, 43.8233, 3.03, 0.54),  # Almaaz
    star_from_hours(87833, 17.9434, 51.4889, 2.24, 1.52),  # Eltanin
    star_from_hours(85670, 17.5072, 52.3014, 2.79, 0.98),  # Rastaban
    star_from_hours(68756, 14.0732, 64.3759, 3.65, -0.05),  # Thuban
    star_from_hours(75458, 15.4155, 58.9661, 3.29, 1.16),  # Edasich
    star_from_hours(105199, 21.3096, 62.5856, 2.45, 0.26),  # Alderamin
    star_from_hours(106032, 21.4777, 70.5607, 3.23, 1.10),  # Alfirk
    star_from_hours(116727, 23.6558, 77.6323, 3.21, 1.03),  # Errai
    star_from_hours(109492, 22.1809, 58.2012, 3.35, 1.57),  # Zeta Cephei
    star_from_hours(109074, 22.0964, -0.3199, 2.94, 0.97),  # Sadalmelik
    star_from_hours(106278, 21.5260, -5.5712, 2.87, 0.83),  # Sadalsuud
    star_from_hours(113136, 22.9108, -15.8208, 3.27, 0.04),  # Skat
    star_from_hours(110395, 22.3609, -1.3873, 3.84, -0.04),  # Sadachbia
    star_from_hours(102618, 20.7946, -9.4958, 3.77, 0.03),  # Albali
    star_from_hours(110003, 22.2806, -7.7833, 4.17, 0.98),  # Ancha
    star_from_hours(107556, 21.7840, -16.1273, 2.85, 0.30),  # Deneb Algedi
    star_from_hours(100345, 20.3502, -14.7814, 3.05, 0.79),  # Dabih
    star_from_hours(100064, 20.3009, -12.5449, 3.58, 1.58),  # Algedi
    star_from_hours(106985, 21.6682, -16.6623, 3.69, 0.31),  # Nashira
    star_from_hours(104139, 21.0991, -17.2329, 4.13, 1.53),  # Psi Capricorni
    star_from_hours(72607, 14.8451, 74.1555, 2.08, 1.47),  # Kochab
    star_from_hours(75097, 15.3455, 71.8340, 3.05, 0.04),  # Pherkad
    star_from_hours(85822, 17.5369, 86.5863, 4.36, 0.28),  # Yildun
    star_from_hours(82080, 16.7662, 82.0373, 4.23, 0.90),  # Epsilon Ursae Minoris
    star_from_hours(77055, 15.7343, 77.7945, 4.32, 0.00),  # Zeta Ursae Minoris
    star_from_hours(79822, 16.2918, 75.7547, 4.95, 0.32),  # Eta Ursae Minoris
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
    49669: "Regulus",
    57632: "Denebola",
    50583: "Algieba",
    54872: "Zosma",
    54879: "Chertan",
    25428: "Elnath",
    17702: "Alcyone",
    20889: "Hyadum I",
    36850: "Castor",
    31681: "Alhena",
    35550: "Wasat",
    32246: "Mebsuta",
    34088: "Mekbuda",
    30324: "Mirzam",
    34444: "Wezen",
    33579: "Adhara",
    35904: "Aludra",
    92420: "Sheliak",
    93194: "Sulafat",
    92791: "Delta Lyrae",
    97278: "Tarazed",
    98036: "Alshain",
    95501: "Deneb el Okab",
    72105: "Izar",
    73555: "Nekkar",
    71075: "Seginus",
    67927: "Muphrid",
    62434: "Mimosa",
    61084: "Gacrux",
    59747: "Delta Crucis",
    71683: "Rigil Kentaurus",
    68933: "Menkent",
    68002: "Theta Centauri",
    45238: "Miaplacidus",
    41037: "Avior",
    45556: "Aspidiske",
    61941: "Porrima",
    63608: "Vindemiatrix",
    66249: "Heze",
    57757: "Zavijava",
    113963: "Markab",
    113881: "Scheat",
    1067: "Algenib",
    107315: "Enif",
    677: "Alpheratz",
    5447: "Mirach",
    9640: "Almach",
    3092: "Delta Andromedae",
    15863: "Mirfak",
    14576: "Algol",
    17448: "Atik",
    14328: "Gamma Persei",
    28360: "Menkalinan",
    28380: "Mahasim",
    23015: "Hassaleh",
    23416: "Almaaz",
    87833: "Eltanin",
    85670: "Rastaban",
    68756: "Thuban",
    75458: "Edasich",
    105199: "Alderamin",
    106032: "Alfirk",
    116727: "Errai",
    109492: "Zeta Cephei",
    109074: "Sadalmelik",
    106278: "Sadalsuud",
    113136: "Skat",
    110395: "Sadachbia",
    102618: "Albali",
    110003: "Ancha",
    107556: "Deneb Algedi",
    100345: "Dabih",
    100064: "Algedi",
    106985: "Nashira",
    104139: "Psi Capricorni",
    72607: "Kochab",
    75097: "Pherkad",
    85822: "Yildun",
    82080: "Epsilon Ursae Minoris",
    77055: "Zeta Ursae Minoris",
    79822: "Eta Ursae Minoris",
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
