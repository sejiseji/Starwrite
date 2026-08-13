from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.stars import NAMED_STARS, STAR_NAMES
from data.stars import STARS_BY_ID


class CatalogTests(unittest.TestCase):
    def test_named_stars_have_display_names(self) -> None:
        self.assertEqual({star.id for star in NAMED_STARS}, set(STAR_NAMES))

    def test_catalog_has_all_88_iau_constellations(self) -> None:
        constellation_ids = {constellation.id for constellation in CONSTELLATIONS}
        expected_ids = {
            'AND',
            'ANT',
            'APS',
            'AQL',
            'AQR',
            'ARA',
            'ARI',
            'AUR',
            'BOO',
            'CAE',
            'CAM',
            'CAP',
            'CAR',
            'CAS',
            'CEN',
            'CEP',
            'CET',
            'CHA',
            'CIR',
            'CMA',
            'CMI',
            'CNC',
            'COL',
            'COM',
            'CRA',
            'CRB',
            'CRT',
            'CRU',
            'CRV',
            'CVN',
            'CYG',
            'DEL',
            'DOR',
            'DRA',
            'EQU',
            'ERI',
            'FOR',
            'GEM',
            'GRU',
            'HER',
            'HOR',
            'HYA',
            'HYI',
            'IND',
            'LAC',
            'LEO',
            'LEP',
            'LIB',
            'LMI',
            'LUP',
            'LYN',
            'LYR',
            'MEN',
            'MIC',
            'MON',
            'MUS',
            'NOR',
            'OCT',
            'OPH',
            'ORI',
            'PAV',
            'PEG',
            'PER',
            'PHE',
            'PIC',
            'PSC',
            'PSA',
            'PUP',
            'PYX',
            'RET',
            'SCL',
            'SCO',
            'SCT',
            'SER',
            'SEX',
            'SGE',
            'SGR',
            'TAU',
            'TEL',
            'TRA',
            'TRI',
            'TUC',
            'UMA',
            'UMI',
            'VEL',
            'VIR',
            'VOL',
            'VUL',
        }

        self.assertEqual(len(CONSTELLATIONS), 88)
        self.assertEqual(constellation_ids, expected_ids)

    def test_constellation_star_references_exist(self) -> None:
        for constellation in CONSTELLATIONS:
            for star_id in constellation.main_star_ids:
                self.assertIn(star_id, STARS_BY_ID, constellation.id)
            for a_id, b_id in constellation.edges:
                self.assertIn(a_id, STARS_BY_ID, constellation.id)
                self.assertIn(b_id, STARS_BY_ID, constellation.id)
