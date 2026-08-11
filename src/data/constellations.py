from __future__ import annotations

from astronomy.catalog import Constellation


CONSTELLATIONS: tuple[Constellation, ...] = (
    Constellation(
        id="ORI",
        name="Orion",
        main_star_ids=(27989, 24436, 25336, 27366, 26311, 26727, 25930, 26207),
        edges=(
            (27989, 25336),
            (25336, 25930),
            (25930, 26311),
            (26311, 26727),
            (26727, 27366),
            (27366, 24436),
            (27989, 26207),
            (24436, 26311),
        ),
        anchor_star_id=27989,
    ),
    Constellation(
        id="CYG",
        name="Cygnus",
        main_star_ids=(102098, 100453, 102488, 97165, 95947),
        edges=((102098, 100453), (100453, 102488), (100453, 97165), (100453, 95947)),
        anchor_star_id=102098,
    ),
    Constellation(
        id="CAS",
        name="Cassiopeia",
        main_star_ids=(746, 3179, 4427, 6686, 8886),
        edges=((746, 3179), (3179, 4427), (4427, 6686), (6686, 8886)),
        anchor_star_id=3179,
    ),
    Constellation(
        id="UMA",
        name="Ursa Major",
        main_star_ids=(54061, 53910, 58001, 59774, 62956, 65378, 67301),
        edges=((54061, 53910), (53910, 58001), (58001, 59774), (59774, 62956), (62956, 65378), (65378, 67301)),
        anchor_star_id=54061,
    ),
    Constellation(
        id="SCO",
        name="Scorpius",
        main_star_ids=(80763, 85927, 86228, 78401, 78820, 80112, 85696),
        edges=((78820, 78401), (78401, 80112), (80112, 80763), (80763, 85696), (85696, 85927), (85927, 86228)),
        anchor_star_id=80763,
    ),
)

