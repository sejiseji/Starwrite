from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, timedelta

from src.astronomy.events import MeteorShowerEvent

EVENT_YEAR_START = 2006
EVENT_YEAR_END = 2046
EVENT_SOURCE_LABEL = "IMO"


@dataclass(slots=True, frozen=True)
class RecurringMeteorShower:
    code: str
    name: str
    peak_month: int
    peak_day: int
    peak_hour_local: int
    radiant_ra_deg: float
    radiant_dec_deg: float
    zhr: int
    parent: str
    related_constellation_id: str | None


# v0.1 uses a compact annual catalog based on IMO calendar / working-list style
# values. Dates and radiants are approximate and repeated for each generated year.
RECURRING_METEOR_SHOWERS: tuple[RecurringMeteorShower, ...] = (
    RecurringMeteorShower("QUA", "Quadrantids", 1, 3, 3, 230.0, 49.0, 110, "2003 EH1", "BOO"),
    RecurringMeteorShower("GUM", "gamma Ursae Minorids", 1, 18, 3, 228.0, 67.0, 3, "unknown", "UMI"),
    RecurringMeteorShower("ACE", "alpha Centaurids", 2, 8, 3, 211.0, -58.0, 6, "unknown", "CEN"),
    RecurringMeteorShower("GNO", "gamma Normids", 3, 14, 3, 239.0, -50.0, 6, "unknown", "NOR"),
    RecurringMeteorShower("LYR", "Lyrids", 4, 22, 3, 271.0, 34.0, 18, "C/1861 G1 Thatcher", "LYR"),
    RecurringMeteorShower("PPU", "pi Puppids", 4, 24, 3, 110.0, -45.0, 5, "26P/Grigg-Skjellerup", "PUP"),
    RecurringMeteorShower("ETA", "Eta Aquariids", 5, 6, 3, 338.0, -1.0, 50, "1P/Halley", "AQR"),
    RecurringMeteorShower("ELY", "eta Lyrids", 5, 10, 3, 291.0, 43.0, 3, "C/1983 H1 IRAS-Araki-Alcock", "LYR"),
    RecurringMeteorShower("JBO", "June Bootids", 6, 27, 1, 221.0, 48.0, 5, "7P/Pons-Winnecke", "BOO"),
    RecurringMeteorShower("JPE", "July Pegasids", 7, 10, 3, 347.0, 11.0, 3, "unknown", "PEG"),
    RecurringMeteorShower("SDA", "Southern delta Aquariids", 7, 31, 2, 340.0, -16.0, 25, "96P/Machholz complex", "AQR"),
    RecurringMeteorShower("CAP", "Alpha Capricornids", 7, 30, 2, 307.0, -10.0, 5, "169P/NEAT", "CAP"),
    RecurringMeteorShower("ERI", "eta Eridanids", 8, 7, 3, 41.0, -11.0, 3, "unknown", "ERI"),
    RecurringMeteorShower("PER", "Perseids", 8, 13, 2, 48.0, 58.0, 100, "109P/Swift-Tuttle", "PER"),
    RecurringMeteorShower("KCG", "kappa Cygnids", 8, 17, 3, 288.0, 55.0, 3, "unknown", "CYG"),
    RecurringMeteorShower("SPE", "September epsilon Perseids", 9, 10, 3, 48.0, 40.0, 5, "unknown", "PER"),
    RecurringMeteorShower("DRA", "October Draconids", 10, 8, 1, 263.0, 56.0, 5, "21P/Giacobini-Zinner", "DRA"),
    RecurringMeteorShower("ORI", "Orionids", 10, 21, 3, 95.0, 16.0, 20, "1P/Halley", "ORI"),
    RecurringMeteorShower("STA", "Southern Taurids", 11, 5, 1, 52.0, 13.0, 5, "2P/Encke complex", "TAU"),
    RecurringMeteorShower("NTA", "Northern Taurids", 11, 12, 1, 58.0, 22.0, 5, "2P/Encke complex", "TAU"),
    RecurringMeteorShower("LEO", "Leonids", 11, 17, 3, 152.0, 22.0, 15, "55P/Tempel-Tuttle", "LEO"),
    RecurringMeteorShower("AMO", "alpha Monocerotids", 11, 21, 3, 117.0, 1.0, 5, "unknown", "MON"),
    RecurringMeteorShower("PHO", "December Phoenicids", 12, 2, 3, 18.0, -53.0, 5, "289P/Blanpain", "PHE"),
    RecurringMeteorShower("PUP", "Puppid-Velids", 12, 7, 3, 123.0, -45.0, 10, "unknown", "PUP"),
    RecurringMeteorShower("MON", "Monocerotids", 12, 9, 3, 100.0, 8.0, 3, "unknown", "MON"),
    RecurringMeteorShower("HYD", "sigma Hydrids", 12, 9, 3, 125.0, 2.0, 7, "unknown", "HYA"),
    RecurringMeteorShower("GEM", "Geminids", 12, 14, 2, 112.0, 33.0, 150, "3200 Phaethon", "GEM"),
    RecurringMeteorShower("COM", "Comae Berenicids", 12, 23, 3, 164.0, 29.0, 3, "unknown", "COM"),
    RecurringMeteorShower("URS", "Ursids", 12, 22, 3, 217.0, 76.0, 10, "8P/Tuttle", "UMI"),
)


def _event_from_recurring(shower: RecurringMeteorShower, year: int) -> MeteorShowerEvent:
    peak_date = date(year, shower.peak_month, shower.peak_day)
    return MeteorShowerEvent(
        id=f"{shower.code}-{year}",
        name=shower.name,
        year=year,
        display_start=peak_date - timedelta(days=1),
        display_end=peak_date,
        peak_hour_local=shower.peak_hour_local,
        radiant_ra_rad=math.radians(shower.radiant_ra_deg),
        radiant_dec_rad=math.radians(shower.radiant_dec_deg),
        zhr=shower.zhr,
        parent=shower.parent,
        related_constellation_id=shower.related_constellation_id,
    )


METEOR_SHOWERS: tuple[MeteorShowerEvent, ...] = tuple(
    _event_from_recurring(shower, year)
    for year in range(EVENT_YEAR_START, EVENT_YEAR_END + 1)
    for shower in RECURRING_METEOR_SHOWERS
)
