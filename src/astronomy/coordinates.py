from __future__ import annotations

import math

from src.sky.vector import Vec3


def equatorial_to_enu(
    ra_rad: float,
    dec_rad: float,
    latitude_rad: float,
    local_sidereal_time_rad: float,
) -> Vec3:
    """Convert equatorial RA/Dec to local ENU direction."""
    hour_angle = local_sidereal_time_rad - ra_rad
    cos_dec = math.cos(dec_rad)
    sin_dec = math.sin(dec_rad)
    cos_lat = math.cos(latitude_rad)
    sin_lat = math.sin(latitude_rad)
    cos_h = math.cos(hour_angle)
    sin_h = math.sin(hour_angle)

    east = -cos_dec * sin_h
    north = sin_dec * cos_lat - cos_dec * sin_lat * cos_h
    up = sin_dec * sin_lat + cos_dec * cos_lat * cos_h
    return Vec3(east, north, up).normalized()

