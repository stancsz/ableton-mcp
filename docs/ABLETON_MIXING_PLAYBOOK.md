# Ableton Mixing Playbook

This is the project-level record of mixing and Ableton-control techniques that
were actually used and verified during the bilingual EDM vocal pass. It is an
operating guide, not a promise that a future mix will need the same settings.
The current authoritative project decisions remain in [`GOAL.md`](../GOAL.md).

## The repeatable control loop

Use this order for every audible problem:

1. Read `GOAL.md`, the saved Live state, and the current device chain.
2. Identify the audible role and the exact track by returned name, not by a
   stale screenshot or assumed number.
3. Ask Gemini to listen to the exact lossless render and request one ranked,
   testable action.
4. Change one meaningful variable only. Prefer a reversible existing device
   parameter over inserting a new processor.
5. Read the parameter back from Live and verify the saved project state.
6. Render the same Main path with the same settings.
7. Run the deterministic WAV audit and a fresh Gemini A/B listen.
8. Keep, revert, or defer the change based on the new audio evidence.
9. Recycle superseded renders and sidecars after the decision.

Never infer a vocal role from a filename alone, and never call a mix release
ready from meters, a screenshot, or an AI report without the owner's D4
stereo/mono/translation listen.

## Current project track map

The visible Live mixer is one-based; the MCP and legacy Remote Script APIs are
zero-based. In the current project:

| Visible Live track | MCP index | Current returned name | Role |
|---|---:|---|---|
| 7 | 6 | `5 backing_vocals` | backing vocal layers |
| 8 | 7 | `8 6 Vocals female` | female lead/chop bus |
| 9 | 8 | `9 6 Vocals male` | English/Mandarin rap |

The names historically appeared as `8-6 Vocals` and `9-6 Vocals`. Always
read back the name immediately before changing a vocal parameter and record
both the visible number and the MCP index in notes.

## Ableton control and save behavior

- The working project uses the legacy Remote Script socket at
  `127.0.0.1:9877`; the SDK bridge at `127.0.0.1:9800` may be unavailable.
- `get_track_info`, `get_master_track_info`, and `get_session_info` are the
  observation boundary. Use `set_device_parameter` only after reading the
  target device and parameter.
- Third-party plugin controls can be exposed with generic parameter names or
  need Live's UI. Treat a UI-only change as unverified until the device is
  visually checked, read back, saved, and rendered.
- `get_arrangement_clips` reports clip `start_time`/`end_time` in beats, not
  seconds. Convert with `seconds = beats * 60 / BPM` before judging whether a
  render is truncated. At 130 BPM, the current 239.435-beat arrangement is
  about 110.5 seconds; the retained 62-bar v60 render is 114.462 seconds
  including its intentional start and tail range.
- The reliable save path is Live's own UI (`Ctrl+S`) after the accepted change.
  Confirm the title has no `*` before declaring the checkpoint saved.
- The reliable render path is Live's Export Audio/Video dialog. For this
  project, retained renders are 24-bit PCM WAV at 44.1 kHz, Normalize Off, and
  No Dither. Keep the exact render range and Main path consistent for A/B work.
  Render Start/Length are segmented Live controls: verify the displayed values
  after every keyboard or mouse edit. If the range drifts, cancel the export
  rather than creating an incomparable candidate.
- The MCP-facing `export_audio` contract is available for capability discovery
  and strict validation, but Ableton's public Live Object Model does not expose
  an offline render call. Until the guarded Windows bridge is enabled and can
  verify the dialog fields plus output duration, a structured blocker is safer
  than pretending a keyboard shortcut completed a render.

## Practical vocal techniques learned here

### Low-quality vocal texture

Treat artifacts as a texture only after intelligibility and level are stable.
Use surgical or dynamic control for a real resonance, then add saturation,
space, or chops deliberately. Do not stack broad cuts because a vocal is
generally described as “boxy.”

### Female lead and backing vocals

Check level, center stability, and backing depth separately. If the female
level is already balanced, do not raise the fader to solve a sibilance issue.
For brief bright consonants, a small threshold change on the existing
de-esser can preserve air better than a broad high-frequency EQ cut. Recheck
for lisping, dullness, and whether the vocal has been pushed backward.

### Male conversational English/Mandarin rap

Use clip gain or vocal riding for phrase consistency before more compression.
Low-mid cleanup should be narrow and evidence-driven. In this project the
male chain already contains cuts at approximately 282, 316, 356, and 500 Hz;
another 295 Hz notch is not automatically an improvement and can make the
rap thin or hollow. When the existing cuts overlap, prefer a fresh listen or
leave the remaining warmth as an intentional character.

### Pitched vocal chops

De-ess the high band with fast attack and a controlled release, then test the
mid/high crossover when the audible bite is concentrated around 3–4 kHz. Keep
the hook bright and check mono collapse; a chop fix that dulls or narrows the
female lead is a failed fix.

### Space and depth

Keep conversational verses relatively dry and centered. Reserve wider delay
or reverb throws for hooks, transitions, and backing layers. Filter return
signals before increasing send level. A backing-vocal depth complaint is a
send/space problem only after its level and center placement are confirmed.

## Plugin choice

Inventory the installed plugins before reaching for stock Ableton devices. The
confirmed useful tools in this project include Pro-Q 4, Pro-MB, Pro-DS, Pro-C
2, Pro-L 2, Pro-R 2, Saturn 2, soothe2, Ozone 11 Dynamic EQ/Maximizer, Waves
Sibilance, Silk Vocal, Vocal Rider, CLA-76/CLA-2A, and RX. Choose the tool that
matches the problem:

- dynamic resonance or masking: Pro-Q 4, Pro-MB, Ozone Dynamic EQ, soothe2;
- sibilance: Pro-DS or Waves Sibilance;
- uneven performance: Vocal Rider, Pro-C 2, CLA-76/CLA-2A;
- repair artifacts: RX;
- final limiting: existing L4/Pro-L 2/Ozone Maximizer, only with explicit
  Master approval.

“Best tool” does not mean “most processing.” An existing, already understood
device is often safer than adding a new plugin when the audible change is
small.

## Gemini listening protocol

Use the direct audio-capable route first:

```powershell
python tools\gemini_audio_feedback.py <exact-wav> --project stancsz-381415
```

Require `AUDIO_GROUNDING: PASS`, the model/version, the exact file path, and
timestamped observations. Ask for one reversible Ableton action at a time and
ask Gemini to reassess female level, mono/stereo center, translation, and
pleasantness after every candidate. `AUDIO UNAVAILABLE` is not a listening
result: start a new chat, upload the exact file again, and retry once. The
Antigravity CLI is useful for text/image reasoning here but is not an audio
listener in this environment.

## Evidence and export hygiene

Keep the current candidate, the accepted reference, the deterministic audit,
and the Gemini reports needed to reproduce the decision. Send superseded WAVs,
`.wav.asd` files, temporary screenshots, and superseded reports to the Windows
Recycle Bin after the A/B decision. Never delete source `.als` files or source
stems. Record the candidate hash, format, duration, loudness/true peak,
correlation, mono loss, and the remaining human gates in `GOAL.md`.

## D4 handoff

The automated loop is complete only when the owner listens at normal and low
volume in stereo, folds to mono, checks headphones plus a small speaker/phone,
and compares the candidate level-matched against the accepted reference. Pay
special attention to female hook priority, Mandarin consonants, male/female
section handoff, kick/sub punch, sibilance, vocal depth, transition tails,
width, and any phasey or hollow artifacts.
