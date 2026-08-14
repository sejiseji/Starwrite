from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, "src")

import pyxel

if not hasattr(pyxel, "pix") and hasattr(pyxel, "pset"):
    pyxel.pix = pyxel.pset


IPHONE16_SCREEN_HEIGHT = 696
IPHONE16_MIN_SCREEN_WIDTH = 396
IPHONE16_MAX_SCREEN_WIDTH = 430
SMARTPHONE_FIRST_SCREEN_SIZE = (IPHONE16_MIN_SCREEN_WIDTH, IPHONE16_SCREEN_HEIGHT)
SETTINGS_KEY = "starwrite_v02_settings"
IMPORT_DIRS = (
    "src",
    "src/astronomy",
    "src/audio",
    "src/data",
    "src/sky",
    "src/ui",
)
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
COUNTRY_LABELS = {
    "JP": "JAPAN",
    "US": "UNITED STATES",
    "GB": "UNITED KINGDOM",
    "FR": "FRANCE",
    "DE": "GERMANY",
    "FI": "FINLAND",
    "AU": "AUSTRALIA",
    "NZ": "NEW ZEALAND",
    "BR": "BRAZIL",
    "ZA": "SOUTH AFRICA",
    "SG": "SINGAPORE",
    "IN": "INDIA",
    "CA": "CANADA",
    "KR": "SOUTH KOREA",
    "TW": "TAIWAN",
    "TH": "THAILAND",
}
LIST_PAGE_SIZE = 6
INPUT_COOLDOWN_FRAMES = 12
INITIAL_INPUT_LOCK_FRAMES = 24
BOOT_FONT = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01111", "10000", "10000", "10000", "10000", "10000", "01111"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01111", "10000", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "J": ("00111", "00010", "00010", "00010", "10010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "10000", "11110", "00001", "00001", "11110"),
    "6": ("01110", "10000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00001", "01110"),
    "-": ("00000", "00000", "00000", "11111", "00000", "00000", "00000"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "<": ("00010", "00100", "01000", "10000", "01000", "00100", "00010"),
    ">": ("01000", "00100", "00010", "00001", "00010", "00100", "01000"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
}


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


def _prepare_import_layout() -> None:
    cwd = os.getcwd()
    src_path = os.path.join(cwd, "src")
    for path in IMPORT_DIRS:
        try:
            os.makedirs(os.path.join(cwd, path), exist_ok=True)
        except OSError:
            pass
    for path in (src_path, "src", cwd):
        if path not in sys.path:
            sys.path.insert(0, path)


class BootstrapApp:
    def __init__(self) -> None:
        self.width, self.height = _screen_size()
        settings = _load_settings()
        setup_is_complete = bool(settings.get("setup_complete"))
        setup_requested = _setup_requested()
        self.language = settings.get("language") if settings.get("language") in ("ja", "en") else _detect_language()
        default_country = "JP" if self.language == "ja" else "US"
        use_saved_location = setup_is_complete and not setup_requested
        saved_country = settings.get("location_country") if use_saved_location else default_country
        self.country_index = COUNTRIES.index(saved_country) if saved_country in COUNTRIES else COUNTRIES.index(default_country)
        saved_city = settings.get("location_city") if use_saved_location else None
        self.city_index = self._city_index_for(saved_city)
        self.country_page = self.country_index // LIST_PAGE_SIZE
        self.city_page = self.city_index // LIST_PAGE_SIZE
        self.prefetch_files = list(PREFETCH_CORE)
        if self.language == "ja":
            self.prefetch_files.extend(PREFETCH_JA)
        self.prefetch_index = 0
        self.loading_frames = 0
        self.main_app = None
        self.state = "COUNTRY" if setup_requested or not setup_is_complete else "LOADING"
        self.accept_input_frame = INITIAL_INPUT_LOCK_FRAMES
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
        if self.state in ("COUNTRY", "CITY", "CONFIRM"):
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
        if self.state in ("COUNTRY", "CITY", "CONFIRM"):
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
        if pyxel.frame_count < self.accept_input_frame:
            return
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return
        x, y = pyxel.mouse_x, pyxel.mouse_y
        if self._hit(x, y, self._rect("ja")):
            self.language = "ja"
            self._cooldown()
            if PREFETCH_JA[0] not in self.prefetch_files:
                self.prefetch_files.extend(PREFETCH_JA)
        elif self._hit(x, y, self._rect("en")):
            self.language = "en"
            self._cooldown()
        elif self.state == "COUNTRY":
            self._handle_country_input(x, y)
        elif self.state == "CITY":
            self._handle_city_input(x, y)
        elif self.state == "CONFIRM":
            self._handle_confirm_input(x, y)

    def _handle_country_input(self, x: int, y: int) -> None:
        page_count = self._page_count(len(COUNTRIES))
        if self.country_page > 0 and self._hit(x, y, self._rect("page_prev")):
            self.country_page = max(0, self.country_page - 1)
            self._cooldown()
            return
        if self.country_page < page_count - 1 and self._hit(x, y, self._rect("page_next")):
            self.country_page = min(page_count - 1, self.country_page + 1)
            self._cooldown()
            return
        for index, rect in self._list_rects():
            country_index = self.country_page * LIST_PAGE_SIZE + index
            if country_index < len(COUNTRIES) and self._hit(x, y, rect):
                self.country_index = country_index
                self.city_index = 0
                self.city_page = 0
                self.state = "CITY"
                self._cooldown()
                return

    def _handle_city_input(self, x: int, y: int) -> None:
        page_count = self._page_count(len(self.cities))
        if self.city_page > 0 and self._hit(x, y, self._rect("page_prev")):
            self.city_page = max(0, self.city_page - 1)
            self._cooldown()
            return
        if self.city_page < page_count - 1 and self._hit(x, y, self._rect("page_next")):
            self.city_page = min(page_count - 1, self.city_page + 1)
            self._cooldown()
            return
        if self._hit(x, y, self._rect("back")):
            self.state = "COUNTRY"
            self._cooldown()
            return
        for index, rect in self._list_rects():
            city_index = self.city_page * LIST_PAGE_SIZE + index
            if city_index < len(self.cities) and self._hit(x, y, rect):
                self.city_index = city_index
                self.state = "CONFIRM"
                self._cooldown()
                return

    def _handle_confirm_input(self, x: int, y: int) -> None:
        if self._hit(x, y, self._rect("back")):
            self.state = "CITY"
            self._cooldown()
        elif self._hit(x, y, self._rect("start")):
            self._save_selection()
            self.state = "LOADING"
            self.loading_frames = 0

    def _cooldown(self) -> None:
        self.accept_input_frame = pyxel.frame_count + INPUT_COOLDOWN_FRAMES

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
        _prepare_import_layout()
        from app_pyxres_sounds import StarSkyApp

        self.main_app = StarSkyApp(start_pyxel=False)

    def _rect(self, key: str) -> tuple[int, int, int, int]:
        bottom = self.height - 66
        rects = {
            "ja": (12, 78, (self.width - 36) // 2, 44),
            "en": (24 + (self.width - 36) // 2, 78, (self.width - 36) // 2, 44),
            "back": (12, bottom, 112, 48),
            "page_prev": (12, bottom, 136, 48),
            "page_next": (self.width - 148, bottom, 136, 48),
            "start": (self.width - 172, bottom, 160, 48),
        }
        return rects[key]

    def _list_rects(self) -> tuple[tuple[int, tuple[int, int, int, int]], ...]:
        top = 190 if self.state == "CITY" else 154
        height = 54
        gap = 8
        return tuple((index, (12, top + index * (height + gap), self.width - 24, height)) for index in range(LIST_PAGE_SIZE))

    @staticmethod
    def _page_count(count: int) -> int:
        return max(1, (count + LIST_PAGE_SIZE - 1) // LIST_PAGE_SIZE)

    @staticmethod
    def _hit(x: int, y: int, rect: tuple[int, int, int, int]) -> bool:
        rx, ry, rw, rh = rect
        return rx <= x < rx + rw and ry <= y < ry + rh

    def _draw_setup(self) -> None:
        self._center_text("STARWRITE", 18, 7, scale=2)
        self._center_text("NO LOCATION ACCESS", 44, 13)
        self._button(self._rect("ja"), "JA", self.language == "ja", 10, scale=2)
        self._button(self._rect("en"), "EN", self.language == "en", 10, scale=2)
        if self.state == "COUNTRY":
            self._draw_country_list()
        elif self.state == "CITY":
            self._draw_city_list()
        else:
            self._draw_confirm()
        loaded = min(self.prefetch_index, len(self.prefetch_files))
        if loaded < len(self.prefetch_files):
            self._center_text(f"PREP {loaded}/{len(self.prefetch_files)}", self.height - 16, 5)

    def _draw_country_list(self) -> None:
        self._center_text("SELECT COUNTRY", 132, 7, scale=2)
        start = self.country_page * LIST_PAGE_SIZE
        for row, rect in self._list_rects():
            country_index = start + row
            if country_index >= len(COUNTRIES):
                continue
            code = COUNTRIES[country_index]
            label = f"{code}  {COUNTRY_LABELS.get(code, code)}"
            self._button(rect, label, country_index == self.country_index, 7, scale=2)
        self._pager(self.country_page, self._page_count(len(COUNTRIES)))

    def _draw_city_list(self) -> None:
        self._center_text(COUNTRY_LABELS.get(self.country, self.country), 128, 10, scale=2)
        self._center_text("SELECT CITY", 154, 7)
        start = self.city_page * LIST_PAGE_SIZE
        for row, rect in self._list_rects():
            city_index = start + row
            if city_index >= len(self.cities):
                continue
            self._button(rect, self.cities[city_index][0], city_index == self.city_index, 7, scale=2)
        self._button(self._rect("back"), "BACK", False, 7, scale=2)
        self._pager(self.city_page, self._page_count(len(self.cities)))

    def _draw_confirm(self) -> None:
        name, latitude, longitude = self.city
        self._center_text("CONFIRM SKY", 148, 7, scale=2)
        self._center_text(COUNTRY_LABELS.get(self.country, self.country), 224, 10, scale=2)
        self._center_text(name, 258, 7, scale=2)
        self._center_text(f"LAT {latitude:.1f}", 318, 13)
        self._center_text(f"LON {longitude:.1f}", 334, 13)
        self._button(self._rect("back"), "BACK", False, 7, scale=2)
        self._button(self._rect("start"), "START", True, 11, scale=2)

    def _pager(self, page: int, pages: int) -> None:
        if page > 0:
            self._button(self._rect("page_prev"), "< PAGE", False, 7, scale=2)
        if page < pages - 1:
            self._button(self._rect("page_next"), "PAGE >", False, 7, scale=2)
        if pages > 1:
            self._center_text(f"{page + 1}/{pages}", self.height - 34, 13)

    def _draw_loading(self) -> None:
        y = self.height // 2 - 18
        dots = "." * ((pyxel.frame_count // 12) % 4)
        self._center_text("LOADING SKY" + dots, y, 7, scale=2)
        loaded = min(self.prefetch_index, len(self.prefetch_files))
        self._center_text(f"FILES {loaded}/{len(self.prefetch_files)}", y + 30, 13)

    def _draw_stars(self) -> None:
        for index in range(80):
            x = (index * 73 + 19) % self.width
            y = (index * 137 + 31 + pyxel.frame_count // 3) % self.height
            color = 7 if index % 5 else 10
            pyxel.pset(x, y, color)

    def _button(self, rect: tuple[int, int, int, int], label: str, active: bool, color: int, scale: int = 1) -> None:
        x, y, w, h = rect
        pyxel.rect(x, y, w, h, 5 if active else 1)
        pyxel.rectb(x, y, w, h, 10 if active else 13)
        text = self._fit_text(label, w - 12, scale)
        self._center_text(text, y + max(3, (h - 7 * scale) // 2), color, x, w, scale)

    @staticmethod
    def _label(text: str, x: int, y: int) -> None:
        pyxel.text(x, y, text, 13)

    def _center_text(
        self,
        text: str,
        y: int,
        color: int,
        x: int | None = None,
        width: int | None = None,
        scale: int = 1,
    ) -> None:
        area_x = 0 if x is None else x
        area_w = self.width if width is None else width
        draw_x = area_x + max(0, (area_w - self._text_width(text, scale)) // 2)
        self._draw_text(draw_x, y, text, color, scale)

    @staticmethod
    def _fit_text(text: str, max_width: int, scale: int) -> str:
        value = text.upper()
        while len(value) > 1 and BootstrapApp._text_width(value, scale) > max_width:
            value = value[:-1]
        return value

    @staticmethod
    def _text_width(text: str, scale: int) -> int:
        if not text:
            return 0
        return (len(text) * 6 - 1) * scale

    @staticmethod
    def _draw_text(x: int, y: int, text: str, color: int, scale: int) -> None:
        cursor_x = x
        for char in text.upper():
            glyph = BOOT_FONT.get(char, BOOT_FONT[" "])
            for gy, row in enumerate(glyph):
                for gx, bit in enumerate(row):
                    if bit == "1":
                        pyxel.rect(cursor_x + gx * scale, y + gy * scale, scale, scale, color)
            cursor_x += 6 * scale


BootstrapApp()
