# Starwrite Sky Prototype

Pyxel-based star sky simulator prototype for GitHub Pages.

The v0.1 scope is intentionally small: render a condition-dependent night sky,
look around it, show five major constellations, and keep one local
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
Visible constellations show bold English labels, and the named star closest to
the screen center is highlighted with a red frame and label.

The upper-right controls are always available:

- `TIME`: toggle the time slider
- `MONTH`: toggle the month slider
- `RESET`: reset time and camera view

The current prototype slider uses edge `-` / `+` buttons:

- `TIME`: -/+10 minutes
- `MONTH`: -/+30 days

Dragging a slider knob or track continuously changes the sky:

- `TIME`: up/down maps to about +/-6 hours from the drag start
- `MONTH`: up/down maps to about +/-180 days from the drag start

The bottom `MENU` button opens a display panel for toggling:

- `INFO`: observation information
- `GUIDE`: horizontal guide lines
- `CONST`: constellation lines
- `SLIDER LEFT/RIGHT`: slider side for right- or left-handed use

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
- Or use the included `.github/workflows/pages.yml` workflow.

The deployed root serves `index.html`, which loads Pyxel Web from jsDelivr and
runs `src/app_v2.py`.

## Mobile Display

The browser build detects narrow portrait phones and uses a taller Pyxel
surface for iPhone-style screens:

- Desktop/default: 320 x 240
- iPhone portrait: 256 x 556

The HTML viewport uses `viewport-fit=cover`, `100dvh`, and disabled overscroll
so the Pyxel canvas can fill the available iPhone 16 browser viewport. Apple
lists iPhone 16 at 1179 x 2556 physical pixels; this prototype targets a
lighter logical resolution for practical Pyxel Web performance.

## Data

The prototype includes 22 constellations:

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

The prototype uses two star sources:

- A small hand-entered set of bright named stars with approximate J2000-style
  RA/Dec, visual magnitude, and color-index values derived from commonly
  published astronomical facts.
- A deterministic synthetic faint-star background generated in code for visual
  density. These synthetic stars are not a scientific catalog.

For a production catalog, replace `src/data/stars.py` with a properly licensed
catalog such as HYG Database or Hipparcos-derived data and document the exact
license in this section.

## References

- Pyxel project: https://github.com/kitao/pyxel
- Pyxel Web custom tag article by Pyxel author: https://tkitao.hatenablog.com/entry/2022/10/08/174438
