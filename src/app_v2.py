from __future__ import annotations

import pyxel

if not hasattr(pyxel, "pix") and hasattr(pyxel, "pset"):
    pyxel.pix = pyxel.pset

import app  # noqa: E402,F401
