# Ableton Mixing Playbook

This is the project-level record of mixing and Ableton-control techniques that
were actually used and verified during the bilingual EDM vocal pass. It is an
operating guide, not a promise that a future mix will need the same settings.
The current authoritative project decisions remain in [`GOAL.md`](../GOAL.md).
For the question matrix and token-routing rules, see
[`GEMINI_TARGETED_MIXING_PROTOCOL.md`](GEMINI_TARGETED_MIXING_PROTOCOL.md).

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
- For a static level trim, use `get_track_volume_info` followed by
  `set_track_volume_value`, then read it back. The value is Live's normalized
  mixer parameter, not a dB number; use the returned `str_for_value()` samples
  to document the actual dB mapping. In this set, Track 9 maps `0.85` to
  `0.0 dB` and `0.90` to `+2.0 dB`. `set_arrangement_clip_gain` is a bounded
  fallback only; its available range did not permit the desired +2 dB move.
  This does not replace phrase-specific automation, which remains UI-only and
  unverified until an envelope-write command is available.
- Re-read the mixer after Live recovery or a controlled restart; a saved Set
  can reopen with the prior normalized value even when the ledger says a trim
  was accepted. In this project Track 9 had drifted back to `0.85` after the
  v117 review, so MCP restored `0.90`, saved, and re-rendered v118 before the
  level/dynamics result was accepted.
- If Gemini identifies a dynamic EQ problem but the third-party plugin's
  internal bands are not exposed by the Remote Script, label the boundary
  explicitly. A single existing EQ Eight bell can be used as a reversible
  static proxy A/B, but it must not be described as dynamic processing; keep
  the original value available for immediate revert and require a fresh
  render plus grounded Gemini decision.
- Third-party plugin controls can be exposed with generic parameter names or
  need Live's UI. Treat a UI-only change as unverified until the device is
  visually checked, read back, saved, and rendered.
- `get_arrangement_clips` reports clip `start_time`/`end_time` in beats, not
  seconds. Convert with `seconds = beats * 60 / BPM` before judging whether a
  render is truncated. At 130 BPM, the current 239.435-beat arrangement is
  about 110.5 seconds; the retained 62-bar v60 render is 114.462 seconds
  including its intentional start and tail range.
- The MCP-facing `save_set` tool is the standard save path after an accepted
  change. It uses Live's own `Ctrl+S` only as an internal compatibility bridge
  when the title has a dirty `*`, then verifies the marker clears. A lingering
  marker or Save-As prompt is blocked, not saved. It also clears known stale
  Export Audio/Video and Save Audio File dialogs before sending Ctrl+S, because
  a leftover modal dialog can swallow the save command.
- The reliable render path is Live's Export Audio/Video dialog. For this
  project, retained renders are 24-bit PCM WAV at 44.1 kHz, Normalize Off, and
  No Dither. Keep the exact render range and Main path consistent for A/B work.
  Render Start/Length are segmented Live controls: verify the displayed values
  after every keyboard or mouse edit. If the range drifts, cancel the export
  rather than creating an incomparable candidate.
- The MCP-facing `export_audio` contract is the standard render entry point.
  Ableton's public Live Object Model does not expose an offline render call, so
  the explicitly opt-in Windows bridge drives the application dialog, then
  verifies the exact Main range, WAV/PCM format, output existence, and duration.
  The verified path currently supports 44.1 kHz / 24-bit WAV output in
  Downloads; a shortcut or click without post-render validation is not success.
  In other words, the workflow is MCP-first even though Live's own renderer is
  reached through its application dialog internally. A direct stdio MCP call
  to `export_audio` is a valid verification route when the host client has not
  refreshed its tool catalog. Use a short unique basename in Downloads for the
  actual Live save-dialog operation (for example `mcp-v103.wav`): this Windows
  Common Dialog build can retain a stale long filename internally. The bridge
  refuses overwrite confirmation and fails fast if an old WAV changes while
  the requested output is absent; rename only after the bounce is validated.
- Gemini approval is separate from Ableton MCP dataset consent. For direct
  stdio MCP calls used by this project, set
  `$env:ABLETON_MCP_DISABLE_DATASET='true'` unless the user explicitly opts
  into contributing prompts and device settings to the public training
  dataset. This keeps MCP control, readback, save, and export available without
  silently broadening the data-sharing scope.
- The public Object Model can inspect/clear clip envelopes but does not provide
  a reliable write-automation-points operation. Phrase-specific reverb throws,
  return fades, and riser dips therefore remain UI-only until a tested
  machine-readable command exists; do not substitute a static device change
  and call it automation. If the UI fallback is used, record the exact lane,
  time range, parameter, readback, save state, and fresh bounce.
- On the current Live 12 runtime, `Clip.gain` is a normalized `0.0-1.0` LOM
  property even though this repository's legacy `set_arrangement_clip_gain`
  argument is named `gain_db`. Treat the MCP value as raw normalized gain, not
  dB; use it only for a bounded whole-clip correction, read it back, save, and
  compare a fresh bounce. It is not a substitute for phrase automation.

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

### Instrumental low-mid control

For a synth stack that masks a riser or kick in a drop, inspect the existing
EQ graph first and test one narrow move. The current project retained a Track
2 `320 Hz` bell at `-2.5 dB` after a grounded Gemini review of `01:08-01:13`;
the change improved perceived separation without changing the Master. Keep
this as a candidate decision, not a universal preset: if the low-mid issue is
dynamic, prefer Pro-Q 4/Ozone Dynamic EQ through a verified UI workflow when
their internal bands cannot be controlled by MCP.

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

For this project, a measured `-0.97 dBTP` warning was resolved with a bounded
Master A/B: visually verify `L4 Ultramaximizer Stereo -> Utility`, trim the
Utility output from `-0.50 dB` to `-0.70 dB`, save, and re-render. The retained
v117 audit measured `-1.17 dBTP` with dynamics intact, and Gemini heard no
loss of punch or vocal forwardness. Treat this as a delivery-margin move, not
permission to chase loudness or keep lowering the Master.

## Efficient evidence loop

Do not spend Gemini output describing facts that the session and plugins can
already show. First use MCP and the deterministic audit for track/device state,
readback, LUFS, true peak, correlation, hashes, and A/B differences. Then use
the best installed visual analyzer for the exact question: Pro-Q 4 or Ozone
Dynamic EQ for frequency/masking, soothe2 or Pro-DS for dynamic resonance and
sibilance, Pro-C 2 for gain reduction, and Pro-L 2/Ozone/L4 for limiter behavior.
If a plugin graph is not exposed through MCP, inspect that graph in Live UI and
record the observation; UI is an inspection fallback, not the normal control
path.

Only then ask Gemini a single `--profile taste` question about what metrics
cannot decide: musical comfort, emotional focus, texture, punch, intentionality,
or which level-matched A/B feels more finished. The useful loop is:

`MCP/local metrics -> plugin visual evidence -> targeted Gemini taste -> one MCP change -> same targeted check`

“Best tool” does not mean “most processing.” An existing, already understood
device is often safer than adding a new plugin when the audible change is
small.

## Gemini listening protocol

Use the direct audio-capable route first:

```powershell
python tools\gemini_audio_feedback.py <exact-wav> --project stancsz-381415 --profile compact --focus "one issue"
```

Require `AUDIO_GROUNDING: PASS`, the model/version, the exact file path, and
timestamped observations. Ask for one reversible Ableton action at a time and
ask Gemini to reassess female level, mono/stereo center, translation, and
pleasantness after every candidate. `AUDIO UNAVAILABLE` is not a listening
result: start a new chat, upload the exact file again, and retry once. The
Antigravity CLI is useful for text/image reasoning here but is not an audio
listener in this environment.

Keep Gemini calls token-efficient. The helper's compact profile returns at most
three issues, defaults to `maxOutputTokens=420` and the verified current-route
`thinkingLevel=LOW`, and
automatically reuses a report when the audio SHA, model, focus, profile, and
generation budget all match. Use `--no-cache` only for a deliberate fresh
re-listen. For a local A/B
question, an explicitly created 15--30 second PCM excerpt may be sent with
`--kind excerpt --focus "..."`; never use an excerpt to claim full-mix balance
or release readiness. After the final mix is chosen, make one complete
full-track call with `--profile release` (600 output-token cap) and retain that
report as the release evidence. The workflow spends long output only on the
final decision, not on every intermediate A/B.

When the question is musical rather than measurable, prefer the smaller taste
call:

```powershell
python tools\gemini_audio_feedback.py <exact-wav> --project stancsz-381415 --profile taste --focus "does the drop feel too boomy or intentionally heavy?"
```

It returns only a yes/no or A/B answer, two timestamped reasons, and one action
(`maxOutputTokens=420`, verified `thinkingLevel=LOW`; typical answers use far
fewer). Route spectrum peaks, masking
bands, gain reduction, true peak, loudness, and correlation to the local audit
and the installed Pro-Q 4, soothe2, Pro-L 2, Ozone, or other meters first;
Gemini's job is the human-like taste check, not duplicating a visual analyzer.
Do not ask the single-file helper to compare to an unattached baseline; ask what
the current file feels like. The current 3.7 endpoint rejected
`thinkingLevel=MINIMAL`, so `--thinking-level LOW` is the default route and
`MEDIUM` is reserved for a deliberate final review.

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
