const assert = require('node:assert/strict');
const { test } = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../assets/starwrite_input.js'), 'utf8');

function setup({ unsupportedTouchEvent = false } = {}) {
  const listeners = new Map();
  const windowListeners = new Map();
  let now = 1000;
  // The relevant SDL invariant: only the tracked first finger releases the
  // emulated mouse. Later IDs cannot steal it while it is down.
  const mouse = { finger: null, down: false, presses: 0 };
  const cancelled = [];
  let visibilityEvents = 0;
  const document = {
    visibilityState: 'visible',
    dispatchEvent(event) {
      if (event.type === 'visibilitychange') visibilityEvents++;
      for (const fn of listeners.get(event.type) || []) fn(event);
      return true;
    },
    addEventListener(type, fn) {
      if (!listeners.has(type)) listeners.set(type, []);
      listeners.get(type).push(fn);
    },
  };
  const window = {
    addEventListener(type, fn) { windowListeners.set(type, fn); },
  };
  class TouchEvent {
    constructor(type, options) {
      if (unsupportedTouchEvent) throw new Error('TouchEvent unavailable');
      Object.assign(this, options, { type });
    }
    preventDefault() { this.defaultPrevented = true; }
    stopPropagation() { this.stopped = true; }
  }
  const canvas = {
    id: 'canvas',
    dispatchEvent(event) {
      event.target = canvas;
      event.preventDefault ||= function () { this.defaultPrevented = true; };
      event.stopPropagation ||= function () { this.stopped = true; };
      for (const fn of listeners.get(event.type) || []) fn(event);
      if (event.stopped) return;
      if (event.type === 'touchcancel') cancelled.push(event);
      for (const finger of event.changedTouches || []) {
        if ((event.type === 'touchstart' || event.type === 'touchmove') && !mouse.down) {
          mouse.finger = finger.identifier; mouse.down = true; mouse.presses++;
        } else if ((event.type === 'touchend' || event.type === 'touchcancel') && mouse.finger === finger.identifier) {
          mouse.finger = null; mouse.down = false;
        }
      }
    },
  };
  vm.runInNewContext(source, { window, document, TouchEvent, Event, Date: { now: () => now } });
  function touch(identifier, x = 20) { return { identifier, clientX: x, clientY: 20, target: canvas }; }
  function emit(type, touches, changedTouches = touches) {
    canvas.dispatchEvent({ type, touches, targetTouches: touches, changedTouches, cancelable: true });
  }
  return { window, document, mouse, cancelled, touch, emit,
    advance(ms) { now += ms; },
    windowEvent(type) { windowListeners.get(type)({ type }); },
    documentEvent(type) { document.dispatchEvent({ type }); },
    visibility(value) { document.visibilityState = value; document.dispatchEvent({ type: 'visibilitychange' }); },
    get visibilityEvents() { return visibilityEvents; },
  };
}

test('ordinary taps keep one press and release without synthetic cancellation', () => {
  const s = setup(); const a = s.touch(1);
  s.emit('touchstart', [a]); s.emit('touchend', [], [a]);
  assert.deepEqual(s.mouse, { finger: null, down: false, presses: 1 });
  assert.equal(s.cancelled.length, 0);
  assert.equal(s.window.starwriteInputCancelSequence, 0);
});

test('a missing end releases only the vanished ID before the next press', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2);
  s.emit('touchstart', [a]);
  s.emit('touchstart', [b]);
  assert.equal(s.cancelled.length, 1);
  assert.equal(s.cancelled[0].changedTouches.length, 1);
  assert.equal(s.cancelled[0].changedTouches[0], a);
  assert.equal(s.cancelled[0].touches[0], b);
  assert.equal(s.mouse.finger, 2);
  assert.equal(s.mouse.presses, 2);
  assert.equal(s.window.starwriteInputCancelSequence, 1);
  s.emit('touchend', [], [b]);
  assert.equal(s.mouse.down, false);
});

test('a real held finger is not cancelled when another finger starts a pinch', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2, 80);
  s.emit('touchstart', [a]); s.emit('touchstart', [a, b], [b]);
  assert.equal(s.cancelled.length, 0);
  assert.equal(s.mouse.finger, 1);
  assert.equal(s.window.starwritePinchActive, true);
  s.emit('touchmove', [a, s.touch(2, 100)], [b]);
  assert.equal(s.window.starwritePinchDelta, 20);
  s.emit('touchend', [a], [b]); s.emit('touchend', [], [a]);
  assert.equal(s.mouse.down, false);
  assert.equal(s.window.starwritePinchActive, false);
  assert.ok(s.window.starwritePinchSuppressUntil > 1000);
});

test('natural touchcancel clears tracking and notifies Python without recursion', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2);
  s.emit('touchstart', [a]); s.emit('touchcancel', [], [a]);
  assert.equal(s.mouse.down, false);
  assert.equal(s.window.starwriteInputCancelSequence, 1);
  s.emit('touchstart', [b]);
  assert.equal(s.cancelled.length, 1);
  assert.equal(s.mouse.presses, 2);
});

for (const kind of ['blur', 'pagehide', 'hidden']) {
  test(`${kind} releases a held finger and resets pinch state`, () => {
    const s = setup(); const a = s.touch(1), b = s.touch(2);
    s.emit('touchstart', [a]); s.emit('touchstart', [a, b], [b]);
    if (kind === 'hidden') s.visibility('hidden'); else s.windowEvent(kind);
    assert.equal(s.mouse.down, false);
    assert.equal(s.cancelled.length, 1);
    assert.equal(s.window.starwritePinchActive, false);
    assert.equal(s.window.starwritePinchDelta, 0);
    assert.equal(s.window.starwritePinchSuppressUntil, 0);
    const c = s.touch(3); s.emit('touchstart', [c]);
    assert.equal(s.mouse.presses, 2);
  });
}

test('fresh single touch recovers stale pinch without suppressing its first press', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2), c = s.touch(3);
  s.emit('touchstart', [a]); s.emit('touchstart', [a, b], [b]);
  s.emit('touchstart', [c]);
  assert.equal(s.window.starwritePinchActive, false);
  assert.equal(s.window.starwritePinchSuppressUntil, 0);
  assert.equal(s.mouse.finger, 3);
  assert.equal(s.mouse.presses, 2);
});

test('constructor incompatibility does not throw from the real touch handler', () => {
  const s = setup({ unsupportedTouchEvent: true });
  s.emit('touchstart', [s.touch(1)]);
  assert.doesNotThrow(() => s.emit('touchstart', [s.touch(2)]));
  assert.equal(s.window.starwritePinchActive, false);
});

test('touch-action is assigned to the actual runtime surface, not only pyxel-run', () => {
  const css = fs.readFileSync(path.join(__dirname, '../assets/starwrite.css'), 'utf8');
  assert.match(css, /#pyxel-screen,\s*#pyxel-screen canvas#canvas\s*\{[^}]*touch-action:\s*none/s);
});

// SDL also starts mouse emulation for a previously hidden finger on MOVE.
test('the finger remaining after a pinch is tracked when its move reaches SDL', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2), c = s.touch(3);
  s.emit('touchstart', [a]); s.emit('touchstart', [a, b], [b]);
  s.emit('touchend', [b], [a]); s.emit('touchmove', [b], [b]);
  assert.equal(s.mouse.finger, 2);
  s.emit('touchstart', [c]);
  assert.equal(s.cancelled.length, 1);
  assert.equal(s.cancelled[0].changedTouches[0], b);
  assert.equal(s.mouse.finger, 3);
  assert.equal(s.mouse.presses, 3);
});

test('elapsed time alone never cancels a genuinely held finger', () => {
  const s = setup(); const a = s.touch(1), b = s.touch(2);
  s.emit('touchstart', [a]); s.advance(60000);
  s.emit('touchstart', [a, b], [b]);
  assert.equal(s.cancelled.length, 0);
  assert.equal(s.mouse.finger, 1);
});

for (const kind of ['focus', 'pageshow', 'pointerdown', 'touchstart']) {
  test(`${kind} resynchronizes visible SDL state once after a lost return event`, () => {
    const s = setup();
    s.visibility('hidden');
    // Simulate actual state returning to visible without its notification.
    s.document.visibilityState = 'visible';
    const restore = () => {
      if (kind === 'touchstart') s.emit('touchstart', [s.touch(41)]);
      else if (kind === 'pointerdown') s.documentEvent(kind);
      else s.windowEvent(kind);
    };
    restore();
    assert.equal(s.visibilityEvents, 2);
    assert.equal(s.window.starwriteInputCancelSequence, 2);
    if (kind === 'touchstart') {
      assert.equal(s.mouse.down, true);
      assert.equal(s.mouse.presses, 1);
    } else {
      restore();
      assert.equal(s.visibilityEvents, 2);
      assert.equal(s.window.starwriteInputCancelSequence, 2);
    }
  });
}

test('normal visible notification restores without a duplicate synthetic event', () => {
  const s = setup();
  s.visibility('hidden'); s.visibility('visible');
  assert.equal(s.visibilityEvents, 2);
  s.windowEvent('focus'); s.windowEvent('pageshow'); s.documentEvent('pointerdown');
  assert.equal(s.visibilityEvents, 2);
});

test('a focus event while still hidden does not wake the paused app', () => {
  const s = setup();
  s.visibility('hidden'); s.windowEvent('focus'); s.windowEvent('pageshow');
  assert.equal(s.visibilityEvents, 1);
  s.document.visibilityState = 'visible'; s.windowEvent('focus');
  assert.equal(s.visibilityEvents, 2);
});

test('ordinary focus and pointer events do not cancel a live gesture', () => {
  const s = setup();
  s.emit('touchstart', [s.touch(1)]);
  s.windowEvent('focus'); s.windowEvent('pageshow'); s.documentEvent('pointerdown');
  assert.equal(s.visibilityEvents, 0);
  assert.equal(s.cancelled.length, 0);
  assert.equal(s.mouse.down, true);
});

test('repeated background/foreground cycles each recover once', () => {
  const s = setup();
  for (let id = 1; id <= 3; id++) {
    s.emit('touchstart', [s.touch(id)]);
    s.windowEvent('blur'); s.windowEvent('pagehide');
    s.visibility('hidden');
    s.document.visibilityState = 'visible'; s.windowEvent('pageshow');
    assert.equal(s.mouse.down, false);
    assert.equal(s.window.starwritePinchActive, false);
  }
  assert.equal(s.visibilityEvents, 6);
  s.emit('touchstart', [s.touch(4)]);
  assert.equal(s.mouse.presses, 4);
});
