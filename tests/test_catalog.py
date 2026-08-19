from __future__ import annotations

import unittest

from data.constellations import CONSTELLATIONS
from data.constellation_line_reference_88 import (
    CONSTELLATION_LINE_EDGES_HIP,
    CONSTELLATION_LINE_POLYLINES_HIP,
    CONSTELLATION_MAIN_STAR_IDS_HIP,
    validate_constellation_line_reference,
)
from data.sky_features import ASTERISMS
from data.stars import NAMED_STARS, STAR_NAMES
from data.stars import STARS_BY_ID


class CatalogTests(unittest.TestCase):
    def test_named_stars_have_display_names(self) -> None:
        self.assertEqual({star.id for star in NAMED_STARS}, set(STAR_NAMES))
        self.assertEqual(len({star.id for star in NAMED_STARS}), len(NAMED_STARS))

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
        self.assertEqual(set(CONSTELLATION_LINE_EDGES_HIP), expected_ids)
        self.assertEqual(set(CONSTELLATION_MAIN_STAR_IDS_HIP), expected_ids)
        self.assertEqual(set(CONSTELLATION_LINE_POLYLINES_HIP), expected_ids)

    def test_constellation_reference_profile_counts(self) -> None:
        edge_count = sum(len(edges) for edges in CONSTELLATION_LINE_EDGES_HIP.values())
        endpoint_ids = {
            star_id
            for edges in CONSTELLATION_LINE_EDGES_HIP.values()
            for edge in edges
            for star_id in edge
        }

        self.assertEqual(edge_count, 757)
        self.assertEqual(len(endpoint_ids), 773)

    def test_constellation_star_references_exist(self) -> None:
        for constellation in CONSTELLATIONS:
            for star_id in constellation.main_star_ids:
                self.assertIn(star_id, STARS_BY_ID, constellation.id)
            for a_id, b_id in constellation.edges:
                self.assertIn(a_id, STARS_BY_ID, constellation.id)
                self.assertIn(b_id, STARS_BY_ID, constellation.id)

    def test_constellation_lines_match_standard_reference(self) -> None:
        constellations = {constellation.id: constellation for constellation in CONSTELLATIONS}

        for constellation_id, constellation in constellations.items():
            self.assertEqual(constellation.edges, CONSTELLATION_LINE_EDGES_HIP[constellation_id])
            self.assertEqual(constellation.main_star_ids, CONSTELLATION_MAIN_STAR_IDS_HIP[constellation_id])

    def test_constellation_reference_edges_are_valid(self) -> None:
        validate_constellation_line_reference()
        for constellation_id, edges in CONSTELLATION_LINE_EDGES_HIP.items():
            seen_edges: set[frozenset[int]] = set()
            for a_id, b_id in edges:
                self.assertNotEqual(a_id, b_id, constellation_id)
                undirected = frozenset((a_id, b_id))
                self.assertNotIn(undirected, seen_edges, constellation_id)
                seen_edges.add(undirected)

    def test_japanese_reaudit_override_targets_are_consistent(self) -> None:
        target_edge_counts = {
            'AND': 15,
            'APS': 3,
            'AQR': 17,
            'BOO': 13,
            'CAR': 12,
            'CEN': 25,
            'CEP': 9,
            'CET': 15,
            'LUP': 15,
            'MIC': 5,
            'PHE': 7,
            'SCT': 2,
            'SGR': 19,
            'TAU': 20,
            'VUL': 2,
        }
        expected_johanley_targets = {
            'APS',
            'AQR',
            'CAR',
            'CEN',
            'CEP',
            'CET',
            'LUP',
            'MIC',
            'PHE',
            'SCT',
            'SGR',
            'TAU',
            'VUL',
        }

        self.assertEqual(set(target_edge_counts) - expected_johanley_targets, {'AND', 'BOO'})

        for constellation_id, expected_edge_count in target_edge_counts.items():
            rebuilt_edges = tuple(
                (polyline[index], polyline[index + 1])
                for polyline in CONSTELLATION_LINE_POLYLINES_HIP[constellation_id]
                for index in range(len(polyline) - 1)
            )
            endpoint_ids = {
                star_id
                for edge in CONSTELLATION_LINE_EDGES_HIP[constellation_id]
                for star_id in edge
            }

            self.assertEqual(len(CONSTELLATION_LINE_EDGES_HIP[constellation_id]), expected_edge_count)
            self.assertEqual(rebuilt_edges, CONSTELLATION_LINE_EDGES_HIP[constellation_id])
            self.assertEqual(set(CONSTELLATION_MAIN_STAR_IDS_HIP[constellation_id]), endpoint_ids)

    def test_feature_edges_are_not_merged_into_constellation_edges(self) -> None:
        constellation_edges = {
            frozenset(edge)
            for constellation in CONSTELLATIONS
            for edge in constellation.edges
        }
        star_constellations: dict[int, set[str]] = {}
        for constellation in CONSTELLATIONS:
            for star_id in constellation.main_star_ids:
                star_constellations.setdefault(star_id, set()).add(constellation.id)

        for feature in ASTERISMS:
            for edge in feature.edges:
                a_id, b_id = edge
                shared_constellations = star_constellations.get(a_id, set()) & star_constellations.get(b_id, set())
                if not shared_constellations:
                    self.assertNotIn(frozenset(edge), constellation_edges, feature.id)
