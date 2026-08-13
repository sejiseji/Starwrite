from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import UTC, datetime

from astronomy.coordinates import equatorial_to_enu
from astronomy.time import julian_date, local_sidereal_time

EARTH_RADIUS_KM = 6378.14


@dataclass(slots=True, frozen=True)
class MoonState:
    azimuth_deg: float
    altitude_deg: float
    right_ascension_deg: float
    declination_deg: float
    illumination: float
    phase_angle_deg: float
    waxing: bool
    distance_km: float
    visible: bool


def compute_moon(dt_utc: datetime, latitude_deg: float, longitude_deg: float) -> MoonState:
    """Return an approximate topocentric-enough moon state for Starwrite v0.1.

    This uses a compact low-precision lunar ephemeris. It is intended for visual
    sky context, not observatory-grade measurements.
    """
    if dt_utc.tzinfo is None:
        raise ValueError("dt_utc must be timezone-aware")
    utc = dt_utc.astimezone(UTC)
    jd = julian_date(utc)
    ra_rad, dec_rad, distance_km, moon_lon_rad, moon_lat_rad = _moon_equatorial_approx(jd)
    sun_lon_rad = _sun_ecliptic_longitude_approx(jd)
    separation = _angular_separation(moon_lon_rad, moon_lat_rad, sun_lon_rad, 0.0)
    illumination = max(0.0, min(1.0, (1.0 - math.cos(separation)) * 0.5))
    phase_diff_deg = (math.degrees(moon_lon_rad - sun_lon_rad) + 360.0) % 360.0
    direction = equatorial_to_enu(
        ra_rad,
        dec_rad,
        math.radians(latitude_deg),
        local_sidereal_time(jd, math.radians(longitude_deg)),
    )
    altitude_deg = math.degrees(math.asin(max(-1.0, min(1.0, direction.z))))
    azimuth_deg = (math.degrees(math.atan2(direction.x, direction.y)) + 360.0) % 360.0
    return MoonState(
        azimuth_deg=azimuth_deg,
        altitude_deg=altitude_deg,
        right_ascension_deg=math.degrees(ra_rad) % 360.0,
        declination_deg=math.degrees(dec_rad),
        illumination=illumination,
        phase_angle_deg=math.degrees(separation),
        waxing=phase_diff_deg < 180.0,
        distance_km=distance_km,
        visible=altitude_deg > 0.0,
    )


def get_phase_name(illumination: float, waxing: bool) -> str:
    if illumination < 0.03:
        return "new"
    if illumination > 0.97:
        return "full"
    if waxing:
        if illumination < 0.48:
            return "waxing_crescent"
        if illumination < 0.52:
            return "first_quarter"
        return "waxing_gibbous"
    if illumination > 0.52:
        return "waning_gibbous"
    if illumination > 0.48:
        return "last_quarter"
    return "waning_crescent"


def moon_light_level(state: MoonState | None) -> float:
    if state is None or not state.visible:
        return 0.0
    altitude_factor = max(0.0, min(1.0, state.altitude_deg / 30.0))
    return max(0.0, min(1.0, state.illumination * altitude_factor))


def moon_tags_from_state(state: MoonState | None) -> tuple[str, ...]:
    if state is None:
        return ()
    tags = ["moon_visible" if state.visible else "moon_hidden"]
    phase_name = get_phase_name(state.illumination, state.waxing)
    if phase_name == "new":
        tags.append("moon_new")
    elif phase_name == "full":
        tags.append("moon_full")
    elif "crescent" in phase_name:
        tags.append("moon_crescent")
    elif "quarter" in phase_name:
        tags.append("moon_quarter")
    else:
        tags.append("moon_gibbous")
    if state.visible:
        if state.altitude_deg < 10.0:
            tags.append("moon_low")
        elif state.altitude_deg > 45.0:
            tags.append("moon_high")
    return tuple(tags)


def moon_tags_from_capture_data(data: dict | None) -> tuple[str, ...]:
    if not data:
        return ()
    try:
        return moon_tags_from_state(moon_state_from_dict(data))
    except Exception:
        return ()


def moon_state_to_dict(state: MoonState) -> dict:
    return {
        "azimuth_deg": state.azimuth_deg,
        "altitude_deg": state.altitude_deg,
        "right_ascension_deg": state.right_ascension_deg,
        "declination_deg": state.declination_deg,
        "illumination": state.illumination,
        "phase_angle_deg": state.phase_angle_deg,
        "waxing": state.waxing,
        "distance_km": state.distance_km,
        "visible": state.visible,
        "phase": get_phase_name(state.illumination, state.waxing),
    }


def moon_state_from_dict(data: dict | None) -> MoonState | None:
    if not data:
        return None
    return MoonState(
        azimuth_deg=float(data["azimuth_deg"]),
        altitude_deg=float(data["altitude_deg"]),
        right_ascension_deg=float(data.get("right_ascension_deg", 0.0)),
        declination_deg=float(data.get("declination_deg", 0.0)),
        illumination=float(data["illumination"]),
        phase_angle_deg=float(data.get("phase_angle_deg", 0.0)),
        waxing=bool(data["waxing"]),
        distance_km=float(data.get("distance_km", 384400.0)),
        visible=bool(data.get("visible", float(data["altitude_deg"]) > 0.0)),
    )


def _moon_equatorial_approx(jd: float) -> tuple[float, float, float, float, float]:
    d = jd - 2451543.5
    node = math.radians(_wrap_deg(125.1228 - 0.0529538083 * d))
    inclination = math.radians(5.1454)
    perigee = math.radians(_wrap_deg(318.0634 + 0.1643573223 * d))
    eccentricity = 0.054900
    mean_anomaly = math.radians(_wrap_deg(115.3654 + 13.0649929509 * d))
    eccentric_anomaly = mean_anomaly + eccentricity * math.sin(mean_anomaly) * (1.0 + eccentricity * math.cos(mean_anomaly))

    xv = math.cos(eccentric_anomaly) - eccentricity
    yv = math.sqrt(1.0 - eccentricity * eccentricity) * math.sin(eccentric_anomaly)
    true_anomaly = math.atan2(yv, xv)
    distance_earth_radii = 60.2666 * math.sqrt(xv * xv + yv * yv)

    xh = distance_earth_radii * (
        math.cos(node) * math.cos(true_anomaly + perigee)
        - math.sin(node) * math.sin(true_anomaly + perigee) * math.cos(inclination)
    )
    yh = distance_earth_radii * (
        math.sin(node) * math.cos(true_anomaly + perigee)
        + math.cos(node) * math.sin(true_anomaly + perigee) * math.cos(inclination)
    )
    zh = distance_earth_radii * math.sin(true_anomaly + perigee) * math.sin(inclination)

    ecliptic_lon = math.atan2(yh, xh)
    ecliptic_lat = math.atan2(zh, math.sqrt(xh * xh + yh * yh))
    obliquity = math.radians(23.4393 - 3.563e-7 * d)
    xe = math.cos(ecliptic_lon) * math.cos(ecliptic_lat)
    ye = (
        math.sin(ecliptic_lon) * math.cos(ecliptic_lat) * math.cos(obliquity)
        - math.sin(ecliptic_lat) * math.sin(obliquity)
    )
    ze = (
        math.sin(ecliptic_lon) * math.cos(ecliptic_lat) * math.sin(obliquity)
        + math.sin(ecliptic_lat) * math.cos(obliquity)
    )
    return (
        math.atan2(ye, xe) % math.tau,
        math.atan2(ze, math.sqrt(xe * xe + ye * ye)),
        distance_earth_radii * EARTH_RADIUS_KM,
        ecliptic_lon % math.tau,
        ecliptic_lat,
    )


def _sun_ecliptic_longitude_approx(jd: float) -> float:
    n = jd - 2451545.0
    mean_longitude = _wrap_deg(280.460 + 0.9856474 * n)
    mean_anomaly = math.radians(_wrap_deg(357.528 + 0.9856003 * n))
    longitude = mean_longitude + 1.915 * math.sin(mean_anomaly) + 0.020 * math.sin(2.0 * mean_anomaly)
    return math.radians(_wrap_deg(longitude))


def _angular_separation(lon_a: float, lat_a: float, lon_b: float, lat_b: float) -> float:
    cos_sep = (
        math.sin(lat_a) * math.sin(lat_b)
        + math.cos(lat_a) * math.cos(lat_b) * math.cos(lon_a - lon_b)
    )
    return math.acos(max(-1.0, min(1.0, cos_sep)))


def _wrap_deg(value: float) -> float:
    return value % 360.0
