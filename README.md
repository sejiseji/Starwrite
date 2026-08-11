# Starwrite Sky Prototype

Pyxel-based star sky simulator prototype for GitHub Pages.

The v0.1 scope is intentionally small: render a condition-dependent night sky,
look around it, show prototype constellations, and keep one local
`SkyCapture`. StarLetter, networking, backend storage, accounts, planets, moon,
sun, AR, and high-precision astronomy corrections are not implemented.

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
<pyxel-run root="." name="src/app_v2.py"></pyxel-run>
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
- `ENTER`: capture when the selected constellation is framed

Information HUD and guide lines start hidden.
Visible constellations show bold labels in the selected language, and the named
star closest to the screen center is highlighted with a red frame and label.

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

The bottom `MENU` button opens a display panel for toggling:

- `INFO`: observation information
- `GUIDE`: horizontal guide lines
- `CONST`: constellation lines
- `SLIDER LEFT/RIGHT`: slider side for right- or left-handed use
- `LANGUAGE EN/JA`: display language for constellation, named-star, and meteor
  shower labels

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

The deployed root serves `index.html`, which loads Pyxel Web from jsDelivr and
runs `src/app_v2.py`.

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

The prototype includes 25 constellations:

- ORI - Orion
- CYG - Cygnus
- CAS - Cassiopeia
- UMA - Ursa Major
- SCO - Scorpius
- LEO - Leo
- TAU - Taurus
- GEM - Gemini
- CMA - Canis Major
- LYR - Lyra
- AQL - Aquila
- BOO - Bootes
- CRU - Crux
- CEN - Centaurus
- CAR - Carina
- VIR - Virgo
- PEG - Pegasus
- AND - Andromeda
- PER - Perseus
- AUR - Auriga
- DRA - Draco
- CEP - Cepheus
- AQR - Aquarius
- CAP - Capricornus
- UMI - Ursa Minor

The prototype uses two star sources:

- A small hand-entered set of bright named stars with approximate J2000-style
  RA/Dec, visual magnitude, and color-index values derived from commonly
  published astronomical facts.
- A deterministic synthetic faint-star background generated in code for visual
  density. These synthetic stars are not a scientific catalog.

The prototype includes a simple meteor-shower event catalog:

- Years: 2006-2046, centered on 2026 and covering 20 years before/after.
- Recurring showers: 12 major annual showers.
- Total generated events: 492.
- Source label shown in the app menu: IMO.

The meteor-shower data is a v0.1 approximation based on the International
Meteor Organization meteor-shower calendar / working-list style data: shower
names, typical peak dates, approximate radiants, ZHR, and parent bodies are
expanded into one event per shower per year. Meteors are visualized as
simplified streaks radiating from the radiant, not as a physical particle
simulation or exact year-specific forecast.

Japanese labels are rendered inside the Pyxel canvas with a generated bitmap
font atlas in image bank 2. The source text data is generated from the bundled
`assets/starwrite_jp10.bdf` bitmap font, which is a subset of the Pyxel official
example font `umplus_j10r.bdf`. The subset covers the current app labels,
printable ASCII, practical hiragana / katakana code blocks, full-width digits,
full-width Latin letters, and common Japanese punctuation / arithmetic symbols
used by the v0.1 UI. The source font metadata identifies it as `umplus` with
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
- International Meteor Organization, major meteor showers: https://www.imo.net/observations/methods/visual-observation/major/
- International Meteor Organization, meteor shower calendar archive / working list context: https://www.imo.net/resources/calendar/2019/
- IMO / AMS meteor shower calendar: https://newimo.amsmeteors.org/
