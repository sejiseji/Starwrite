from __future__ import annotations

from datetime import date, datetime, timezone

from src.astronomy.events import LunarEclipseEvent

LUNAR_ECLIPSE_SOURCE_LABEL = "NASA"


def _dt(year: int, month: int, day: int, hour: int, minute: int, second: int) -> datetime:
    return datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)


def _event(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    second: int,
    eclipse_type: str,
    umbral_magnitude: float,
    duration_minutes: int,
    totality_minutes: int | None,
    visibility_region: str,
) -> LunarEclipseEvent:
    event_date = date(year, month, day)
    type_code = "TLE" if eclipse_type == "total" else "PLE"
    return LunarEclipseEvent(
        id=f"{type_code}-{year}-{month:02d}-{day:02d}",
        name="Total Lunar Eclipse" if eclipse_type == "total" else "Partial Lunar Eclipse",
        year=year,
        display_start=event_date,
        display_end=event_date,
        # NASA's table gives the time of greatest eclipse in TD. For this prototype
        # the value is close enough to UTC for event navigation and visibility checks.
        greatest_at_utc=_dt(year, month, day, hour, minute, second),
        eclipse_type=eclipse_type,
        umbral_magnitude=umbral_magnitude,
        duration_minutes=duration_minutes,
        totality_minutes=totality_minutes,
        visibility_region=visibility_region,
    )


LUNAR_ECLIPSES: tuple[LunarEclipseEvent, ...] = (
    _event(2006, 9, 7, 18, 52, 25, "partial", 0.184, 91, None, "Europe, Africa, Asia, Australia"),
    _event(2007, 3, 3, 23, 21, 59, "total", 1.233, 221, 73, "Americas, Europe, Africa, Asia"),
    _event(2007, 8, 28, 10, 38, 27, "total", 1.476, 212, 90, "east Asia, Australia, Pacific, Americas"),
    _event(2008, 2, 21, 3, 27, 9, "total", 1.106, 205, 50, "Americas, Europe, Africa, central Atlantic"),
    _event(2008, 8, 16, 21, 11, 12, "partial", 0.808, 188, None, "South America, Europe, Africa, Asia, Australia"),
    _event(2009, 12, 31, 19, 23, 46, "partial", 0.076, 60, None, "Europe, Africa, Asia, Australia"),
    _event(2010, 6, 26, 11, 39, 34, "partial", 0.537, 163, None, "east Asia, Australia, Pacific, west Americas"),
    _event(2010, 12, 21, 8, 18, 4, "total", 1.256, 209, 72, "east Asia, Australia, Pacific, Americas, Europe"),
    _event(2011, 6, 15, 20, 13, 43, "total", 1.700, 219, 100, "South America, Europe, Africa, Asia, Australia"),
    _event(2011, 12, 10, 14, 32, 56, "total", 1.106, 212, 51, "Europe, east Africa, Asia, Australia, Pacific, North America"),
    _event(2012, 6, 4, 11, 4, 20, "partial", 0.370, 127, None, "Asia, Australia, Pacific, Americas"),
    _event(2013, 4, 25, 20, 8, 38, "partial", 0.015, 27, None, "Europe, Africa, Asia, Australia"),
    _event(2014, 4, 15, 7, 46, 48, "total", 1.291, 215, 78, "Australia, Pacific, Americas"),
    _event(2014, 10, 8, 10, 55, 44, "total", 1.166, 200, 59, "Asia, Australia, Pacific, Americas"),
    _event(2015, 4, 4, 12, 1, 24, "total", 1.001, 209, 5, "Asia, Australia, Pacific, Americas"),
    _event(2015, 9, 28, 2, 48, 17, "total", 1.276, 200, 72, "east Pacific, Americas, Europe, Africa, west Asia"),
    _event(2017, 8, 7, 18, 21, 38, "partial", 0.246, 115, None, "Europe, Africa, Asia, Australia"),
    _event(2018, 1, 31, 13, 31, 0, "total", 1.315, 203, 76, "Asia, Australia, Pacific, west North America"),
    _event(2018, 7, 27, 20, 22, 54, "total", 1.609, 235, 103, "South America, Europe, Africa, Asia, Australia"),
    _event(2019, 1, 21, 5, 13, 27, "total", 1.195, 197, 62, "central Pacific, Americas, Europe, Africa"),
    _event(2019, 7, 16, 21, 31, 55, "partial", 0.653, 178, None, "South America, Europe, Africa, Asia, Australia"),
    _event(2021, 5, 26, 11, 19, 53, "total", 1.009, 187, 15, "east Asia, Australia, Pacific, Americas"),
    _event(2021, 11, 19, 9, 4, 6, "partial", 0.974, 208, None, "Americas, north Europe, east Asia, Australia, Pacific"),
    _event(2022, 5, 16, 4, 12, 42, "total", 1.414, 207, 85, "Americas, Europe, Africa"),
    _event(2022, 11, 8, 11, 0, 22, "total", 1.359, 220, 85, "Asia, Australia, Pacific, Americas"),
    _event(2023, 10, 28, 20, 15, 18, "partial", 0.122, 77, None, "east Americas, Europe, Africa, Asia, Australia"),
    _event(2024, 9, 18, 2, 45, 25, "partial", 0.085, 63, None, "Americas, Europe, Africa"),
    _event(2025, 3, 14, 6, 59, 56, "total", 1.178, 218, 65, "Pacific, Americas, west Europe, west Africa"),
    _event(2025, 9, 7, 18, 12, 58, "total", 1.362, 209, 82, "Europe, Africa, Asia, Australia"),
    _event(2026, 3, 3, 11, 34, 52, "total", 1.151, 207, 58, "east Asia, Australia, Pacific, Americas"),
    _event(2026, 8, 28, 4, 14, 4, "partial", 0.930, 198, None, "east Pacific, Americas, Europe, Africa"),
    _event(2028, 1, 12, 4, 14, 13, "partial", 0.066, 56, None, "Americas, Europe, Africa"),
    _event(2028, 7, 6, 18, 20, 57, "partial", 0.389, 141, None, "Europe, Africa, Asia, Australia"),
    _event(2028, 12, 31, 16, 53, 15, "total", 1.246, 209, 71, "Europe, Africa, Asia, Australia, Pacific"),
    _event(2029, 6, 26, 3, 23, 22, "total", 1.844, 220, 102, "Americas, Europe, Africa, Middle East"),
    _event(2029, 12, 20, 22, 43, 12, "total", 1.117, 213, 54, "Americas, Europe, Africa, Asia"),
    _event(2030, 6, 15, 18, 34, 34, "partial", 0.502, 144, None, "Europe, Africa, Asia, Australia"),
    _event(2032, 4, 25, 15, 14, 51, "total", 1.191, 211, 66, "east Africa, Asia, Australia, Pacific"),
    _event(2032, 10, 18, 19, 3, 40, "total", 1.103, 196, 47, "Africa, Europe, Asia, Australia"),
    _event(2033, 4, 14, 19, 13, 51, "total", 1.094, 215, 49, "Europe, Africa, Asia, Australia"),
    _event(2033, 10, 8, 10, 56, 23, "total", 1.350, 202, 79, "Asia, Australia, Pacific, Americas"),
    _event(2034, 9, 28, 2, 47, 37, "partial", 0.014, 27, None, "Americas, Europe, Africa"),
    _event(2035, 8, 19, 1, 12, 15, "partial", 0.104, 77, None, "Americas, Europe, Africa, Middle East"),
    _event(2036, 2, 11, 22, 13, 6, "total", 1.299, 202, 74, "Americas, Europe, Africa, Asia, west Australia"),
    _event(2036, 8, 7, 2, 52, 32, "total", 1.454, 231, 95, "Americas, Europe, Africa, west Asia"),
    _event(2037, 1, 31, 14, 1, 38, "total", 1.207, 197, 64, "east Europe, east Africa, Asia, Australia, Pacific, North America"),
    _event(2037, 7, 27, 4, 9, 53, "partial", 0.809, 192, None, "Americas, Europe, Africa"),
    _event(2039, 6, 6, 18, 54, 25, "partial", 0.885, 179, None, "Europe, Africa, Asia, Australia"),
    _event(2039, 11, 30, 16, 56, 28, "partial", 0.943, 206, None, "Europe, Africa, Asia, Australia, Pacific"),
    _event(2040, 5, 26, 11, 46, 22, "total", 1.535, 211, 92, "east Asia, Australia, Pacific, west Americas"),
    _event(2040, 11, 18, 19, 4, 41, "total", 1.397, 220, 88, "east Americas, Europe, Africa, Asia, Australia"),
    _event(2041, 5, 16, 0, 43, 3, "partial", 0.064, 58, None, "east Americas, Europe, Africa, west Asia"),
    _event(2041, 11, 8, 4, 35, 5, "partial", 0.170, 90, None, "Americas, Europe, Africa"),
    _event(2043, 3, 25, 14, 32, 4, "total", 1.114, 215, 53, "east Africa, east Europe, Asia, Australia, Pacific, west North America"),
    _event(2043, 9, 19, 1, 51, 50, "total", 1.256, 206, 72, "Americas, Europe, Africa, west Asia"),
    _event(2044, 3, 13, 19, 38, 33, "total", 1.203, 209, 66, "east South America, Europe, Africa, Asia, Australia"),
    _event(2044, 9, 7, 11, 20, 44, "total", 1.046, 206, 34, "east Asia, Australia, Pacific, Americas"),
    _event(2046, 1, 22, 13, 2, 37, "partial", 0.053, 50, None, "Asia, Australia, North America"),
    _event(2046, 7, 18, 1, 6, 5, "partial", 0.246, 115, None, "Americas, Europe, Africa, west Asia"),
)
