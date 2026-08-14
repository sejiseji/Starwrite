from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import pyxel

if not hasattr(pyxel, "pix") and hasattr(pyxel, "pset"):
    pyxel.pix = pyxel.pset


IPHONE16_SCREEN_HEIGHT = 696
IPHONE16_MIN_SCREEN_WIDTH = 396
IPHONE16_MAX_SCREEN_WIDTH = 430
SMARTPHONE_FIRST_SCREEN_SIZE = (IPHONE16_MIN_SCREEN_WIDTH, IPHONE16_SCREEN_HEIGHT)
SETTINGS_KEY = "starwrite_v02_settings"
PREFETCH_CORE = (
    "src/app_pyxres_sounds.py",
    "src/audio/bgm.py",
    "src/audio/ui_sfx.py",
    "src/astronomy/catalog.py",
    "src/astronomy/coordinates.py",
    "src/astronomy/events.py",
    "src/astronomy/moon.py",
    "src/astronomy/observer.py",
    "src/astronomy/time.py",
    "src/data/constellations.py",
    "src/data/meteor_showers.py",
    "src/data/sky_features.py",
    "src/data/stars.py",
    "src/sky/camera.py",
    "src/sky/capture.py",
    "src/sky/letters.py",
    "src/sky/meteors.py",
    "src/sky/moon.py",
    "src/sky/renderer.py",
    "src/sky/simulation.py",
    "src/sky/vector.py",
    "src/ui/hud.py",
    "src/ui/localization.py",
)
PREFETCH_JA = ("src/data/font_jp.py",)
CITIES: dict[str, tuple[tuple[str, float, float], ...]] = {
    "JP": (
        ("Tokyo", 35.6762, 139.6503),
        ("Fukushima", 37.7608, 140.4747),
        ("Sapporo", 43.0618, 141.3545),
        ("Sendai", 38.2682, 140.8694),
        ("Niigata", 37.9161, 139.0364),
        ("Nagoya", 35.1815, 136.9066),
        ("Osaka", 34.6937, 135.5023),
        ("Hiroshima", 34.3853, 132.4553),
        ("Fukuoka", 33.5902, 130.4017),
        ("Naha", 26.2124, 127.6792),
    ),
    "US": (
        ("New York", 40.7128, -74.0060),
        ("Los Angeles", 34.0522, -118.2437),
        ("Chicago", 41.8781, -87.6298),
        ("Seattle", 47.6062, -122.3321),
        ("Honolulu", 21.3099, -157.8581),
    ),
    "GB": (("London", 51.5072, -0.1276),),
    "FR": (("Paris", 48.8566, 2.3522),),
    "DE": (("Berlin", 52.5200, 13.4050),),
    "FI": (("Helsinki", 60.1699, 24.9384), ("Tampere", 61.4978, 23.7610)),
    "AU": (("Sydney", -33.8688, 151.2093), ("Melbourne", -37.8136, 144.9631), ("Hobart", -42.8821, 147.3272)),
    "NZ": (("Auckland", -36.8509, 174.7645),),
    "BR": (("Sao Paulo", -23.5558, -46.6396),),
    "ZA": (("Cape Town", -33.9249, 18.4241),),
    "SG": (("Singapore", 1.3521, 103.8198),),
    "IN": (("Delhi", 28.6139, 77.2090),),
    "CA": (("Toronto", 43.6532, -79.3832), ("Vancouver", 49.2827, -123.1207)),
    "KR": (("Seoul", 37.5665, 126.9780),),
    "TW": (("Taipei", 25.0330, 121.5654),),
    "TH": (("Bangkok", 13.7563, 100.5018),),
}
COUNTRIES = tuple(CITIES)


def _screen_size() -> tuple[int, int]:
    try:
        from js import window  # type: ignore

        width = float(window.innerWidth)
        height = float(window.innerHeight)
        is_portrait_phone = width <= 500 and height / max(width, 1.0) >= 1.7
        if is_portrait_phone:
            screen_width = int(round(IPHONE16_SCREEN_HEIGHT * width / max(height, 1.0))) + 2
            screen_width = max(IPHONE16_MIN_SCREEN_WIDTH, min(IPHONE16_MAX_SCREEN_WIDTH, screen_width))
            return (screen_width, IPHONE16_SCREEN_HEIGHT)
    except Exception:
        pass
    return SMARTPHONE_FIRST_SCREEN_SIZE


def _load_settings() -> dict:
    try:
        from js import window  # type: ignore

        raw = window.localStorage.getItem(SETTINGS_KEY)
        return json.loads(raw) if raw else {}
    except Exception:
        return {}


def _save_settings(settings: dict) -> None:
    try:
        from js import window  # type: ignore

        window.localStorage.setItem(SETTINGS_KEY, json.dumps(settings))
    except Exception:
        pass


def _detect_language() -> str:
    try:
        from js import navigator  # type: ignore

        values = list(navigator.languages) if navigator.languages else [navigator.language]
        return "ja" if any(str(value).lower().startswith("ja") for value in values) else "en"
    except Exception:
        return "en"


def _setup_requested() -> bool:
    try:
        from js import window  # type: ignore

        return "setup" in str(window.location.search)
    except Exception:
        return False


class BootstrapApp:
    def __init__(self) -> None:
        self.width, self.height = _screen_size()
        settings = _load_settings()
        self.language = settings.get("language") if settings.get("language") in ("ja", "en") else _detect_language()
        self.country_index = COUNTRIES.index(settings.get("location_country")) if settings.get("location_country") in COUNTRIES else 0
        self.city_index = self._city_index_for(settings.get("location_city"))
        self.prefetch_files = list(PREFETCH_CORE)
        if self.language == "ja":
            self.prefetch_files.extend(PREFETCH_JA)
        self.prefetch_index = 0
        self.loading_frames = 0
        self.main_app = None
        self.state = "SETUP" if _setup_requested() or not settings.get("setup_complete") else "LOADING"
        pyxel.init(self.width, self.height, title="Starwrite Sky", fps=30)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    @property
    def country(self) -> str:
        return COUNTRIES[self.country_index]

    @property
    def cities(self) -> tuple[tuple[str, float, float], ...]:
        return CITIES[self.country]

    @property
    def city(self) -> tuple[str, float, float]:
        return self.cities[self.city_index % len(self.cities)]

    def _city_index_for(self, city_name: object) -> int:
        country = COUNTRIES[self.country_index]
        for index, city in enumerate(CITIES[country]):
            if city[0] == city_name:
                return index
        return 0

    def update(self) -> None:
        if self.main_app is not None:
            self.main_app.update()
            return
        self._prefetch_step()
        if self.state == "SETUP":
            self._handle_setup_input()
        elif self.state == "LOADING":
            self.loading_frames += 1
            if self.prefetch_index >= len(self.prefetch_files) and self.loading_frames >= 12:
                self._start_main_app()

    def draw(self) -> None:
        if self.main_app is not None:
            self.main_app.draw()
            return
        pyxel.cls(0)
        self._draw_stars()
        if self.state == "SETUP":
            self._draw_setup()
        else:
            self._draw_loading()

    def _prefetch_step(self) -> None:
        if self.prefetch_index >= len(self.prefetch_files):
            return
        path = self.prefetch_files[self.prefetch_index]
        self.prefetch_index += 1
        try:
            from js import window  # type: ignore

            window.fetch(path).catch(lambda _error: None)
        except Exception:
            pass

    def _handle_setup_input(self) -> None:
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return
        x, y = pyxel.mouse_x, pyxel.mouse_y
        if self._hit(x, y, self._rect("ja")):
            self.language = "ja"
            if PREFETCH_JA[0] not in self.prefetch_files:
                self.prefetch_files.extend(PREFETCH_JA)
        elif self._hit(x, y, self._rect("en")):
            self.language = "en"
        elif self._hit(x, y, self._rect("country_prev")):
            self.country_index = (self.country_index - 1) % len(COUNTRIES)
            self.city_index = 0
        elif self._hit(x, y, self._rect("country_next")):
            self.country_index = (self.country_index + 1) % len(COUNTRIES)
            self.city_index = 0
        elif self._hit(x, y, self._rect("city_prev")):
            self.city_index = (self.city_index - 1) % len(self.cities)
        elif self._hit(x, y, self._rect("city_next")):
            self.city_index = (self.city_index + 1) % len(self.cities)
        elif self._hit(x, y, self._rect("start")):
            self._save_selection()
            self.state = "LOADING"
            self.loading_frames = 0

    def _save_selection(self) -> None:
        name, latitude, longitude = self.city
        settings = _load_settings()
        settings.update(
            {
                "latitude": latitude,
                "longitude": longitude,
                "language": self.language,
                "location_country": self.country,
                "location_city": name,
                "setup_complete": True,
            }
        )
        _save_settings(settings)

    def _start_main_app(self) -> None:
        self.state = "MAIN"
        from app_pyxres_sounds import StarSkyApp

        self.main_app = StarSkyApp(start_pyxel=False)

    def _rect(self, key: str) -> tuple[int, int, int, int]:
        cx = self.width // 2
        top = 138
        rects = {
            "ja": (cx - 112, top + 76, 104, 34),
            "en": (cx + 8, top + 76, 104, 34),
            "country_prev": (cx - 146, top + 156, 40, 34),
            "country_next": (cx + 106, top + 156, 40, 34),
            "city_prev": (cx - 146, top + 226, 40, 34),
            "city_next": (cx + 106, top + 226, 40, 34),
            "start": (cx - 92, top + 306, 184, 40),
        }
        return rects[key]

    @staticmethod
    def _hit(x: int, y: int, rect: tuple[int, int, int, int]) -> bool:
        rx, ry, rw, rh = rect
        return rx <= x < rx + rw and ry <= y < ry + rh

    def _draw_setup(self) -> None:
        cx = self.width // 2
        top = 138
        self._center_text("STARWRITE", top, 7)
        self._center_text("CHOOSE A SKY TO BEGIN", top + 24, 13)
        self._center_text("NO LOCATION ACCESS", top + 42, 5)
        self._label("LANGUAGE", cx - 112, top + 62)
        self._button(self._rect("ja"), "JA", self.language == "ja", 10)
        self._button(self._rect("en"), "EN", self.language == "en", 10)
        self._label("COUNTRY / REGION", cx - 112, top + 136)
        self._button(self._rect("country_prev"), "-", False, 7)
        self._button(self._rect("country_next"), "+", False, 7)
        self._center_text(self.country, top + 167, 7)
        self._label("CITY", cx - 112, top + 206)
        self._button(self._rect("city_prev"), "-", False, 7)
        self._button(self._rect("city_next"), "+", False, 7)
        self._center_text(self.city[0], top + 237, 7)
        self._button(self._rect("start"), "START", True, 11)
        loaded = min(self.prefetch_index, len(self.prefetch_files))
        self._center_text(f"PREPARING {loaded}/{len(self.prefetch_files)}", top + 366, 5)

    def _draw_loading(self) -> None:
        y = self.height // 2 - 18
        dots = "." * ((pyxel.frame_count // 12) % 4)
        self._center_text("LOADING SKY" + dots, y, 7)
        loaded = min(self.prefetch_index, len(self.prefetch_files))
        self._center_text(f"FILES {loaded}/{len(self.prefetch_files)}", y + 22, 13)

    def _draw_stars(self) -> None:
        for index in range(80):
            x = (index * 73 + 19) % self.width
            y = (index * 137 + 31 + pyxel.frame_count // 3) % self.height
            color = 7 if index % 5 else 10
            pyxel.pset(x, y, color)

    def _button(self, rect: tuple[int, int, int, int], label: str, active: bool, color: int) -> None:
        x, y, w, h = rect
        pyxel.rect(x, y, w, h, 5 if active else 1)
        pyxel.rectb(x, y, w, h, 10 if active else 13)
        self._center_text(label, y + max(3, (h - 5) // 2), color, x, w)

    @staticmethod
    def _label(text: str, x: int, y: int) -> None:
        pyxel.text(x, y, text, 13)

    def _center_text(self, text: str, y: int, color: int, x: int | None = None, width: int | None = None) -> None:
        area_x = 0 if x is None else x
        area_w = self.width if width is None else width
        pyxel.text(area_x + max(0, (area_w - len(text) * 4) // 2), y, text, color)


BootstrapApp()
