from __future__ import annotations

import math
from datetime import UTC, datetime

TAU = math.tau


def _as_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        raise ValueError("datetime must be timezone-aware")
    return dt.astimezone(UTC)


def julian_date(dt: datetime) -> float:
    """Return Julian Date for a timezone-aware datetime."""
    utc_dt = _as_utc(dt)
    year = utc_dt.year
    month = utc_dt.month
    day = utc_dt.day
    hour = (
        utc_dt.hour
        + utc_dt.minute / 60.0
        + utc_dt.second / 3600.0
        + utc_dt.microsecond / 3_600_000_000.0
    )

    if month <= 2:
        year -= 1
        month += 12

    a = year // 100
    b = 2 - a + a // 4
    jd0 = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5
    return jd0 + hour / 24.0


def greenwich_sidereal_time(jd: float) -> float:
    """Return apparent-enough Greenwich sidereal time in radians for v0.1."""
    t = (jd - 2451545.0) / 36525.0
    theta_deg = (
        280.46061837
        + 360.98564736629 * (jd - 2451545.0)
        + 0.000387933 * t * t
        - (t * t * t) / 38710000.0
    )
    return math.radians(theta_deg % 360.0)


def local_sidereal_time(jd: float, longitude_rad: float) -> float:
    """Return local sidereal time in radians. East longitude is positive."""
    return (greenwich_sidereal_time(jd) + longitude_rad) % TAU

