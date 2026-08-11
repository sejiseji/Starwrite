# Pyxel Star Sky Prototype - Implementation Specification v0.1

This repository implements a Pyxel-based star sky simulator prototype that runs
from static hosting such as GitHub Pages.

The prototype is deliberately limited to the core experience: choose an
observer, choose time, look around the sky, see stars and key constellations,
and keep one local capture state.

## v0.1 Goals

- Specify observer latitude and longitude.
- Specify and animate observation date/time.
- Render a condition-dependent star field.
- Look around the sky with a camera.
- Show stars moving with time and seasonal changes with date.
- Show at least ORI, CYG, CAS, UMA, and SCO constellation lines.
- Select and highlight constellations.
- Detect when the selected constellation is framed well enough to capture.
- Save the latest `SkyCapture` state locally.
- Run from GitHub Pages with no server process.

## Explicitly Out Of Scope

- StarLetter.
- Message input.
- Network communication.
- Backend storage.
- GitHub API persistence.
- User accounts or anonymous user IDs.
- Matching, payments, donation, ads, notifications, moderation, or SNS flows.
- Required GPS.
- Camera photos or real screenshot saving.
- AR.
- Planets, moon, sun, Milky Way, atmospheric scattering, precession, nutation,
  or observatory-grade precision.

## Architecture Boundary

The dependency direction is:

```text
Astronomy Core
  -> Sky Model / Camera
  -> Pyxel Renderer
  -> Application / UI
```

Future work may add:

```text
SkyCapture
  -> StarLetter
  -> Network
```

Astronomy code and rendering code must not depend on StarLetter or networking.
Those features must not be implemented in v0.1.

## Implementation Rules

- Prefer pure functions, dataclasses, small classes, and explicit dependencies.
- Do not introduce DI containers, repositories, event buses, service locators,
  plugin systems, complex factories, unnecessary ABCs, ECS, or async
  infrastructure.
- Keep projection math inside `SkyCamera`.
- Keep astronomy math outside Pyxel renderer code.
- Use timezone-aware datetimes internally.
- Store only local preferences and one latest capture in browser storage.

## Milestones

1. Pure Astronomy Core: `Vec3`, `Observer`, `Star`, Julian Date, sidereal time,
   equatorial to ENU, tests.
2. Camera: `SkyCamera`, camera transform, perspective projection, tests.
3. Static Sky: Pyxel startup, stars, camera movement, horizon filtering.
4. Time Simulation: `SimulationClock`, +/-10 minutes, play/pause, date mode.
5. Constellations: five constellations, lines, selection, highlighting.
6. Capture: frame check, `SkyCapture`, latest local capture.
7. Web Release: static `index.html`, GitHub Pages workflow, README.

## Definition Of Done

- Latitude, longitude, date, and time affect the sky.
- Stars render above the horizon with magnitude differences.
- Camera can look around the sphere.
- Time can step and animate; date mode can step by days.
- Five constellations can be toggled, selected, and captured.
- Latest capture is represented as state, not an image.
- Main astronomy and projection behavior is covered by tests.
- GitHub Pages can serve the prototype without backend infrastructure.
