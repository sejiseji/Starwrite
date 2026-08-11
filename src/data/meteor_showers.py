from __future__ import annotations

import math
from datetime import date

from astronomy.events import MeteorShowerEvent


METEOR_SHOWERS: tuple[MeteorShowerEvent, ...] = (
    MeteorShowerEvent(
        id="PER-2026",
        name="Perseids",
        year=2026,
        display_start=date(2026, 8, 12),
        display_end=date(2026, 8, 13),
        peak_hour_local=2,
        radiant_ra_rad=math.radians(48.0),
        radiant_dec_rad=math.radians(58.0),
        zhr=100,
        parent="109P/Swift-Tuttle",
    ),
)
