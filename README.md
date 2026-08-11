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
- `TAB`: next constellation
- `SHIFT+TAB`: previous constellation
- `F`: frame the selected constellation when it is above the horizon
- `H`: HUD
- `ENTER`: capture when the selected constellation is framed

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
runs `src/app.py`.

## Data

The five required constellations are included:

- ORI - Orion
- CYG - Cygnus
- CAS - Cassiopeia
- UMA - Ursa Major
- SCO - Scorpius

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
