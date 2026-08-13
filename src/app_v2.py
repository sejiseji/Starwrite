from __future__ import annotations

import pyxel

APP_ENTRY_VERSION = "46ac44c-constellation-summaries"

if not hasattr(pyxel, "pix") and hasattr(pyxel, "pset"):
    pyxel.pix = pyxel.pset


def _signal_loading() -> None:
    try:
        from js import CustomEvent, document, window  # type: ignore

        document.body.dataset.starwriteLoading = "1"
        window.dispatchEvent(CustomEvent.new("starwrite-loading"))
    except Exception:
        pass


_signal_loading()

import app  # noqa: E402,F401
