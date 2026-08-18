# Starwrite Sky Prototype

Pyxel-based star sky simulator prototype for GitHub Pages.

The v0.1 scope is intentionally small: render a condition-dependent night sky,
look around it, show prototype constellations, and keep one local
`SkyCapture`. StarLetter, networking, backend storage, accounts, planets, sun,
AR, and high-precision astronomy corrections are not implemented.

## Run Locally

Install dependencies:

```sh
python3 -m pip install ".[dev]"
```

Run the desktop Pyxel app:

```sh
PYTHONPATH=src pyxel run src/app.py
```

Run the browser version from a local static server:

```sh
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

The browser entrypoint uses Pyxel Web custom tags:

```html
<pyxel-run root="." name="src/app_bootstrap.py"></pyxel-run>
```

## Controls

- Mouse drag: yaw / pitch
- Mouse wheel: FOV
- `W` / `A` / `S` / `D`: camera
- `Z` / `X`: FOV
- `UP` / `DOWN`: latitude
- `Q` / `E`: longitude
- `LEFT` / `RIGHT`: +/-10 minutes in `TONIGHT`, +/-1 day in `DATE`
- `SPACE`: play / pause
- `M`: toggle `TONIGHT` / `DATE`
- `C`: constellation lines
- `G`: guide lines
- `TAB`: next constellation
- `SHIFT+TAB`: previous constellation
- `F`: frame the selected constellation when it is above the horizon
- `H`: information HUD
- `ENTER`: capture the current sky view

Information HUD and guide lines start hidden.
Visible constellations show bold labels in the selected language, and the named
star closest to the screen center is highlighted with a red frame and label.
The moon is rendered from the current observation time and location. When it is
near the screen center, a compact `MOON` / `月` focus label shows its
illumination percentage.

The bottom main controls are:

- `LETTER`: open the latest unread letter, or the latest received letter
- `LOG`: open the local exchange log
- `CAPTURE`: save the current sky view and schedule a simulated letter receive

The upper-right controls are always available:

- `TIME`: toggle the time slider
- `DAY`: toggle the date slider
- `EVENT`: toggle the celestial event slider
- `RESET`: reset time and camera view

The current prototype slider uses edge `+` / `-` buttons:

- `TIME`: +/-15 minutes
- `DAY`: +/-1 day
- `EVENT`: next/previous registered event

Dragging a slider knob or track continuously changes the sky:

- `TIME`: up/down maps to about +/-6 hours from the drag start
- `DAY`: up/down maps to about +/-180 days from the drag start
- `EVENT`: tap the upper/lower half to jump to the next/previous event

When the `EVENT` control jumps to a registered meteor shower, the camera also
turns toward the related constellation in the current prototype catalog.

Sky view controls:

- Mouse / one-finger drag: look around
- Mouse wheel / trackpad scroll: zoom
- Two-finger pinch on touch devices: zoom

The `MENU` button opens a display panel for toggling:

- `INFO`: observation information
- `GUIDE`: horizontal guide lines
- `CONST`: constellation lines
- `FEATURE`: common sky-feature guide lines and labels
- `SLIDER LEFT/RIGHT`: slider side for right- or left-handed use
- `LANGUAGE EN/JA`: display language for constellation, named-star, meteor
  shower, and sky-feature labels

## Test

```sh
PYTHONPATH=src python3 -m pytest
```

The tests also run without pytest:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests
```

## GitHub Pages

This project is static. There is no web build step for v0.1.

Two publishing options are supported:

- Enable GitHub Pages from the repository branch/root.

The deployed root serves `index.html`, which loads the vendored Pyxel Web
wrapper from `assets/vendor/pyxel/pyxel.js` and runs
`app_bootstrap.py`. The bootstrap app shows the first Pyxel screen quickly,
handles the initial language/city setup, starts source-file prefetching, and
then hands control to `src/app_pyxres_sounds.py`. Pyxel's wheel, CSS, startup
images, and import hook are vendored with the project to reduce startup fetches
from the Pyxel CDN. Pyodide v314.0.4 runtime files are also vendored under
`assets/vendor/pyodide/v314.0.4/full/`, and `index.html` preloads the main
runtime files while the Pyxel start screen is visible.

## Mobile Display

The browser build detects narrow portrait phones and uses a taller Pyxel
surface for iPhone-style screens:

- Desktop/default: 480 x 360
- iPhone portrait: 396-430 x 696

The HTML viewport uses `viewport-fit=cover`, `100dvh`, and disabled overscroll
so the Pyxel canvas can fill the available iPhone 16 browser viewport. Apple
lists iPhone 16 at 1179 x 2556 physical pixels; this prototype targets a
sharper logical resolution while keeping Pyxel Web performance practical. The
portrait width is adjusted from the browser viewport ratio to avoid thin side
gaps caused by Safari's visible toolbar area.

## Data

The prototype includes all 88 IAU constellation IDs. Constellation boundaries
are IAU-defined, but stick-figure line art is not unique or official. Starwrite
uses a reviewed display profile for consistency:

- Line topology: ConstellationLines by Marc van der Sluys, DOI
  `10.5281/zenodo.10397192`, CC BY 4.0.
- HR-to-HIP crosswalk and endpoint coordinates: HYG Database v4.1 by David Nash
  / Astronexus and contributors, CC BY-SA 4.0.
- Review profile: Starwrite `reviewed_pyxel` constellation figure audit dated
  2026-08-18, aligned to common modern Stellarium / Sky & Telescope-style
  stick figures while keeping dense Pyxel linework readable.
- Runtime line endpoints: 685 constellation-line segments using 694 HIP stars.
- Feature / Asterism overlays such as the Big Dipper, seasonal triangles,
  Pleiades, Hyades, and Southern Cross remain separate from constellation body
  lines.

The prototype uses three star sources:

- A small hand-entered set of bright named stars with approximate J2000-style
  RA/Dec, visual magnitude, and color-index values derived from commonly
  published astronomical facts.
- A compact HYG v4.1 subset containing only the HIP stars required by the
  standardized 88-constellation line profile.
- A deterministic synthetic faint-star background generated in code for visual
  density. These synthetic stars are not a scientific catalog.

The prototype includes a simple meteor-shower event catalog:

- Years: 2006-2046, centered on 2026 and covering 20 years before/after.
- Event stepping uses the selected city's approximate UTC offset so a remote
  city such as Sao Paulo is evaluated against its local peak night, not the
  device's current timezone.

Moon position and phase use a compact low-precision lunar ephemeris in
`src/astronomy/moon.py`. It is intended for Starwrite's visual sky context and
local Capture/Letter matching tags, not observatory-grade measurement.
- Recurring showers: 29 annual showers, including southern-sky and equatorial
  showers used by the EVENT control.
- Meteor-shower generated events: 1189.
- Lunar eclipse events: 59 total/partial eclipses from 2006 through 2046.
- Source label shown in the app menu: IMO/NASA.

The meteor-shower data is a v0.1 approximation based on the International
Meteor Organization meteor-shower calendar / working-list style data: shower
names, typical peak dates, approximate radiants, ZHR, and parent bodies are
expanded into one event per shower per year. Meteors are visualized as
simplified streaks radiating from the radiant, not as a physical particle
simulation or exact year-specific forecast.

The lunar-eclipse data is a v0.1 event catalog derived from NASA's decade
tables of lunar eclipses by Fred Espenak / NASA GSFC. Starwrite includes Total
and Partial eclipses only; Penumbral eclipses are intentionally omitted because
they are subtle visually. NASA's tables list the greatest-eclipse time in TD;
this prototype treats those values as approximate UTC for event navigation and
city-based Moon-above-horizon filtering. Eclipse data acknowledgment:
`Eclipse Predictions by Fred Espenak, NASA's GSFC`.

The prototype also includes a small sky-feature overlay controlled by the
`FEATURE` menu toggle. It uses bright green guide lines and labels for common
observing references:

- Summer Triangle
- Winter Triangle
- Big Dipper
- Spring Arc
- Milky Way, shown as an approximate guide path

The Capture / Letter demo uses local preset letters only. Pressing `CAPTURE`
stores the current sky view as data, matches a preset letter, waits 5-8
seconds, then shows a quiet arrival cut-in. The `LETTER` view restores the
captured sky from data and shows the translated text first, followed by the
original text when it differs. The `LOG` stores up to 100 exchanges in
localStorage using FIFO trimming.

Japanese labels and preset letters are rendered inside the Pyxel canvas with a
generated bitmap font atlas split across Pyxel image banks. The checked-in
source font is `assets/umplus_j10r.bdf`, the Pyxel official example font. The
runtime subset is `assets/starwrite_jp10.bdf` and `src/data/font_jp.py`;
regenerate both after adding Japanese text:

```sh
python3 scripts/build_font_subset.py
```

The generated subset covers the current app labels, printable ASCII, practical
hiragana / katakana code blocks, full-width digits, full-width Latin letters,
common Japanese punctuation / arithmetic symbols, a baseline set of daily-life
kanji for preset letters, and any kanji currently used by preset letters. The
source font metadata identifies it as `umplus` with
copyright `Copyright (C) 2002-2004 COZ`; verify the upstream font license before
reusing it outside this prototype. Full arbitrary Japanese text entry is
reserved for the later StarLetter scope and should use a complete Japanese font
instead of extending this UI subset ad hoc.

For a production catalog, replace `src/data/stars.py` with a properly licensed
catalog such as HYG Database or Hipparcos-derived data and document the exact
license in this section.

## References

- Pyxel project: https://github.com/kitao/pyxel
- Pyxel custom font sample: https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/13_custom_font.py
- Pyxel Web custom tag article by Pyxel author: https://tkitao.hatenablog.com/entry/2022/10/08/174438
- ConstellationLines: https://github.com/MarcvdSluys/ConstellationLines
- ConstellationLines DOI: https://doi.org/10.5281/zenodo.10397192
- HYG Database: https://github.com/astronexus/HYG-Database
- International Meteor Organization, major meteor showers: https://www.imo.net/observations/methods/visual-observation/major/
- International Meteor Organization, meteor shower calendar archive / working list context: https://www.imo.net/resources/calendar/2019/
- IMO / AMS meteor shower calendar: https://newimo.amsmeteors.org/
- NASA lunar eclipses 2001-2010: https://eclipse.gsfc.nasa.gov/LEdecade/LEdecade2001.html
- NASA lunar eclipses 2011-2020: https://eclipse.gsfc.nasa.gov/LEdecade/LEdecade2011.html
- NASA lunar eclipses 2021-2030: https://eclipse.gsfc.nasa.gov/LEdecade/LEdecade2021.html
- NASA lunar eclipses 2031-2040: https://eclipse.gsfc.nasa.gov/LEdecade/LEdecade2031.html
- NASA lunar eclipses 2041-2050: https://eclipse.gsfc.nasa.gov/LEdecade/LEdecade2041.html
