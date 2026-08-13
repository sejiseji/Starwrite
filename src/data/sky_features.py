from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Asterism:
    id: str
    name: str
    star_ids: tuple[int, ...]
    edges: tuple[tuple[int, int], ...]


@dataclass(slots=True, frozen=True)
class SkyPath:
    id: str
    name: str
    points: tuple[tuple[float, float], ...]


def _hours_to_rad(hours: float) -> float:
    return math.radians(hours * 15.0)


def _deg_to_rad(degrees: float) -> float:
    return math.radians(degrees)


ASTERISMS: tuple[Asterism, ...] = (
    Asterism(
        id="SUMMER_TRIANGLE",
        name="Summer Triangle",
        star_ids=(91262, 97649, 102098),
        edges=((91262, 97649), (97649, 102098), (102098, 91262)),
    ),
    Asterism(
        id="WINTER_TRIANGLE",
        name="Winter Triangle",
        star_ids=(27989, 32349, 37279),
        edges=((27989, 32349), (32349, 37279), (37279, 27989)),
    ),
    Asterism(
        id="BIG_DIPPER",
        name="Big Dipper",
        star_ids=(54061, 53910, 58001, 59774, 62956, 65378, 67301),
        edges=((54061, 53910), (53910, 58001), (58001, 59774), (59774, 62956), (62956, 65378), (65378, 67301)),
    ),
    Asterism(
        id="SPRING_ARC",
        name="Spring Arc",
        star_ids=(67301, 65378, 69673, 65474),
        edges=((67301, 65378), (65378, 69673), (69673, 65474)),
    ),
    Asterism(
        id="SPRING_TRIANGLE",
        name="Spring Triangle",
        star_ids=(69673, 65474, 57632),
        edges=((69673, 65474), (65474, 57632), (57632, 69673)),
    ),
    Asterism(
        id="GREAT_DIAMOND",
        name="Great Diamond",
        star_ids=(69673, 65474, 57632, 63125),
        edges=((69673, 65474), (65474, 57632), (57632, 63125), (63125, 69673)),
    ),
    Asterism(
        id="WINTER_HEXAGON",
        name="Winter Hexagon",
        star_ids=(24608, 21421, 24436, 32349, 37279, 37826),
        edges=((24608, 21421), (21421, 24436), (24436, 32349), (32349, 37279), (37279, 37826), (37826, 24608)),
    ),
    Asterism(
        id="ORION_BELT",
        name="Orion's Belt",
        star_ids=(26727, 26311, 25930),
        edges=((26727, 26311), (26311, 25930)),
    ),
    Asterism(
        id="GREAT_SQUARE",
        name="Great Square of Pegasus",
        star_ids=(113963, 113881, 677, 1067),
        edges=((113963, 113881), (113881, 677), (677, 1067), (1067, 113963)),
    ),
    Asterism(
        id="NORTHERN_CROSS",
        name="Northern Cross",
        star_ids=(102098, 100453, 95947, 102488, 97165),
        edges=((102098, 100453), (100453, 95947), (102488, 100453), (100453, 97165)),
    ),
    Asterism(
        id="CASSIOPEIA_W",
        name="Cassiopeia W",
        star_ids=(746, 3179, 4427, 6686, 8886),
        edges=((746, 3179), (3179, 4427), (4427, 6686), (6686, 8886)),
    ),
    Asterism(
        id="POINTER_STARS",
        name="Pointer Stars",
        star_ids=(54061, 53910),
        edges=((54061, 53910),),
    ),
    Asterism(
        id="SOUTHERN_CROSS",
        name="Southern Cross",
        star_ids=(60718, 62434, 61084, 59747),
        edges=((60718, 61084), (62434, 59747)),
    ),
    Asterism(
        id="SOUTHERN_POINTERS",
        name="Southern Pointers",
        star_ids=(71683, 68702),
        edges=((71683, 68702),),
    ),
    Asterism(
        id="TEAPOT",
        name="Teapot",
        star_ids=(90496, 89931, 90185, 88635, 93506, 92855),
        edges=((90496, 89931), (89931, 90185), (90185, 88635), (88635, 90496), (89931, 93506), (93506, 92855)),
    ),
)


MILKY_WAY = SkyPath(
    id="MILKY_WAY",
    name="Milky Way",
    points=tuple(
        (_hours_to_rad(ra_hours), _deg_to_rad(dec_deg))
        for ra_hours, dec_deg in (
            (0.4, 60.0),
            (1.6, 58.0),
            (3.3, 50.0),
            (5.3, 32.0),
            (6.6, 8.0),
            (7.4, -20.0),
            (8.8, -45.0),
            (10.5, -60.0),
            (12.5, -62.0),
            (14.5, -55.0),
            (16.3, -35.0),
            (17.7, -24.0),
            (18.9, -2.0),
            (20.2, 35.0),
            (21.6, 55.0),
            (23.0, 60.0),
            (0.4, 60.0),
        )
    ),
)


SKY_PATHS: tuple[SkyPath, ...] = (MILKY_WAY,)
