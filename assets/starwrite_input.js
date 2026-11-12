// SDL tracks the first touch ID until its end/cancel arrives. If a browser
// loses that notification, later IDs never become mouse presses in Pyxel.
// Reconcile against the browser's current touch list, never a time limit.
window.starwriteInputCancelSequence = 0;
const starwriteForwardedTouches = new Map();
let starwriteSendingCancel = false;

function starwriteCanvasTouch(touch) {
  return touch.target && touch.target.id === "canvas";
}

function starwriteCancelTouches(touches, remaining = []) {
  if (!touches.length) return false;
  const byTarget = new Map();
  for (const touch of touches) {
    starwriteForwardedTouches.delete(touch.identifier);
    if (!byTarget.has(touch.target)) byTarget.set(touch.target, []);
    byTarget.get(touch.target).push(touch);
  }
  window.starwriteInputCancelSequence += 1;
  starwriteSendingCancel = true;
  try {
    for (const [target, changedTouches] of byTarget) {
      try {
        target.dispatchEvent(new TouchEvent("touchcancel", {
          bubbles: true,
          cancelable: true,
          touches: remaining,
          targetTouches: remaining.filter((touch) => touch.target === target),
          changedTouches,
        }));
      } catch (_error) {
        // An unsupported TouchEvent constructor must not block real input.
      }
    }
  } finally {
    starwriteSendingCancel = false;
  }
  return true;
}

function starwriteRecoverMissingTouches(event) {
  const remaining = Array.from(event.touches || []);
  const ids = new Set(remaining.map((touch) => touch.identifier));
  const missing = Array.from(starwriteForwardedTouches.values())
    .filter((touch) => !ids.has(touch.identifier));
  if (starwriteCancelTouches(missing, remaining)) {
    window.starwritePinchActive = false;
    window.starwritePinchDelta = 0;
    window.starwritePinchSuppressUntil = 0;
  }
}

function starwriteRememberTouches(event, includeNew = false) {
  for (const touch of Array.from(event.touches || [])) {
    if (starwriteCanvasTouch(touch) &&
        (includeNew || starwriteForwardedTouches.has(touch.identifier))) {
      starwriteForwardedTouches.set(touch.identifier, touch);
    }
  }
}

function starwriteResetTouchInput() {
  const touches = Array.from(starwriteForwardedTouches.values());
  if (!starwriteCancelTouches(touches)) {
    window.starwriteInputCancelSequence += 1;
  }
  window.starwritePinchActive = false;
  window.starwritePinchDelta = 0;
  window.starwritePinchSuppressUntil = 0;
  starwriteLastPinchDistance = 0;
}

      window.starwritePinchDelta = 0;
      window.starwritePinchActive = false;
      window.starwritePinchSuppressUntil = 0;
      let starwriteLastPinchDistance = 0;
      const starwritePinchSuppressMs = 180;

      function starwriteTouchDistance(event) {
        if (!event.touches || event.touches.length < 2) {
          return 0;
        }
        const a = event.touches[0];
        const b = event.touches[1];
        return Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
      }

      function starwriteHandlePinchStart(event) {
        starwriteRecoverMissingTouches(event);
        if (!event.touches || event.touches.length < 2) {
          window.starwritePinchActive = false;
          starwriteRememberTouches(event, true);
          starwriteLastPinchDistance = 0;
          return;
        }
        window.starwritePinchActive = true;
        starwriteLastPinchDistance = starwriteTouchDistance(event);
        if (event.cancelable) {
          event.preventDefault();
        }
        event.stopPropagation();
      }

      function starwriteHandlePinchMove(event) {
        starwriteRememberTouches(event);
        if (!event.touches || event.touches.length < 2) {
          if (window.starwritePinchActive) {
            window.starwritePinchActive = false;
            window.starwritePinchSuppressUntil = Date.now() + starwritePinchSuppressMs;
            if (event.cancelable) {
              event.preventDefault();
            }
            event.stopPropagation();
          } else {
            // SDL synthesizes DOWN for an unknown finger on its first MOVE.
            starwriteRememberTouches(event, true);
          }
          starwriteLastPinchDistance = 0;
          return;
        }
        window.starwritePinchActive = true;
        const distance = starwriteTouchDistance(event);
        if (starwriteLastPinchDistance > 0) {
          window.starwritePinchDelta += distance - starwriteLastPinchDistance;
        }
        starwriteLastPinchDistance = distance;
        if (event.cancelable) {
          event.preventDefault();
        }
        event.stopPropagation();
      }

      function starwriteHandlePinchEnd(event) {
        for (const touch of Array.from(event.changedTouches || [])) {
          starwriteForwardedTouches.delete(touch.identifier);
        }
        if (event.type === "touchcancel" && !starwriteSendingCancel &&
            Array.from(event.changedTouches || []).some(starwriteCanvasTouch)) {
          window.starwriteInputCancelSequence += 1;
        }
        const wasPinching =
          window.starwritePinchActive || Date.now() < window.starwritePinchSuppressUntil;
        if (!event.touches || event.touches.length < 2) {
          if (window.starwritePinchActive) {
            window.starwritePinchSuppressUntil = Date.now() + starwritePinchSuppressMs;
          }
          window.starwritePinchActive = false;
          starwriteLastPinchDistance = 0;
        }
        if (wasPinching) {
          if (event.cancelable) {
            event.preventDefault();
          }
        }
      }

      document.addEventListener("touchstart", starwriteHandlePinchStart, { passive: false, capture: true });
      document.addEventListener("touchmove", starwriteHandlePinchMove, { passive: false, capture: true });
      document.addEventListener("touchend", starwriteHandlePinchEnd, { passive: false, capture: true });
      document.addEventListener("touchcancel", starwriteHandlePinchEnd, { passive: false, capture: true });

window.addEventListener("blur", starwriteResetTouchInput);
window.addEventListener("pagehide", starwriteResetTouchInput);
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") starwriteResetTouchInput();
});
