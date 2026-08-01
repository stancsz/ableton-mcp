---
name: ableton-vocal-edm-processing
description: >-
  Diagnose and smooth harsh, brittle, or artificial vocals in a connected
  Ableton Live set, then make a vocal group sit inside an EDM groove with
  de-essing, tuning, corrective EQ, bus ducking, and optional beat-synced
  chops. Use when a user asks to fix vocal harshness, make vocals smoother or
  less on top of the beat, set up Pro-DS, soften Auto-Tune, remove bright or
  phone-like EQ, or make a vocal bus duck or chop with drums.
---

# Ableton Vocal EDM Processing

Use this skill to turn a vocal chain that feels sharp or pasted on into a
controlled, beat-aware EDM vocal. Work from the real Live session: inspect all
active vocal paths, make small reversible changes, read the devices back, and
separate configured/runtime evidence from audible approval.

The default outcome is a live, unsaved mix change staged for A/B listening.
Never save the Set, bounce audio, or change the master unless the user asks.

## Operating boundaries

- Read the session before editing. Map tracks by name, parent group, clips, and
  device order; do not trust user-facing track numbers or stale element indices.
- Use Ableton MCP for session/track/clip readback and transport. Use the Live UI
  through the Computer Use/node-repl bridge for third-party plugin editors and
  stock-device controls when the MCP write surface cannot set them reliably.
- Refresh the Live accessibility/screenshot state after every UI action. Use
  only element indices from the latest state. If `set_value` reports a read-only
  slider, use a calibrated drag and verify the resulting parameter with MCP.
- Preserve existing mute, solo, routing, automation, and unsaved state. Do not
  edit the master to solve a vocal problem.
- A parameter readback, active meter, or successful transport call proves
  configuration/runtime only. It does not prove smoothness, pumping quality,
  phase safety, or absence of artifacts. Require human A/B listening before
  calling the result approved.

## Workflow

### 1. Inspect the vocal topology

1. Read `get_session_info` and record tempo, transport state, track count, and
   the Live title's unsaved marker.
2. Read `get_track_info` for every lead, backing, alternate, and vocal-group
   candidate. Record device order, device-on state, key parameters, fader/output
   gain, and parent group.
3. Read arrangement clips for the vocal paths. Identify alternating lead clips;
   both paths must be treated if the arrangement switches between them.
4. Read the master chain only to confirm context. Leave it unchanged.

In a typical arrangement, a user-facing track such as `8-6 Vocals` and an
alternate `9-6 Vocals` may feed separate processing paths, while a group such
as `10-Group` contains vocal-only stems. Treat the group as a bus problem and
the lead tracks as a tone/intelligibility problem.

### 2. Diagnose before changing

Look for these concrete failure modes rather than reaching for generic EQ:

| Evidence in the chain | Likely result | First correction |
| --- | --- | --- |
| Auto-Tune Retune Speed at `0 ms`, 100% wet | Hard, robotic pitch movement | Start around `15–25 ms`; use `20 ms` for a clean EDM compromise |
| Pro-DS range around `14 dB`, very low threshold, detector from `2.5 kHz` | Lisping, dull consonants, unstable brightness | Split Band; detector HP around `4.5–6 kHz`, range `6–9 dB`, threshold for roughly `3–6 dB` reduction |
| Bright-vocal EQ boosts around `3–4 kHz` and `15–16 kHz` | Forward bite and brittle air | Reduce boosts before adding another de-esser; keep broad boosts modest |
| EQ Eight output around `+4 dB` or a strong `1–2 kHz` shelf | Vocal appears on top even when tone is acceptable | Trim output and flatten the presence shelf before compressing harder |
| Post-gate Pro-Q preset named `Phone` or similar | Nasal, narrow, pasted vocal | Bypass it and audition the uncolored path |
| Vocal-group Glue has drum sidechain but only `50%` blend, `2:1`, and positive makeup | Ducking is too subtle while the bus remains forward | Make the existing sidechain more authoritative and remove makeup gain |

Do not assume every harsh vocal needs more de-essing. Repeated bright boosts,
hard pitch correction, and bus makeup gain often create the problem together.

### 3. Smooth the lead vocal paths

Apply one controlled change at a time and reread the chain after each change.

#### Tuning

- Keep the correct key/scale and formant behavior already chosen by the user.
- Move `0 ms` Retune Speed to about `20 ms` first. Do not change key, scale, or
  wet/dry without evidence that tuning is the problem.

#### Pro-DS

- Prefer Split Band for a lead vocal when the plugin UI supports it.
- Start with detector high-pass near `5 kHz`, range near `8 dB`, and a threshold
  that catches sibilant peaks without clamping every consonant.
- Use the plugin UI as the source of truth for Split Band. Some MCP mappings
  report a generic `Single Vocal` mode even when Split Band is visibly selected.
- Leave lookahead around `15 ms` unless the consonants clearly need another
  response. Keep the detector low-pass at the plugin default unless there is a
  reason to narrow it.

#### Corrective EQ and gain

- Reduce harsh presence around `2.5–4.5 kHz` with a broad, small cut or by
  removing an existing boost. Avoid a deep static notch unless a resonance is
  confirmed.
- Treat air above `12 kHz` conservatively. A broad boost of about `+1–2 dB` is
  generally enough after de-essing; do not stack a `+6 dB` shelf with another
  bright vocal preset.
- Trim EQ output gain when it is acting as hidden loudness. Level-match before
  deciding whether a tone change helped.
- Bypass a telephone/phone-style post-gate EQ if it is not an intentional
  effect. Keep the original device available for undo/A-B rather than deleting
  it.

### 4. Make the vocal group breathe with the beat

Prefer the existing drum-keyed bus compressor before adding a new effect.

For a vocal group that is already sidechained from the drum group:

1. Confirm the external source by name and tap point. In the reference Set it
   was `5-4 Drums`, `Post FX`.
2. Set external/internal sidechain blend to `100%` so the drum transient drives
   the duck consistently.
3. Use a `4:1` ratio and a fast attack for a clear EDM pump.
4. Set release from tempo and groove. At `130 BPM`, a `~200–230 ms` release is
   an effective eighth-note recovery starting point. Shorten it for a tighter
   chop; lengthen it if the vocal gasps between beats.
5. Lower threshold until the bus ducks audibly on drum hits, usually targeting
   about `3–6 dB` of gain reduction. Do not chase a number without listening;
   drum-group level changes the actual reduction.
6. Set makeup/output gain to `0 dB` while balancing the bus, and use `100%`
   dry/wet for the direct pump. Level-match the group against the bypassed
   version.

This is a rhythmic duck, not a mute. If the vocal disappears, raise the
threshold or reduce the ratio before adding more level downstream.

For literal syllable chops, use a duplicate or parallel vocal path with
tempo-synced Beat Repeat, Auto Pan in volume/gate behavior, or arrangement
volume automation at `1/8` or `1/16` notes. Keep the dry intelligible path
available and audition the chop only after the bus pump works. Do not put a
full-time stutter on the only lead vocal without a human check.

### 5. Verify and hand off

Before reporting completion:

1. Reread every changed track and confirm the final numeric values, device-on
   states, sidechain source/tap, and group membership.
2. Confirm the master device list is unchanged.
3. Start playback through an early lead phrase, an alternate lead phrase, and a
   group-heavy section. Verify active meters and the intended transport state.
4. A/B the processed lead against the prior state at matched level. Listen for
   sibilance, lisps, pitch snapping, pumping timing, lost words, and the vocal's
   relationship to kick/snare.
5. State exactly what was verified. If no post-FX bounce or human listening was
   performed, say so. Do not call a meter or EQ graph an acoustic approval.
6. Leave the Set unsaved unless the user explicitly asks to save it. Tell the
   user to save after approving the A/B.

## Reference result from the current project

The following is a documented example, not a blind preset:

- Main `8-6 Vocals`: Auto-Tune Retune Speed `0 → 20 ms`; Pro-DS threshold
  `-45 → -35.10 dB`, range `14 → 8.19 dB`, detector HP `2.5 → 5.01 kHz`, with
  Split Band selected in the UI; EQ Eight presence shelf `+2.60 → +0.48 dB`;
  EQ output `+4 → +2.06 dB`; Bright Vocal Pro-Q boosts around `3.5 kHz` and
  `15.7 kHz` reduced to approximately `+1.08 dB` and `+1.64 dB`.
- Alternate `9-6 Vocals`: Auto-Tune changed to `20 ms`; the same bright Pro-Q
  boosts were reduced; a post-gate `Phone` Pro-Q was bypassed; its existing
  Pro-DS profile around `-36 dB` threshold, `8 dB` range, and `3.5 kHz`
  detector HP was retained.
- `10-Group`: existing Glue Compressor remained keyed from `5-4 Drums` but was
  changed from threshold `-20 dB`, ratio `2:1`, `+5 dB` output, `50%` sidechain
  mix, and `80%` wet to approximately `-28.3 dB`, `4:1`, `0 dB` output, `100%`
  sidechain mix, and `100%` wet. Attack stayed fast and release stayed at `.2`
  for the 130 BPM groove.

These values made the vocal less brittle and made the vocal group move with the
drums without changing the master. They remain starting points: verify the
actual gain reduction and approve the sound by ear in the target arrangement.
