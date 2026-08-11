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
