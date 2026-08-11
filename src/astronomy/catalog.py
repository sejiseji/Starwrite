from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Star:
    id: int
    ra_rad: float
    dec_rad: float
    magnitude: float
    color_index: float | None


@dataclass(slots=True, frozen=True)
class Constellation:
    id: str
    name: str
    main_star_ids: tuple[int, ...]
    edges: tuple[tuple[int, int], ...]
    anchor_star_id: int | None = None

