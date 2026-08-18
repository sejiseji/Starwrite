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

    def test_reinforced_constellation_edges_remain_present(self) -> None:
        constellations = {constellation.id: constellation for constellation in CONSTELLATIONS}

        expected_edges = {
            "ORI": ((27989, 26727), (24436, 25930), (25336, 26207)),
            "SCO": ((78401, 80763),),
            "GEM": ((36850, 37826), (32246, 34088)),
            "CMA": ((32349, 33579),),
            "UMI": ((72607, 77055),),
            "LEP": ((23685, 24305), (27654, 27288)),
            "VIR": ((63608, 66249),),
            "GRU": ((108085, 112122),),
            "COL": ((25859, 27628),),
            "VOL": ((200303, 200302),),
        }

        for constellation_id, edges in expected_edges.items():
            actual = {frozenset(edge) for edge in constellations[constellation_id].edges}
            for edge in edges:
                self.assertIn(frozenset(edge), actual, constellation_id)
