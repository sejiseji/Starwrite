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
    star_from_hours(36188, 7.4525, 8.2893, 2.89, -0.08),  # Gomeisa
    star_from_hours(23875, 5.1308, -5.0864, 2.79, 0.55),  # Cursa
    star_from_hours(18543, 3.9672, -13.5085, 2.97, 1.59),  # Zaurak
    star_from_hours(13847, 2.9710, -40.3047, 3.24, 0.13),  # Acamar
    star_from_hours(3419, 0.7265, -17.9866, 2.04, 1.02),  # Diphda
    star_from_hours(14135, 3.0379, 4.0897, 2.54, 1.63),  # Menkar
    star_from_hours(10826, 2.3224, -2.9776, 3.00, 1.60),  # Mira
    star_from_hours(12706, 2.7217, -10.6780, 3.73, 1.05),  # Baten Kaitos
    star_from_hours(9487, 2.0341, 2.7638, 3.82, 0.04),  # Alrescha
    star_from_hours(7097, 1.5247, 15.3458, 4.27, 0.95),  # Kullat Nunu
    star_from_hours(8198, 1.7566, 9.1577, 4.27, 1.00),  # Torcular
    star_from_hours(118268, 23.9885, 6.8633, 4.01, 0.44),  # Omega Piscium
    star_from_hours(9884, 2.1195, 23.4624, 2.00, 1.15),  # Hamal
    star_from_hours(8903, 1.9107, 20.8080, 2.64, -0.10),  # Sheratan
    star_from_hours(8832, 1.8922, 19.2939, 3.88, 0.03),  # Mesarthim
    star_from_hours(101958, 20.6606, 15.9119, 3.77, -0.02),  # Sualocin
    star_from_hours(101769, 20.6258, 14.5951, 3.64, 0.04),  # Rotanev
    star_from_hours(102531, 20.7775, 16.1243, 4.27, 1.02),  # Gamma Delphini
    star_from_hours(96837, 19.6683, 18.0139, 4.39, 1.43),  # Sham
    star_from_hours(97365, 19.7898, 18.5343, 3.82, 1.01),  # Delta Sagittae
    star_from_hours(98337, 19.9825, 19.4921, 3.51, 1.37),  # Gamma Sagittae
    star_from_hours(95771, 19.4784, 24.6649, 4.44, 1.50),  # Anser
    star_from_hours(98543, 20.0153, 27.7536, 4.52, 0.95),  # 23 Vulpeculae
    star_from_hours(99853, 20.2710, 27.8142, 4.57, 1.10),  # 31 Vulpeculae
    star_from_hours(90185, 18.4029, -34.3846, 1.79, -0.11),  # Kaus Australis
    star_from_hours(92855, 18.9211, -26.2967, 2.05, -0.13),  # Nunki
    star_from_hours(93506, 19.0435, -29.8801, 2.60, 0.04),  # Ascella
    star_from_hours(89931, 18.3499, -29.8281, 2.72, 1.05),  # Kaus Media
    star_from_hours(90496, 18.4662, -25.4217, 2.82, 1.00),  # Kaus Borealis
    star_from_hours(88635, 18.0968, -30.4241, 2.98, 1.52),  # Alnasl
    star_from_hours(86032, 17.5822, 12.5600, 2.08, 0.15),  # Rasalhague
    star_from_hours(86742, 17.7245, 4.5673, 2.76, 1.16),  # Cebalrai
    star_from_hours(79593, 16.2391, -3.6943, 2.73, 1.58),  # Yed Prior
    star_from_hours(84012, 17.1729, -15.7249, 2.43, 0.15),  # Sabik
    star_from_hours(80816, 16.5037, 21.4896, 2.77, 0.95),  # Kornephoros
    star_from_hours(84345, 17.2441, 14.3903, 3.35, 1.45),  # Rasalgethi
    star_from_hours(80170, 16.3290, 19.1530, 3.13, 0.08),  # Sarin
    star_from_hours(84379, 17.2505, 24.8392, 4.41, 0.55),  # Maasym
    star_from_hours(76267, 15.5781, 26.7147, 2.22, 0.03),  # Alphecca
    star_from_hours(75695, 15.4638, 29.1057, 3.68, 0.53),  # Nusakan
    star_from_hours(76952, 15.7124, 26.2956, 3.84, 0.74),  # Gamma Coronae Borealis
    star_from_hours(77512, 15.8266, 26.0685, 4.63, 1.00),  # Delta Coronae Borealis
    star_from_hours(72622, 14.8479, -16.0418, 2.75, 0.14),  # Zubenelgenubi
    star_from_hours(74785, 15.2834, -9.3831, 2.61, -0.10),  # Zubeneschamali
    star_from_hours(73714, 15.0678, -25.2819, 3.25, 1.70),  # Brachium
    star_from_hours(75177, 15.3089, -28.1351, 3.60, 1.40),  # Upsilon Librae
    star_from_hours(59803, 12.2634, -17.5419, 2.59, -0.08),  # Gienah Corvi
    star_from_hours(61359, 12.5731, -23.3968, 2.65, 1.33),  # Kraz
    star_from_hours(60965, 12.4977, -16.5154, 2.95, 0.13),  # Algorab
    star_from_hours(59316, 12.1687, -22.6198, 3.02, 1.33),  # Minkar
    star_from_hours(46390, 9.4598, -8.6586, 1.99, 1.44),  # Alphard
    star_from_hours(64962, 13.3153, -23.1715, 2.99, 0.92),  # Gamma Hydrae
    star_from_hours(43813, 8.9232, 5.9456, 3.10, 1.00),  # Zeta Hydrae
    star_from_hours(52943, 10.8271, -16.1937, 3.11, 1.24),  # Nu Hydrae
    star_from_hours(30867, 6.4803, -7.0329, 3.76, 0.00),  # Beta Monocerotis
    star_from_hours(30419, 6.3961, 4.5929, 4.39, 1.10),  # Epsilon Monocerotis
    star_from_hours(34769, 7.1977, -0.4928, 4.15, -0.10),  # Delta Monocerotis
    star_from_hours(39429, 8.0597, -40.0031, 2.21, -0.27),  # Naos
    star_from_hours(39757, 8.1257, -24.3043, 2.83, 1.25),  # Tureis
    star_from_hours(35264, 7.2857, -37.0975, 3.25, 1.20),  # Azmidi
    star_from_hours(44816, 9.1333, -43.4326, 2.21, 1.70),  # Suhail
    star_from_hours(39953, 8.1589, -47.3366, 1.75, -0.22),  # Regor
    star_from_hours(45941, 9.3686, -55.0107, 1.96, 0.00),  # Alsephina
    star_from_hours(42913, 8.7451, -54.7088, 2.47, -0.18),  # Markeb Velae
    star_from_hours(71860, 14.6988, -47.3882, 2.30, -0.20),  # Men
    star_from_hours(73273, 14.9755, -43.1339, 2.68, -0.20),  # Beta Lupi
    star_from_hours(76297, 15.5857, -41.1668, 2.78, -0.18),  # Gamma Lupi
    star_from_hours(75141, 15.3027, -40.6475, 3.22, -0.18),  # Delta Lupi
    star_from_hours(25985, 5.5455, -17.8223, 2.58, 0.21),  # Arneb
    star_from_hours(25606, 5.4708, -20.7594, 2.81, 0.81),  # Nihal
    star_from_hours(23685, 5.0910, -22.3710, 3.19, 1.46),  # Epsilon Leporis
    star_from_hours(24305, 5.2155, -16.2055, 3.29, -0.11),  # Mu Leporis
    star_from_hours(27288, 5.7826, -14.8219, 3.55, 0.10),  # Zeta Leporis
    star_from_hours(27072, 5.7411, -22.4484, 3.59, 0.48),  # Gamma Leporis
    star_from_hours(27654, 5.8554, -20.8791, 3.76, 0.98),  # Delta Leporis
    star_from_hours(40526, 8.2753, 9.1855, 3.53, 1.48),  # Tarf
    star_from_hours(42911, 8.7447, 18.1543, 3.94, 1.08),  # Asellus Australis
    star_from_hours(42806, 8.7214, 21.4685, 4.66, 0.01),  # Asellus Borealis
    star_from_hours(43103, 8.7783, 28.7599, 4.03, 1.01),  # Iota Cancri
    star_from_hours(44066, 8.9748, 11.8577, 4.26, 0.14),  # Acubens
    star_from_hours(40167, 8.2035, 17.6478, 4.67, 0.53),  # Tegmine
    star_from_hours(77070, 15.7378, 6.4256, 2.63, 1.17),  # Unukalhai
    star_from_hours(77233, 15.7698, 15.4218, 3.65, 0.07),  # Beta Serpentis
    star_from_hours(78072, 15.9409, 15.6616, 3.85, 0.48),  # Gamma Serpentis
    star_from_hours(76276, 15.5800, 10.5389, 3.80, 0.27),  # Delta Serpentis
    star_from_hours(77622, 15.8469, 4.4777, 3.71, 0.15),  # Epsilon Serpentis
    star_from_hours(89962, 18.3552, -2.8988, 3.23, 0.94),  # Eta Serpentis
    star_from_hours(86263, 17.6264, -15.3986, 3.54, 0.26),  # Xi Serpentis
    star_from_hours(63125, 12.9338, 38.3184, 2.89, -0.12),  # Cor Caroli
    star_from_hours(61317, 12.5624, 41.3575, 4.24, 0.59),  # Chara
    star_from_hours(66234, 13.5742, 49.0160, 4.68, 0.13),  # 24 Canum Venaticorum
    star_from_hours(60742, 12.4490, 28.2684, 4.35, 1.13),  # Gamma Comae Berenices
    star_from_hours(64394, 13.1979, 27.8782, 4.23, 0.57),  # Beta Comae Berenices
    star_from_hours(64241, 13.1665, 17.5294, 4.32, 0.46),  # Diadem
    star_from_hours(60202, 12.3453, 17.7929, 4.72, 1.01),  # 11 Comae Berenices
    star_from_hours(63355, 12.9821, 17.4094, 4.76, 1.57),  # 36 Comae Berenices
    star_from_hours(8796, 1.8847, 29.5788, 3.42, 0.49),  # Mothallah
    star_from_hours(10064, 2.1591, 34.9873, 3.00, 0.14),  # Beta Trianguli
    star_from_hours(10670, 2.2886, 33.8472, 4.03, 0.02),  # Gamma Trianguli
    star_from_hours(111169, 22.5215, 50.2825, 3.76, 0.03),  # Alpha Lacertae
    star_from_hours(110538, 22.3927, 52.2290, 4.42, 1.02),  # Beta Lacertae
    star_from_hours(111022, 22.4922, 47.7069, 4.34, 1.68),  # 5 Lacertae
    star_from_hours(111944, 22.6752, 44.2763, 4.50, 1.32),  # 11 Lacertae
    star_from_hours(109937, 22.2662, 37.7487, 4.14, 1.45),  # 1 Lacertae
    star_from_hours(33449, 6.9546, 58.4228, 4.35, 0.85),  # 15 Lyncis
    star_from_hours(36145, 7.4452, 49.2115, 4.61, 0.00),  # 21 Lyncis
    star_from_hours(41075, 8.3806, 43.1881, 4.25, 1.55),  # Alsciaukat
    star_from_hours(45688, 9.3141, 36.8026, 3.82, 0.07),  # 38 Lyncis
    star_from_hours(45860, 9.3509, 34.3926, 3.14, 1.55),  # Alpha Lyncis
    star_from_hours(100751, 20.4275, -56.7351, 1.94, -0.12),  # Peacock
    star_from_hours(102395, 20.7493, -66.2032, 3.42, 0.16),  # Beta Pavonis
    star_from_hours(99240, 20.1452, -66.1821, 3.55, 0.75),  # Delta Pavonis
    star_from_hours(105858, 21.4407, -65.3662, 4.21, 0.49),  # Gamma Pavonis
    star_from_hours(86929, 17.7622, -64.7239, 3.61, 1.16),  # Eta Pavonis
    star_from_hours(85792, 17.5307, -49.8761, 2.84, -0.14),  # Alpha Arae
    star_from_hours(85258, 17.4217, -55.5299, 2.84, 1.48),  # Beta Arae
    star_from_hours(83081, 16.9770, -55.9901, 3.12, 1.55),  # Zeta Arae
    star_from_hours(85267, 17.4232, -56.3777, 3.31, -0.15),  # Gamma Arae
    star_from_hours(85727, 17.5183, -60.6838, 3.60, -0.10),  # Delta Arae
    star_from_hours(88714, 18.1105, -50.0915, 3.65, -0.10),  # Theta Arae
    star_from_hours(82363, 16.8298, -59.0414, 3.77, 1.56),  # Eta Arae
    star_from_hours(109268, 22.1372, -46.9610, 1.73, -0.07),  # Alnair
    star_from_hours(112122, 22.7111, -46.8846, 2.07, 1.61),  # Tiaki
    star_from_hours(108085, 21.8988, -37.3649, 3.00, -0.08),  # Aldhanab
    star_from_hours(112623, 22.8092, -51.3169, 3.49, 0.08),  # Epsilon Gruis
    star_from_hours(114421, 23.1726, -45.2467, 3.88, 1.00),  # Iota Gruis
    star_from_hours(110997, 22.4878, -43.4956, 3.97, 1.02),  # Delta Gruis
    star_from_hours(2081, 0.4381, -42.3060, 2.40, 1.08),  # Ankaa
    star_from_hours(5165, 1.1014, -46.7184, 3.32, 0.89),  # Beta Phoenicis
    star_from_hours(6867, 1.4728, -43.3182, 3.41, 1.54),  # Gamma Phoenicis
    star_from_hours(765, 0.1568, -45.7474, 3.88, 1.01),  # Epsilon Phoenicis
    star_from_hours(7083, 1.5209, -49.0727, 3.93, 0.97),  # Delta Phoenicis
    star_from_hours(5348, 1.1397, -55.2458, 3.94, -0.12),  # Wurren
    star_from_hours(26634, 5.6608, -34.0741, 2.65, -0.12),  # Phact
    star_from_hours(27628, 5.8493, -35.7683, 3.12, 1.15),  # Wazn
    star_from_hours(30277, 6.3686, -33.4364, 3.85, 0.86),  # Delta Columbae
    star_from_hours(25859, 5.5202, -35.4705, 3.86, 1.13),  # Epsilon Columbae
    star_from_hours(28328, 5.9858, -42.8151, 3.96, 1.15),  # Eta Columbae
    star_from_hours(28199, 5.9589, -35.2833, 4.36, -0.17),  # Gamma Columbae
    # Remaining IAU constellation support stars.
    star_from_hours(200001, 10.4525, -31.0678, 4.25, 1.10),  # Alpha Antliae
    star_from_hours(200002, 10.9453, -37.1378, 4.60, 1.02),  # Iota Antliae
    star_from_hours(200003, 9.5128, -31.8894, 4.79, 1.25),  # Epsilon Antliae
    star_from_hours(200011, 14.7977, -79.0447, 3.83, 1.45),  # Alpha Apodis
    star_from_hours(200012, 16.7179, -77.5166, 4.24, 1.32),  # Beta Apodis
    star_from_hours(200013, 16.5575, -78.8971, 3.87, 1.55),  # Gamma Apodis
    star_from_hours(200014, 16.3391, -78.6957, 4.68, 0.95),  # Delta Apodis
    star_from_hours(200021, 4.6760, -41.8638, 4.45, 0.32),  # Alpha Caeli
    star_from_hours(200022, 4.7009, -37.1443, 5.04, 0.52),  # Beta Caeli
    star_from_hours(200023, 5.0734, -35.4828, 4.55, 1.18),  # Gamma Caeli
    star_from_hours(200031, 4.9008, 66.3427, 4.29, 0.12),  # Alpha Camelopardalis
    star_from_hours(200032, 5.0569, 60.4422, 4.03, 1.12),  # Beta Camelopardalis
    star_from_hours(200033, 3.8393, 71.3323, 4.59, 0.87),  # Gamma Camelopardalis
    star_from_hours(200041, 8.3088, -76.9197, 4.07, 0.90),  # Alpha Chamaeleontis
    star_from_hours(200042, 12.3058, -79.3122, 4.24, 0.55),  # Beta Chamaeleontis
    star_from_hours(200043, 10.5920, -78.6078, 4.11, 1.05),  # Gamma Chamaeleontis
    star_from_hours(200044, 10.7630, -80.5402, 4.45, 1.24),  # Delta Chamaeleontis
    star_from_hours(200051, 14.7085, -64.9751, 3.19, 0.15),  # Alpha Circini
    star_from_hours(200052, 15.2919, -58.8012, 4.07, 0.62),  # Beta Circini
    star_from_hours(200053, 15.3896, -59.3207, 4.48, 0.26),  # Gamma Circini
    star_from_hours(200061, 19.1579, -37.9045, 4.10, 0.95),  # Alpha Coronae Australis
    star_from_hours(200062, 19.1671, -39.3407, 4.11, 1.12),  # Beta Coronae Australis
    star_from_hours(200063, 19.1069, -37.0634, 4.23, 0.48),  # Gamma Coronae Australis
    star_from_hours(200064, 18.9787, -37.1074, 4.87, 0.30),  # Epsilon Coronae Australis
    star_from_hours(200071, 10.9962, -18.2988, 4.07, 1.07),  # Alpha Crateris
    star_from_hours(200072, 11.1943, -22.8256, 4.46, 0.98),  # Beta Crateris
    star_from_hours(200073, 11.4147, -17.6840, 4.08, 0.22),  # Gamma Crateris
    star_from_hours(200074, 11.3223, -14.7785, 3.56, 1.12),  # Delta Crateris
    star_from_hours(200081, 4.5666, -55.0450, 3.27, 0.74),  # Alpha Doradus
    star_from_hours(200082, 5.5604, -62.4898, 3.76, 0.25),  # Beta Doradus
    star_from_hours(200083, 4.2671, -51.4867, 4.25, 1.18),  # Gamma Doradus
    star_from_hours(200084, 5.7462, -65.7355, 4.35, 0.95),  # Delta Doradus
    star_from_hours(200091, 21.2637, 5.2479, 3.92, 0.52),  # Alpha Equulei
    star_from_hours(200092, 21.3815, 6.8111, 5.16, 0.38),  # Beta Equulei
    star_from_hours(200093, 21.1724, 10.1316, 4.69, 0.70),  # Gamma Equulei
    star_from_hours(200094, 21.2413, 10.0069, 4.49, 1.08),  # Delta Equulei
    star_from_hours(200101, 3.2012, -28.9869, 3.87, 0.54),  # Alpha Fornacis
    star_from_hours(200102, 2.8182, -32.4059, 4.46, 1.02),  # Beta Fornacis
    star_from_hours(200103, 2.0748, -29.2968, 4.69, 1.14),  # Nu Fornacis
    star_from_hours(200111, 4.2334, -42.2944, 3.86, 1.00),  # Alpha Horologii
    star_from_hours(200112, 2.9793, -64.0713, 4.98, 0.18),  # Beta Horologii
    star_from_hours(200113, 4.1807, -41.9937, 4.93, 0.40),  # Delta Horologii
    star_from_hours(200114, 2.6234, -52.5431, 5.31, 0.66),  # Eta Horologii
    star_from_hours(200121, 0.4276, -77.2542, 2.80, 0.62),  # Beta Hydri
    star_from_hours(200122, 1.9795, -61.5699, 2.86, 0.29),  # Alpha Hydri
    star_from_hours(200123, 3.7873, -74.2390, 3.26, 1.60),  # Gamma Hydri
    star_from_hours(200131, 20.6261, -47.2915, 3.11, 1.00),  # Alpha Indi
    star_from_hours(200132, 20.9135, -58.4541, 3.67, 0.98),  # Beta Indi
    star_from_hours(200133, 21.3311, -53.4494, 4.39, 0.35),  # Theta Indi
    star_from_hours(200134, 21.9653, -54.9926, 4.40, 1.05),  # Delta Indi
    star_from_hours(200141, 10.8885, 34.2149, 3.83, 0.95),  # Praecipua
    star_from_hours(200142, 10.4647, 36.7072, 4.21, 0.88),  # Beta Leonis Minoris
    star_from_hours(200143, 10.1238, 35.2447, 4.48, 0.42),  # 21 Leonis Minoris
    star_from_hours(200151, 6.1707, -74.7530, 5.09, 0.95),  # Alpha Mensae
    star_from_hours(200152, 5.0453, -71.3143, 5.31, 0.52),  # Beta Mensae
    star_from_hours(200153, 5.5314, -76.3417, 5.19, 1.00),  # Gamma Mensae
    star_from_hours(200161, 20.8328, -33.7797, 4.88, 0.33),  # Alpha Microscopii
    star_from_hours(200162, 21.0215, -32.2578, 4.67, 1.02),  # Gamma Microscopii
    star_from_hours(200163, 21.2986, -32.1725, 4.71, 0.90),  # Epsilon Microscopii
    star_from_hours(200171, 12.6197, -69.1355, 2.69, -0.18),  # Alpha Muscae
    star_from_hours(200172, 12.7714, -68.1081, 3.04, -0.16),  # Beta Muscae
    star_from_hours(200173, 12.5411, -72.1329, 3.84, -0.14),  # Gamma Muscae
    star_from_hours(200174, 13.0378, -71.5489, 3.61, 1.00),  # Delta Muscae
    star_from_hours(200181, 16.3307, -50.1554, 4.02, 1.10),  # Gamma2 Normae
    star_from_hours(200182, 16.4531, -47.5547, 4.47, 1.52),  # Epsilon Normae
    star_from_hours(200183, 16.0536, -49.2297, 4.65, 0.12),  # Eta Normae
    star_from_hours(200184, 16.1082, -45.1733, 4.73, 0.80),  # Delta Normae
    star_from_hours(200191, 21.6913, -77.3895, 3.76, 1.00),  # Nu Octantis
    star_from_hours(200192, 22.7677, -81.3816, 4.13, 1.62),  # Beta Octantis
    star_from_hours(200193, 14.4489, -83.6679, 4.32, 1.15),  # Delta Octantis
    star_from_hours(200194, 21.1461, -88.9565, 5.42, 0.45),  # Sigma Octantis
    star_from_hours(200201, 6.8032, -61.9414, 3.27, 0.18),  # Alpha Pictoris
    star_from_hours(200202, 5.7881, -51.0665, 3.85, 0.28),  # Beta Pictoris
    star_from_hours(200203, 5.8305, -56.1667, 4.50, 1.08),  # Gamma Pictoris
    star_from_hours(200211, 22.9608, -29.6222, 1.16, 0.09),  # Fomalhaut
    star_from_hours(200212, 22.5251, -32.3460, 4.29, 0.15),  # Beta Piscis Austrini
    star_from_hours(200213, 22.8754, -32.8754, 4.46, 1.05),  # Gamma Piscis Austrini
    star_from_hours(200214, 22.9325, -32.5396, 4.20, 0.30),  # Delta Piscis Austrini
    star_from_hours(200221, 8.7265, -33.1864, 3.68, 0.42),  # Alpha Pyxidis
    star_from_hours(200222, 8.6684, -35.3083, 3.97, 1.18),  # Beta Pyxidis
    star_from_hours(200223, 8.8422, -27.7101, 4.01, 1.00),  # Gamma Pyxidis
    star_from_hours(200231, 4.2404, -62.4739, 3.35, 0.92),  # Alpha Reticuli
    star_from_hours(200232, 3.7367, -64.8069, 3.84, 1.14),  # Beta Reticuli
    star_from_hours(200233, 4.2747, -59.3017, 4.44, 1.02),  # Epsilon Reticuli
    star_from_hours(200241, 0.9768, -29.3575, 4.30, 1.00),  # Alpha Sculptoris
    star_from_hours(200242, 23.5495, -37.8183, 4.38, 1.12),  # Beta Sculptoris
    star_from_hours(200243, 23.3137, -32.5320, 4.41, 1.00),  # Gamma Sculptoris
    star_from_hours(200244, 23.8154, -28.1303, 4.57, 0.38),  # Delta Sculptoris
    star_from_hours(200251, 18.5868, -8.2441, 3.85, 1.33),  # Alpha Scuti
    star_from_hours(200252, 18.7862, -4.7478, 4.22, 1.18),  # Beta Scuti
    star_from_hours(200253, 18.7046, -9.0526, 4.72, 0.28),  # Delta Scuti
    star_from_hours(200254, 18.4866, -14.5658, 4.67, 1.08),  # Gamma Scuti
    star_from_hours(200261, 10.1323, -0.3716, 4.49, 0.00),  # Alpha Sextantis
    star_from_hours(200262, 10.5049, -0.6369, 5.08, 0.35),  # Beta Sextantis
    star_from_hours(200263, 9.8751, -8.1049, 5.05, 1.02),  # Gamma Sextantis
    star_from_hours(200271, 18.4496, -45.9685, 3.49, 0.96),  # Alpha Telescopii
    star_from_hours(200272, 18.4805, -49.0706, 4.13, 1.12),  # Zeta Telescopii
    star_from_hours(200273, 18.1872, -45.9544, 4.52, 1.02),  # Epsilon Telescopii
    star_from_hours(200281, 16.8111, -69.0277, 1.91, 1.45),  # Alpha Trianguli Australis
    star_from_hours(200282, 15.9191, -63.4307, 2.85, 0.28),  # Beta Trianguli Australis
    star_from_hours(200283, 15.3152, -68.6795, 2.87, 1.00),  # Gamma Trianguli Australis
    star_from_hours(200291, 22.3084, -60.2596, 2.86, 1.39),  # Alpha Tucanae
    star_from_hours(200292, 23.2905, -58.2359, 3.99, 0.33),  # Gamma Tucanae
    star_from_hours(200293, 0.5258, -62.9581, 4.36, 0.58),  # Beta1 Tucanae
    star_from_hours(200294, 0.3345, -64.8748, 4.23, 0.34),  # Zeta Tucanae
    star_from_hours(200301, 8.4289, -66.1369, 3.75, 1.10),  # Beta Volantis
    star_from_hours(200302, 7.1458, -70.4989, 3.78, 0.98),  # Gamma2 Volantis
    star_from_hours(200303, 7.6970, -72.6061, 3.93, 0.15),  # Zeta Volantis
    star_from_hours(200304, 7.2805, -67.9572, 3.98, 1.04),  # Delta Volantis
    star_from_hours(200305, 9.0408, -66.3958, 4.00, 0.28),  # Alpha Volantis
    # Feature support stars.
    star_from_hours(200401, 10.1222, 16.7627, 3.52, -0.03),  # Eta Leonis
    star_from_hours(200402, 10.2782, 23.4173, 3.44, 0.31),  # Zeta Leonis
    star_from_hours(200403, 9.8794, 26.0069, 3.88, 1.22),  # Mu Leonis
    star_from_hours(200404, 9.7642, 23.7743, 2.98, 0.81),  # Epsilon Leonis
    star_from_hours(200405, 4.3823, 17.5425, 3.76, 0.98),  # Delta1 Tauri
    star_from_hours(200406, 4.4769, 19.1804, 3.53, 1.01),  # Epsilon Tauri
    star_from_hours(200407, 4.4777, 15.9622, 3.84, 0.18),  # Theta Tauri
    star_from_hours(200408, 3.7638, 24.3677, 3.87, -0.07),  # Maia
    star_from_hours(200409, 3.7479, 24.1133, 3.70, -0.09),  # Electra
    star_from_hours(200410, 3.7721, 23.9484, 4.18, -0.06),  # Merope
    star_from_hours(200411, 3.7532, 24.4673, 4.30, -0.06),  # Taygeta
    star_from_hours(200412, 3.7467, 24.2895, 5.45, -0.05),  # Celaeno
    star_from_hours(200413, 3.7651, 24.5546, 5.76, -0.04),  # Sterope
    star_from_hours(200414, 3.8194, 24.0534, 3.62, -0.06),  # Atlas
    star_from_hours(200415, 3.8198, 24.1368, 5.05, -0.08),  # Pleione
    star_from_hours(200416, 23.2861, 3.2823, 3.70, 0.92),  # Gamma Piscium
    star_from_hours(200417, 23.3390, 5.3813, 5.05, 1.05),  # 7 Piscium
    star_from_hours(200418, 23.4661, 6.3791, 4.27, 1.07),  # Theta Piscium
    star_from_hours(200419, 23.6658, 5.6263, 4.13, 0.50),  # Iota Piscium
    star_from_hours(200420, 23.7008, 1.7800, 4.50, 1.00),  # Lambda Piscium
    star_from_hours(200421, 23.7732, 3.4868, 5.04, 1.55),  # 19 Piscium
    star_from_hours(200422, 22.4805, -0.0199, 3.65, 0.01),  # Zeta Aquarii
    star_from_hours(200423, 22.5893, -0.1175, 4.04, 0.04),  # Eta Aquarii
    star_from_hours(200424, 22.4213, 1.3774, 4.66, -0.13),  # Pi Aquarii
    star_from_hours(200425, 17.2508, 36.8092, 3.16, 1.43),  # Pi Herculis
    star_from_hours(200426, 16.7149, 38.9223, 3.48, 0.94),  # Eta Herculis
    star_from_hours(200427, 16.6881, 31.6031, 2.81, 0.65),  # Zeta Herculis
    star_from_hours(200428, 17.0048, 30.9264, 3.91, 0.95),  # Epsilon Herculis
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
    36188: "Gomeisa",
    23875: "Cursa",
    18543: "Zaurak",
    13847: "Acamar",
    3419: "Diphda",
    14135: "Menkar",
    10826: "Mira",
    12706: "Baten Kaitos",
    9487: "Alrescha",
    7097: "Kullat Nunu",
    8198: "Torcular",
    118268: "Omega Piscium",
    9884: "Hamal",
    8903: "Sheratan",
    8832: "Mesarthim",
    101958: "Sualocin",
    101769: "Rotanev",
    102531: "Gamma Delphini",
    96837: "Sham",
    97365: "Delta Sagittae",
    98337: "Gamma Sagittae",
    95771: "Anser",
    98543: "23 Vulpeculae",
    99853: "31 Vulpeculae",
    90185: "Kaus Australis",
    92855: "Nunki",
    93506: "Ascella",
    89931: "Kaus Media",
    90496: "Kaus Borealis",
    88635: "Alnasl",
    86032: "Rasalhague",
    86742: "Cebalrai",
    79593: "Yed Prior",
    84012: "Sabik",
    80816: "Kornephoros",
    84345: "Rasalgethi",
    80170: "Sarin",
    84379: "Maasym",
    76267: "Alphecca",
    75695: "Nusakan",
    76952: "Gamma Coronae Borealis",
    77512: "Delta Coronae Borealis",
    72622: "Zubenelgenubi",
    74785: "Zubeneschamali",
    73714: "Brachium",
    75177: "Upsilon Librae",
    59803: "Gienah Corvi",
    61359: "Kraz",
    60965: "Algorab",
    59316: "Minkar",
    46390: "Alphard",
    64962: "Gamma Hydrae",
    43813: "Zeta Hydrae",
    52943: "Nu Hydrae",
    30867: "Beta Monocerotis",
    30419: "Epsilon Monocerotis",
    34769: "Delta Monocerotis",
    39429: "Naos",
    39757: "Tureis",
    35264: "Azmidi",
    44816: "Suhail",
    39953: "Regor",
    45941: "Alsephina",
    42913: "Markeb Velae",
    71860: "Men",
    73273: "Beta Lupi",
    76297: "Gamma Lupi",
    75141: "Delta Lupi",
    25985: "Arneb",
    25606: "Nihal",
    23685: "Epsilon Leporis",
    24305: "Mu Leporis",
    27288: "Zeta Leporis",
    27072: "Gamma Leporis",
    27654: "Delta Leporis",
    40526: "Tarf",
    42911: "Asellus Australis",
    42806: "Asellus Borealis",
    43103: "Iota Cancri",
    44066: "Acubens",
    40167: "Tegmine",
    77070: "Unukalhai",
    77233: "Beta Serpentis",
    78072: "Gamma Serpentis",
    76276: "Delta Serpentis",
    77622: "Epsilon Serpentis",
    89962: "Eta Serpentis",
    86263: "Xi Serpentis",
    63125: "Cor Caroli",
    61317: "Chara",
    66234: "24 Canum Venaticorum",
    60742: "Gamma Comae Berenices",
    64394: "Beta Comae Berenices",
    64241: "Diadem",
    60202: "11 Comae Berenices",
    63355: "36 Comae Berenices",
    8796: "Mothallah",
    10064: "Beta Trianguli",
    10670: "Gamma Trianguli",
    111169: "Alpha Lacertae",
    110538: "Beta Lacertae",
    111022: "5 Lacertae",
    111944: "11 Lacertae",
    109937: "1 Lacertae",
    33449: "15 Lyncis",
    36145: "21 Lyncis",
    41075: "Alsciaukat",
    45688: "38 Lyncis",
    45860: "Alpha Lyncis",
    100751: "Peacock",
    102395: "Beta Pavonis",
    99240: "Delta Pavonis",
    105858: "Gamma Pavonis",
    86929: "Eta Pavonis",
    85792: "Alpha Arae",
    85258: "Beta Arae",
    83081: "Zeta Arae",
    85267: "Gamma Arae",
    85727: "Delta Arae",
    88714: "Theta Arae",
    82363: "Eta Arae",
    109268: "Alnair",
    112122: "Tiaki",
    108085: "Aldhanab",
    112623: "Epsilon Gruis",
    114421: "Iota Gruis",
    110997: "Delta Gruis",
    2081: "Ankaa",
    5165: "Beta Phoenicis",
    6867: "Gamma Phoenicis",
    765: "Epsilon Phoenicis",
    7083: "Delta Phoenicis",
    5348: "Wurren",
    26634: "Phact",
    27628: "Wazn",
    30277: "Delta Columbae",
    25859: "Epsilon Columbae",
    28328: "Eta Columbae",
    28199: "Gamma Columbae",
    # Remaining IAU constellation support stars.
    200001: 'Alpha Antliae',
    200002: 'Iota Antliae',
    200003: 'Epsilon Antliae',
    200011: 'Alpha Apodis',
    200012: 'Beta Apodis',
    200013: 'Gamma Apodis',
    200014: 'Delta Apodis',
    200021: 'Alpha Caeli',
    200022: 'Beta Caeli',
    200023: 'Gamma Caeli',
    200031: 'Alpha Camelopardalis',
    200032: 'Beta Camelopardalis',
    200033: 'Gamma Camelopardalis',
    200041: 'Alpha Chamaeleontis',
    200042: 'Beta Chamaeleontis',
    200043: 'Gamma Chamaeleontis',
    200044: 'Delta Chamaeleontis',
    200051: 'Alpha Circini',
    200052: 'Beta Circini',
    200053: 'Gamma Circini',
    200061: 'Alpha Coronae Australis',
    200062: 'Beta Coronae Australis',
    200063: 'Gamma Coronae Australis',
    200064: 'Epsilon Coronae Australis',
    200071: 'Alpha Crateris',
    200072: 'Beta Crateris',
    200073: 'Gamma Crateris',
    200074: 'Delta Crateris',
    200081: 'Alpha Doradus',
    200082: 'Beta Doradus',
    200083: 'Gamma Doradus',
    200084: 'Delta Doradus',
    200091: 'Alpha Equulei',
    200092: 'Beta Equulei',
    200093: 'Gamma Equulei',
    200094: 'Delta Equulei',
    200101: 'Alpha Fornacis',
    200102: 'Beta Fornacis',
    200103: 'Nu Fornacis',
    200111: 'Alpha Horologii',
    200112: 'Beta Horologii',
    200113: 'Delta Horologii',
    200114: 'Eta Horologii',
    200121: 'Beta Hydri',
    200122: 'Alpha Hydri',
    200123: 'Gamma Hydri',
    200131: 'Alpha Indi',
    200132: 'Beta Indi',
    200133: 'Theta Indi',
    200134: 'Delta Indi',
    200141: 'Praecipua',
    200142: 'Beta Leonis Minoris',
    200143: '21 Leonis Minoris',
    200151: 'Alpha Mensae',
    200152: 'Beta Mensae',
    200153: 'Gamma Mensae',
    200161: 'Alpha Microscopii',
    200162: 'Gamma Microscopii',
    200163: 'Epsilon Microscopii',
    200171: 'Alpha Muscae',
    200172: 'Beta Muscae',
    200173: 'Gamma Muscae',
    200174: 'Delta Muscae',
    200181: 'Gamma2 Normae',
    200182: 'Epsilon Normae',
    200183: 'Eta Normae',
    200184: 'Delta Normae',
    200191: 'Nu Octantis',
    200192: 'Beta Octantis',
    200193: 'Delta Octantis',
    200194: 'Sigma Octantis',
    200201: 'Alpha Pictoris',
    200202: 'Beta Pictoris',
    200203: 'Gamma Pictoris',
    200211: 'Fomalhaut',
    200212: 'Beta Piscis Austrini',
    200213: 'Gamma Piscis Austrini',
    200214: 'Delta Piscis Austrini',
    200221: 'Alpha Pyxidis',
    200222: 'Beta Pyxidis',
    200223: 'Gamma Pyxidis',
    200231: 'Alpha Reticuli',
    200232: 'Beta Reticuli',
    200233: 'Epsilon Reticuli',
    200241: 'Alpha Sculptoris',
    200242: 'Beta Sculptoris',
    200243: 'Gamma Sculptoris',
    200244: 'Delta Sculptoris',
    200251: 'Alpha Scuti',
    200252: 'Beta Scuti',
    200253: 'Delta Scuti',
    200254: 'Gamma Scuti',
    200261: 'Alpha Sextantis',
    200262: 'Beta Sextantis',
    200263: 'Gamma Sextantis',
    200271: 'Alpha Telescopii',
    200272: 'Zeta Telescopii',
    200273: 'Epsilon Telescopii',
    200281: 'Alpha Trianguli Australis',
    200282: 'Beta Trianguli Australis',
    200283: 'Gamma Trianguli Australis',
    200291: 'Alpha Tucanae',
    200292: 'Gamma Tucanae',
    200293: 'Beta1 Tucanae',
    200294: 'Zeta Tucanae',
    200301: 'Beta Volantis',
    200302: 'Gamma2 Volantis',
    200303: 'Zeta Volantis',
    200304: 'Delta Volantis',
    200305: 'Alpha Volantis',
    # Feature support stars.
    200401: 'Eta Leonis',
    200402: 'Zeta Leonis',
    200403: 'Mu Leonis',
    200404: 'Epsilon Leonis',
    200405: 'Delta1 Tauri',
    200406: 'Epsilon Tauri',
    200407: 'Theta Tauri',
    200408: 'Maia',
    200409: 'Electra',
    200410: 'Merope',
    200411: 'Taygeta',
    200412: 'Celaeno',
    200413: 'Sterope',
    200414: 'Atlas',
    200415: 'Pleione',
    200416: 'Gamma Piscium',
    200417: '7 Piscium',
    200418: 'Theta Piscium',
    200419: 'Iota Piscium',
    200420: 'Lambda Piscium',
    200421: '19 Piscium',
    200422: 'Zeta Aquarii',
    200423: 'Eta Aquarii',
    200424: 'Pi Aquarii',
    200425: 'Pi Herculis',
    200426: 'Eta Herculis',
    200427: 'Zeta Herculis',
    200428: 'Epsilon Herculis',
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
