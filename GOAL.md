# GOAL.md — EDM Ableton Project: Mastered and Release-Ready

## North star

Finish one EDM track in Ableton Live that keeps its musical identity, survives
level-matched comparison with credible references, translates in stereo and
mono, and is approved by a human listener for release.

“Mastered” means more than a louder master channel. The project must have a
finished arrangement, a controlled mix, a deliberate master, a verified export,
and evidence that the final version still works when it is played quietly,
loudly, in mono, and on more than one playback system.

This is the music-production goal for one Ableton Set. The AbletonMCP code and
the local audit skills are instruments in the workflow; passing a software test
does not mean that the song sounds finished.

## Active production goal — 2026-08-18

Move the current EDM Set from focused vocal/instrumental A/B work to a mature,
production-ready mix and master. “As production-ready as possible” means that
each group is finished for its musical role, the full mix has intentional depth
and movement, and the final master is competitive with level-matched references
without flattening the track. It does not mean chasing a loudness number or
stacking processing because a meter or plugin allows it.

Work in this order, with a comparable full Main-path render after every accepted
stage:

1. **Finish the vocal group bus.** Balance lead, rap, chops, and backing vocals;
   control masking, sibilance, harshness, dynamics, and vocal-group returns;
   preserve intelligibility, character, center stability, and musical contrast
   between verse, hook, and drop. Confirm that group compression/limiting is not
   fighting the Master limiter.
2. **Finish the instrumental group bus.** Resolve kick/bass/sub ownership,
   second-drop impact, synth low-mid buildup, drum transient/body balance,
   upper-mid harshness, and mono translation. Preserve the EDM energy arc while
   keeping the instrumental bus from masking the vocal group or pumping against
   it.
3. **Prepare the overall Master.** Check the pre-master first, then make the
   smallest evidence-backed tonal/dynamic/stereo decisions on the Master. Use
   level-matched references, preserve depth and transients, keep delivery true
   peak at or below `-1 dBTP`, and verify that the final limiter is not doing
   corrective work that belongs on either group.
4. **Polish the full mix, return tracks, and FX.** Refine sends, filtering,
   reverb/delay depth, transitions, automation, tails, stereo width, and the
   relationship between clean electronic elements and textured vocals. The
   result should feel intentional, spacious where it needs to be, punchy in the
   drops, controlled in the verses, and recognizably mature EDM on speakers,
   headphones, earbuds, and mono playback.

 Each stage is complete only after: current device/track state is read; one
 meaningful change (or a clearly bounded batch) is made; Live readback and save
 succeed; the same render range is used; the post-FX/post-Master WAV passes the
 deterministic audit; and the change is retained, reverted, or deferred with a
 recorded reason. AI listening is a second set of ears, not owner approval.
 The overall goal remains open until the final candidate reaches D4 and the
 owner approves the stereo, mono, low-volume, translation, and reference checks.

## Current truth and assumptions

- The repository already contains Ableton session-control, recovery, and
  deterministic mix-audit tooling.
- One structural feedback note was supplied for `maybe edm - fixed.mp3`. It
  explicitly says the audio was not heard, so its points are hypotheses and
  checkpoints—not confirmed defects.
- No Ableton Set, authoritative full-track bounce, or reference track was
  inspected while creating this document.
- Until those inputs are supplied, every mix problem is a hypothesis. Do not
  write a diagnosis as fact from a filename, device list, or generic EDM rule.
- The exact EDM lane, key, tempo, vocal role, release destination, and reference
  tracks remain project decisions. Record them before making irreversible edits.

### Observed Ableton baseline — 2026-08-17

This is live session/configuration evidence from the connected Set, not a claim
about how the audio sounds:

- Live 12 Standard; title `maybe edm - mcp-fixed`; 130 BPM, 4/4; approximately
  284 seconds; transport stopped; nine audio tracks and five return tracks.
- No track was reported muted, soloed, or armed in the baseline read.
- The Master has an enabled L4 Ultramaximizer with a -4 dB threshold, -1 dB
  ceiling, and 16x oversampling, followed by a stereo Utility at 100% width
  with Bass Mono off and output at -6 dB.
- Group track `group` has another enabled L4 at -6 dB threshold; the other
  group also has an enabled L4. This is a routing/serial-limiting risk to test,
  not proof that the mix is over-compressed.
- Relevant named tracks include `2 synth`, `3 bass`, `4 drums`, `5 backing_vocals`,
  `8-6 Vocals`, and `9-6 Vocals`. The vocal chains include Pro-Q 4, soothe2 or
  Auto-Tune Pro, Glue Compressor, Convology XT, Multiband Gate, Utility, and
  Ozone 11 Imager; exact audible impact still requires a bounce and listening.

### Current evidence artifacts — 2026-08-17

- Original Set preserved at `D:\studio\maybeimalright - mowen Project\maybe edm - mcp-fixed.als`.
- Dated checkpoint verified at `C:\Users\stanc\Downloads\maybe-edm-mcp-fixed-checkpoint-2026-08-17 Project\maybe-edm-mcp-fixed-checkpoint-2026-08-17.als`.
- Baseline active-content WAV: `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-trimmed.wav`.
- The corresponding full export is `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17.wav`.
- Baseline SHA-256: `B88FD509076B32DDD7E263CA8C45072ECA95B180BA9A37E40C18CB190855F9F2`.
- Full export SHA-256: `60C0465A5FE6F5BD4D283EB9035499624C337E6299AA66B81F2C066FC86647FE`.
- The active-content file is 24-bit PCM WAV, 44.1 kHz, stereo, 114.115 s. The
  full export is 24-bit PCM WAV, 44.1 kHz, stereo, 241.500 s, with measured
  silence from 108.646 s to the end. The current Live arrangement reports clips
  through 239.435 s, so export trim/arrangement intent remains an open gate.
- Audit artifacts: `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-trimmed.audit.md`, its rerun report, and `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-full.audit.md`.
- Gemini upload completed through the visible attachment flow for the exact baseline WAV after the project-local default-approval policy was recorded. Gemini returned `AUDIO UNAVAILABLE`; the single bounded retry ended in a connection failure. No audio-grounded findings were promoted, and the local status remains `D2 / MIX_RISK_REVIEW`.

## Definition of success

The track is done only when all of the following are true:

1. The arrangement communicates a clear energy arc: intro, build, drop or main
   hook, contrast section, return, and a clean ending appropriate to the track.
2. The kick, bass, and sub have intentional ownership of the low end. The kick
   remains punchy, the bass breathes musically, and the sub does not disappear
   or collapse when the mix is summed to mono.
3. The central hook and any vocal lead are intelligible at low monitoring
   volume without needing excessive brightness, width, or limiting.
4. The mix has no known clipping, accidental mute/solo, broken routing, abrupt
   trims, unwanted noise, audible pumping, harshness, metallic/watery artifacts,
   or phase problems that the final listening pass has rejected.
5. The master is competitive with level-matched references without destroying
   transients, depth, vocal dynamics, or low-end movement.
6. A fresh, lossless, post-FX/post-master bounce has been analyzed and the
   remaining audible gates have been checked by a human.
7. The final export package is reproducible from the saved Set and includes the
   approved master plus any explicitly requested premaster, instrumental,
   vocal-free, or stem deliverables.

## Non-goals

- Do not optimize for a universal LUFS number or make the song loud simply
  because a meter permits it.
- Do not add plugins to hide arrangement, sound-selection, or gain-staging
  problems.
- Do not call a mix professional because an MCP call, screenshot, meter, test,
  or AI response succeeded. Those are evidence about configuration or risk,
  not proof of musical quality.
- Do not change the Master chain during an audit without an explicit decision,
  a saved checkpoint, and a reversible A/B.
- Do not upload audio to Gemini or another external service unless the exact
  file and destination have been authorized at action time.

## Evidence model

Use the local mix-audit vocabulary as the maturity scale:

- **D0 — no reliable render:** no authoritative audio evidence exists.
- **D1 — technically readable:** the supplied WAV decodes and its integrity is
  known.
- **D2 — measurable mix risk:** loudness, dynamics, spectrum, and stereo/mono
  risks have been checked.
- **D3 — contextual comparison:** level-matched references and relevant stems
  have been checked where available.
- **D4 — human-approved:** stereo, mono, translation, and musical listening have
  been completed and the owner accepts the result.

Release approval requires **D4**. A clean deterministic report can move the
project forward, but it cannot replace the final listening decision.

Every important conclusion should identify its evidence source:

`source/path or Live state → observation → hypothesis → test → decision`

Keep deterministic measurements, optional second-set-of-ears notes, and human
listening conclusions in separate sections of the project log.

## Feedback ledger

Transcribe the initial feedback here before changing the Set. Each item must be
specific enough to test and must retain its original timestamp or passage when
one exists.

| ID | Priority | Timestamp/passage | Audible observation | Likely cause | Ableton test/action | Result |
|---|---|---|---|---|---|---|
| F-001 | P1 | Vocal entrances and verse phrases | Vocal may be uneven before heavy processing | Clip-gain inconsistency may be making compression or saturation trigger unevenly | Level phrases before the main vocal chain; compare the same verse before/after | Open / unverified |
| F-002 | P1 | Rap verses versus drops | The beat may swallow the conversational vocal | Instrumental energy may mask the vocal’s 1–3 kHz core | Test small, vocal-triggered ducking on the instrumental bus or dynamic EQ before raising the vocal fader | Open / unverified |
| F-003 | P1 | Verse versus English hook, especially “Tell me where you are” | The lo-fi vocal may lack intentional spatial contrast | The verse and hook may share the same dry/wet field | Keep verses relatively dry, centered, and intimate; reserve wider reverb/delay throws for the English hook | Open / unverified |
| F-004 | P1 | Reverb and delay returns | Effects may wash the stereo field or add mud | Unfiltered returns may carry excessive low-mid energy | High-pass and low-pass the returns; level-match the filtered/unfiltered A/B | Open / unverified |
| F-005 | P1 | Pitched-down vocal duplicate | A dark supporting vocal layer may fight the kick and sub | Unwanted 100–250 Hz energy from the duplicate | Sweep a controlled high-pass on the support layer, then check the full mix and mono sum before choosing a cutoff | Open / unverified |
| F-006 | P0 | Kick/sub passages and first drop | Kick and sub may lose impact or translate inconsistently | Phase relationship or insufficient kick-triggered bass ducking | Run a polarity/phase A/B with an appropriate meter or Utility, then test controlled ducking; verify in stereo, mono, and low-volume playback | Open / unverified |
| F-007 | P2 | Full arrangement | Vocal grit may read as a defect instead of an intentional texture | The vocal’s lo-fi character may not contrast with clean electronic elements | Keep drums, hats, and lead synths crisp and pristine enough to frame the saturated vocal | Open / unverified |

### Feedback provenance

The supplied note is a non-auditory structural review. It did not provide
timestamps, measured frequencies, or confirmed listening observations. Treat the
rows above as a test plan. A later Gemini review is only promoted to an
audio-grounded finding when the exact attachment is visible, Gemini confirms it
heard the audio, and the response contains a timestamped observation rather than
filename- or genre-based advice.

### Gemini audit outcome — 2026-08-17

- Request type: full-track mix review.
- Exact attachment: `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-trimmed.wav`.
- Visible attachment chip was confirmed before sending; destination was
  `gemini.google.com`.
- Gemini response: `AUDIO UNAVAILABLE`.
- One bounded retry was attempted; Gemini then showed a connection failure and
  produced no timestamped listening observations.
- Decision: keep all proposed vocal/mix changes unverified and do not use this
  attempt as evidence that the mix is release-ready.

### Antigravity CLI evaluation — 2026-08-17

- `agy` is installed and reachable at `C:\Users\stanc\AppData\Local\agy\bin\agy.exe`; the live model list includes `gemini-3.7-flash-high`, `gemini-3.7-flash-medium`, and `gemini-3.7-flash-low`.
- A text smoke test succeeded through `agy -p` with JSON output, confirming the
  headless Gemini 3.7 route is live.
- Exact-audio gate: two fresh CLI sessions were given the authorized baseline
  WAV path and `C:\Users\stanc\Downloads` via `--add-dir`. Both returned
  `AUDIO UNAVAILABLE`; neither produced timestamped listening observations.
- `--add-dir` therefore provides workspace access, not proof of multimodal audio
  attachment. Do not add Antigravity CLI as an equivalent audio-review option or
  promote its output to mix evidence unless a future smoke test returns
  `HEARD_AUDIO:` with concrete timestamps.
- Root cause confirmed against Google's current Antigravity Agent documentation:
  the Antigravity agent defaults to Gemini 3.7 Flash, but its supported input
  types are currently text and image only; audio, video, and document inputs are
  explicitly unsupported. This is an agent/wrapper capability boundary, not a
  Gemini 3.7 audio-model limitation. A direct Gemini API audio request remains
  the correct headless route to test next.

### Direct Gemini audio route — 2026-08-17

- The standard route is now the project helper
  `tools/gemini_audio_feedback.py`, using the active authenticated `gcloud`
  account and the Vertex `generateContent` endpoint with `gemini-3.7-flash`.
- A text smoke request succeeded, then a 30-second lossless WAV audio smoke
  request returned `HEARD_AUDIO` with timestamped observations. Response usage
  reported an `AUDIO` prompt modality.
- The exact 114.115-second active-content WAV then returned HTTP 200 from
  `gemini-3.7-flash` with an `AUDIO` prompt modality and timestamped mix notes:
  high-mid harshness in drop vocal chops around 00:46–01:07 and 01:33–01:48;
  male verse boxiness/separation around 00:21–00:41 and 01:07–01:28; drop
  synth/vocal masking around 00:46–01:05; transition clutter around 00:40–00:46
  and 01:28–01:33; and second-drop limiter clutter around 01:33–01:50.
- These are now the first audio-grounded second-set-of-ears findings. They are
  still recommendations to test, not proof that an Ableton change is correct.
- The direct API response reported `trafficType: ON_DEMAND`; do not assume this
  consumes Antigravity subscription quota or is free. Preserve the project,
  model, usage, exact file, and SHA-256 in every revision log.
- Saved report: `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-gemini-direct.audit.md`;
  SHA-256 `8E30033FE4EE0A0AD48CEB4454BDA67D1972F34EED579F38AD433FB115E9B768`.

### WAV versus MP3 upload check — 2026-08-17

- The active-content WAV decodes as 24-bit PCM, 44.1 kHz, stereo, 114.115397 s;
  `ffprobe` and a full MP3 transcode completed without decode errors.
- The full export also decodes as 24-bit PCM, 44.1 kHz, stereo, 241.500 s, but
  contains silence from 108.646 s to the end; it is not the same artifact as the
  active-content file.
- Non-destructive MP3 derivatives were created at
  `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17-trimmed.mp3`;
  and `C:\Users\stanc\Downloads\maybe-edm-mix-baseline-2026-08-17.mp3`; both
  are 44.1 kHz stereo and decode successfully.
- Antigravity Gemini 3.7 returned `AUDIO UNAVAILABLE` for the active-content MP3
  twice and for the full-export MP3 once.
- Gemini browser visibly accepted the active-content MP3 and the full-export MP3.
  Both listening requests remained in `Stop response` state for bounded waits
  without timestamped observations and were stopped manually.
- Decision: no WAV/MP3 corruption is evidenced. The upload/modality path remains
  the blocker, while export trim/arrangement intent is a separate open issue.

### Current P0 inspection — 2026-08-17 latest

- The connected Set currently reports an unsaved title marker and active
  playback; no transport or mix edit was made during the file tests.
- `3 bass` has an enabled Compressor at threshold `-20.0 dB`, ratio `4:1`,
  attack `1.00 ms`, release `30.0 ms`, dry/wet `75%`, and sidechain `On` with
  an 80 Hz high-pass detector. Raw readback is threshold `0.3599999`, ratio
  `0.75`, attack `0.4000000`, release `0.1569926`, dry/wet `0.75`; the
  sidechain source is not exposed by the current read response.
- `4 drums` has no compressor; its visible devices are Multiband Gate and
  Convology XT. This confirms the existing bass compressor is the first
  reversible low-end A/B target, but does not prove audible over-ducking.
- The repository now includes a guarded `set_device_parameter` readback path in
  `AbletonMCP_Remote_Script/__init__.py` and `MCP_Server/server.py`. It has been
  syntax-tested and the project tests pass, but it is not active in the current
  running Remote Script until that script is safely reloaded. No parameter was
  changed or saved.

### Runtime edit-path status — 2026-08-17 latest

- Read-only socket inspection confirmed the connected Set is still the
  unsaved `maybe-edm-mcp-fixed-checkpoint-2026-08-17*` Set. Transport was
  stopped after inspection.
- The currently-loaded Control Surface returned `Unknown command:
  set_device_parameter`. The active User Library copy was identified at
  `C:\Users\stanc\OneDrive\Documents\Ableton\User Library\Remote Scripts\AbletonMCP\__init__.py`.
- A recoverable backup was created before staging the minimal setter and
  main-thread refresh into that installed copy. The installed copy compiles;
  Live must reload the Control Surface before its new command can be tested.
- No device parameter was changed. The first candidate remains the existing
  `3 bass` Compressor release, currently `30.0 ms`, with a controlled test
  toward approximately `80 ms` based on Gemini's full-track kick-weight note.
  Do not guess the normalized value; set it only after reload and require
  readback, a fresh bounce, deterministic audit, and A/B review.

Rules for the ledger:

- Fix the highest-impact confirmed problem first.
- Change one meaningful variable at a time, render the same passage, and
  level-match the A/B before deciding keep, revert, or defer.
- A note such as “sounds muddy” is an observation, not a diagnosis. Test the
  low-mid buildup, arrangement overlap, monitoring condition, and reference
  comparison before choosing EQ.
- “No issue found” means no issue was evidenced in the tested passage; it does
  not prove the whole track is solved.

## Production path

### Phase 0 — Protect the project and establish the baseline

- Save a dated `Save As` copy or checkpoint before substantial work.
- Record the Live Set title, saved/unsaved state, tempo, key or scale if known,
  sample rate, project length, track and group topology, routing, mute/solo/arm
  state, device order, and complete Master chain.
- Choose two or three level-matched references in the same EDM lane. Record why
  each reference is relevant: low end, drop impact, vocal placement, width,
  texture, or loudness.
- Render an authoritative full Main-path WAV before edits. If a premaster is
  available, render it separately from the current post-master version.
- Hash and record the exact audio paths. Never reuse a stale bounce from another
  song, stem, or earlier project state.
- Run the repository’s local analyzer on the supplied WAV. If an input is
  missing, mark the relevant result `unknown`; never turn unknown into pass.

### Phase 1 — Resolve the song before polishing the master

- Define the track’s promise in one sentence: listener, mood, EDM subgenre,
  energy, and the moment the hook pays off.
- Confirm the arrangement has contrast. The drop should earn its impact through
  density, rhythm, register, texture, and/or automation—not only a limiter jump.
- Remove or replace parts that create persistent metallic, watery, chirpy,
  phasey, or otherwise distracting artifacts. Do not spend a master EQ trying
  to repair a source that should be replaced.
- Confirm transitions, fills, risers, impacts, tails, fades, and the final
  ending are intentional. Do not use compression to disguise a missing section
  or an abrupt edit.

### Phase 2 — Build a stable EDM mix

- Gain-stage individual tracks and groups so the Master is not being used as a
  rescue fader. Keep the pre-master clean and dynamically useful.
- Give kick, bass, and sub distinct rhythmic and spectral roles. Use sidechain
  as a musical envelope, starting with a controlled test rather than a preset:
  approximately 2:1–4:1, 10–30 ms attack, 80–150 ms release, and roughly 1–3 dB
  of reduction unless the arrangement calls for more.
- Keep the lowest bass region intentionally centered and check it in mono.
  Widen upper harmonics or supporting layers only when the mono sum keeps the
  hook and low end intact.
- High-pass non-bass elements only as needed; investigate 200–400 Hz buildup,
  400–800 Hz boxiness, 2–5 kHz harshness, and 60–120 Hz kick/bass conflict with
  actual audio and level-matched references rather than applying fixed cuts.
- Use clip gain and automation for uneven performances or sections. Do not
  solve every level problem by adding more bus compression.
- If there is a vocal, check diction, pitch artifacts, sibilance, consonants,
  breath, masking, dry/wet balance, and the vocal stem’s phase independently.
  A healthy full-mix correlation does not prove that a vocal stem is in phase.
- For this project’s lo-fi male vocal direction, treat the vocal as an
  intentional texture only after the fundamentals work: level phrases before
  compression, keep conversational verses centered and relatively dry, and use
  the English hook “Tell me where you are” as a candidate for wider, more
  complex throws. Filter every reverb/delay return before deciding that the
  vocal needs more space.
- If the vocal is dynamically masked, test targeted instrumental ducking around
  its core 1–3 kHz range before pushing the fader. If a pitched-down duplicate
  exists, inspect and high-pass its 100–250 Hz contribution separately.
- Keep group processing purposeful. Watch for serial limiting on a group and
  the Master flattening the same transients twice.

### Phase 3 — Pre-master gate

Before designing a final master, make a clean pre-master version:

- no accidental clipping or hidden limiter used only to create headroom;
- no known bypassed, muted, or left-behind processing that changes the intended
  sound;
- a few dB of usable headroom, commonly around -3 to -6 dB peak as a starting
  point, while following the actual reference and mix behavior;
- kick transient, snare/clap impact, bass movement, hook intelligibility, and
  section contrast still work at low volume;
- the full Main path has been rendered, not inferred from a stem or pre-FX
  device read.

If this gate fails, return to the mix. A master is not the place to repair a
broken arrangement, masked hook, or uncontrolled low end.

### Phase 4 — Build and compare master candidates

Use the smallest chain that solves an evidenced problem. Stock Ableton devices
are the default; use third-party plugins only when they are present, licensed,
and understood in this Set.

Candidate chain, in principle:

1. corrective EQ only when the mix/reference comparison justifies it;
2. optional gentle bus compression or saturation for a clearly audible reason;
3. stereo/mono protection and tonal balance checks;
4. one final limiter with a true-peak ceiling near **-1 dBTP** for delivery.

Create at least two level-matched candidates when loudness is a meaningful
tradeoff:

- **Dynamic candidate:** preserves more punch and movement.
- **EDM loudness candidate:** starts around **-9 to -11 LUFS integrated** only if
  the level-matched A/B keeps kick transients, bass definition, hook clarity,
  and depth. This is a starting range, not a pass/fail requirement.

Keep a safer streaming-oriented candidate near the reference’s normalized
level—often approximately **-14 LUFS integrated**—when it materially improves
translation or preserves the track. Choose by level-matched listening, not by
the larger number.

For every candidate, record limiter gain reduction, ceiling, integrated and
short-term loudness, true peak, crest/dynamics proxy, spectral observations,
and what changed audibly. Watch specifically for squashed vocals, flattened
drums, harsh high mids, boomy/thin low end, and stereo-image damage.

### Phase 5 — Translation and human approval

The owner must listen to the same final bounce in all of these conditions:

- normal stereo monitoring at a sensible level;
- low volume, where balance and hook priority become obvious;
- mono or a Utility mono check, focusing on sub, kick, vocal, and the main hook;
- headphones plus at least one real-world speaker or small playback system;
- level-matched comparison against the chosen references;
- the quiet intro, first build, first drop, densest section, breakdown, final
  drop, and fade/tail.

Write down exact observations. Approval means the owner accepts the remaining
tradeoffs; it does not mean every meter is ideal.

### Phase 6 — Export and archive

- Export the analyzed release candidate as a 24-bit PCM WAV at the project’s
  native 44.1 or 48 kHz sample rate. An AIFF may be kept as an additional
  delivery format, but the repository’s deterministic analyzer requires a WAV
  companion; an AIFF-only final cannot satisfy the audit gate. Do not upsample
  for appearance.
- Use no dither unless reducing bit depth; apply it once at the final reduction.
- Keep the final true peak at or below -1 dBTP as a conservative delivery gate.
- Check start/end trims, fades, tails, silence, file duration, channel count,
  and file naming.
- Preserve the approved premaster, master candidate notes, audit JSON/Markdown,
  reference list, and a dated Set checkpoint.
- Create instrumental, vocal-free, radio edit, or stems only when requested;
  each deliverable gets its own basic decode/trim/peak check.

## Export → deterministic audit → Gemini loop

Repeat this loop for each meaningful revision. It is the default feedback loop
for this project, not a substitute for the owner’s final listening.

1. Save a new dated Ableton checkpoint and export one exact full-track WAV from
   the Main path. Do not silently convert, normalize, or overwrite the source.
2. Record the absolute path, filename, duration, sample rate, channel count,
   export revision, and SHA-256 hash. Keep pre-master and post-master files
   clearly distinct.
3. Run `skills/ableton-mix-audit/scripts/mix_audit.py` on that exact WAV. Attach
   the resulting JSON/Markdown report to the revision log, keeping hard
   technical failures, deterministic warnings, and unknowns separate. Do not
   give Gemini these local metrics in the initial listening request; avoid
   anchoring its ears to the machine’s hypotheses.
4. Prepare one Gemini request for one user-authorized file. Classify it as
   `full-track` or `stem`, and ask for: timestamp → audible observation → likely
   cause → testable Ableton action → confidence. Gemini must say `AUDIO
   UNAVAILABLE` if it did not actually hear the file.
5. Initialize the approved Computer Use path, identify one unique browser
   window from the current window list, and use an observe → one action →
   refresh loop. Verify the visible attachment chip before sending. Immediately
   before the visible Send action, obtain action-time confirmation for that exact
   path and the destination `gemini.google.com`; never automate credentials,
   security codes, CAPTCHA, or a security interstitial, and never use CDP, DOM,
   a terminal, or a hidden upload command for the file picker.
6. Convert only timestamped, audio-grounded observations into new feedback
   ledger rows. Keep generic or ungrounded Gemini text labeled `unverified`.
7. Test one Ableton change at a time, export the same passage/full path again,
   rerun the audit, and level-match the A/B before keeping or reverting it.
8. Stop the loop at D4: the owner has listened in stereo and mono, checked
   translation, and approved the release candidate.

If the exact local path is missing, Gemini is signed out, the attachment chip is
not visible, or an external permission prompt appears, mark the revision blocked
and preserve the evidence. Hand sign-in back to the user and never type their
credentials. If the attachment chip is visible but the response says `AUDIO
UNAVAILABLE`, allow one bounded retry with a clearer listening prompt; if the
retry also fails, mark the review unverified/blocked. Do not guess a
personal-folder path or retry by uploading another file.

## AbletonMCP operating contract

The workflow is:

`Hands inspect/edit → Ears measure → human listens → Hands make one reversible change`

- MCP or the SDK bridge can read and manipulate session structure, devices,
  clips, routing, and transport. It does not hear playback.
- The deterministic analyzer can measure a supplied WAV: integrity, silence,
  sample peak, optional LUFS/true peak, dynamics proxies, spectrum, correlation,
  mono loss, and reference deviation. These are risk measurements, not a quality
  score.
- Extension `render_analyze` is useful for source/track checks but is pre-FX.
  Final-master claims require a fresh bounce of the full post-FX Main path and
  analysis of that bounce.
- If the bridge or Remote Script is unavailable, record the blocker and use
  the safe fallback: export from Live, analyze locally, and keep session edits
  manual or explicitly authorized.
- Never automatically replay a failed state-changing Ableton command. Verify
  the Set state first and preserve the failure record when recovery is external.
- If a second set of ears is used, it must receive the exact authorized audio,
  return timestamped observations, and state `AUDIO UNAVAILABLE` when it did not
  actually hear the file.

## Plugin inventory and selection rule

The current Live browser was scanned on 2026-08-17. Confirmed installed tools
include FabFilter Pro-Q 4, Pro-MB, Pro-DS, Pro-C 2, and Pro-L 2; oeksound
soothe2; iZotope Ozone 11 Dynamic EQ, Spectral Shaper, Maximizer, Low End
Focus, and RX 11 repair tools; Waves Sibilance, Clarity Vx, Silk Vocal, Vocal
Rider, CLA-76, CLA-2A, and L4; plus Melodyne, VocAlign 6 Pro, Auto-Tune Pro,
Audified 1A Equalizer, and MixChecker Ultra.

For every future mix move, inspect the existing chain and this installed
inventory first. Choose the best tool for the audible problem: dynamic/surgical
resonance control with Pro-Q 4, Ozone Dynamic EQ, or soothe2; sibilance with
Pro-DS or Waves Sibilance; vocal leveling with Pro-C 2, CLA-76/CLA-2A, Silk
Vocal, or Vocal Rider; master dynamics with Pro-L 2/Ozone Maximizer/L4; and
artifact repair with RX. Stock Ableton devices remain valid fallbacks, not the
default. Third-party UI-only changes require visual/readback verification and
a fresh bounce before acceptance.

## Acceptance checklist

### Active production stages

- [ ] Vocal group bus is finished: lead/rap/chops/backing balance, intelligibility,
      dynamics, sibilance/harshness, depth, and group-bus limiting are accepted
      in the full mix and do not rely on the Master to sound controlled.
- [ ] Instrumental group bus is finished: kick/bass/sub ownership, drop impact,
      synth masking, drum punch, top-end control, vocal space, and mono
      translation are accepted in the full mix.
- [ ] Pre-master and overall Master are prepared from the accepted group passes;
      level-matched references, true peak, dynamics, limiter behavior, and
      delivery loudness are documented.
- [ ] Return tracks and FX are polished: sends are intentional, returns are
      filtered and depth-appropriate, transitions/tails are clean, and the mix
      has a mature EDM sense of space, impact, and movement.
- [ ] A fresh final post-FX/post-Master render uses the verified authoritative
      range; it is audited, compared, and listened to before release approval.

### Project and evidence

- [x] Dated Save As/checkpoint exists and the original source is preserved.
- [x] Tempo, key/scale, sample rate, arrangement length, routing, track states,
      devices, and Master chain are recorded.
- [x] Initial feedback is transcribed into the ledger with priorities and
      passages.
- [x] Baseline full-track WAV path and hash are recorded.
- [ ] Two or three relevant references are level-matched and recorded.
- [x] Audit report includes no invented values; missing inputs are `unknown`.
- [ ] Every Gemini review has an exact-file path, visible attachment evidence,
      timestamped observations, and an explicit `AUDIO UNAVAILABLE` outcome when
      listening failed.
- [x] Kick/bass attribution, vocal masking, and stem phase findings are marked
      `unknown` when the required stems or full mix are absent; they are never
      inferred from a single unrelated file.

### Music and mix

- [ ] Arrangement and energy arc are intentional before final mastering.
- [ ] Kick/bass/sub relationship works in stereo and mono.
- [ ] Hook and vocal, if present, remain intelligible at low volume.
- [ ] No confirmed P0 issue remains; P1 issues are fixed, accepted, or explicitly
      deferred with a reason.
- [ ] No clipping, broken routing, accidental mute/solo, abrupt trim, or known
      distracting artifact remains in the approved bounce.

### Master and delivery

- [ ] Pre-master was checked before the final limiter was committed.
- [ ] Master candidates were level-matched; loudness was not judged by the
      louder file winning.
- [ ] Final post-master bounce decodes correctly and has no hard technical fail.
- [ ] True peak is at or below -1 dBTP for the delivery candidate.
- [ ] Loudness and dynamics fit the chosen references and preserve the music.
- [ ] Stereo/mono/translation listening is completed by a human.
- [ ] Final WAV and requested alternates are exported, checked, and archived.
- [ ] The owner has explicitly approved the final release candidate.

## First working session inputs

To begin the actual Set work, gather:

1. the exact `.als` path or a user-selected copy;
2. one fresh full-track WAV, preferably both pre-master and current master;
3. the exact local path to the bounce that may be uploaded to Gemini, plus
   confirmation that the destination is authorized;
4. the initial feedback list, with timestamps where possible;
5. two or three reference tracks and the intended EDM lane;
6. the Live edition/version and whether the bridge or legacy Remote Script is
   connected;
7. any required vocal/stem paths and the allowed plugin inventory;
8. the intended delivery (streaming, DJ/club, label demo, or multiple versions).

The first action after these inputs is observation and baseline capture—not
master-chain changes.

## Authoritative current-state update — 2026-08-17

This section supersedes stale earlier notes in this document where they say
that no Set, bounce, or audio-grounded Gemini result exists.

- The dated checkpoint Set has been inspected live: Live 12 Standard, 130 BPM,
  4/4, nine audio tracks, transport stopped, approximately 284 seconds.
- The direct Vertex route returned `AUDIO_GROUNDING: PASS` from
  `gemini-3.7-flash` for the baseline and candidate bounces. The current
  candidate report is
  `C:\Users\stanc\Downloads\maybe-edm-mix-candidate-release-2026-08-17-gemini.audit.md`.
- The live bass test is applied and read back: `3 bass` Compressor Release is
  `82.6 ms` (raw `0.25`).
- The plugin-first vocal revision is applied: hook EQ Eight cuts at
  `4.20 kHz / -3.0 dB` and `6.09 kHz / -3.0 dB`; male-vocal EQ Eight cut at
  `356 Hz / -2.5 dB`. Pro-Q 4 and soothe2 remain in the existing chains; their
  detailed band controls require Live UI verification.
- The Master L4 still reads `-4.0 dB` threshold. The Master-specific setter
  change is not yet active, so the limiter recommendation remains open.
- Candidate bounce:
  `C:\Users\stanc\Downloads\maybe-edm-mix-candidate-release-2026-08-17.wav`;
  24-bit PCM, 44.1 kHz stereo, 106.816 seconds. Local checks pass technical
  headroom, true-peak, trim, spectral, and mono heuristics but warn on low
  dynamics. The candidate Gemini report still flags hook harshness, master
  over-limiting, male-vocal low-mid masking, and kick/sub masking.

### Latest controlled vocal pass â€” 2026-08-17

- The current audible-song candidate is
  `C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v25-vocal-group-off-500hz-cleanup-2026-08-17.wav`.
  It is 24-bit PCM, 44.1 kHz stereo, 110.423 seconds, with SHA-256
  `3f72c53ad8d4d885a68bcfcabfa42ce6a74152b4df19ab8d49b0c84fffa17485`.
- The shared vocal-group L4 is bypassed and read back as `Off`; this removes
  the prior serial âˆ¼7.5 dB vocal-group limiting while retaining the master
  L4. The current vocal EQ pass adds a restrained 500 Hz, Q 1.21, -1.5 dB
  cut on both vocal lanes. The master vocal group is not release-approved;
  this remains an A/B candidate.
- Direct Vertex Gemini returned `AUDIO_GROUNDING: PASS` from
  `gemini-3.7-flash` on the exact current WAV. Gemini confirms the vocal
  chops/stutters and drum transients are working; remaining risks are male
  400â€“800 Hz boxiness/masking, hook 3.5â€“5 kHz harshness plus 8â€“10 kHz
  sibilance, offbeat 50â€“70 Hz bass looseness, and an abrupt outro cutoff.
- The deterministic audit passes sample peak, true peak, dynamics, spectral,
  stereo-correlation, and mono-loss checks, with `D2 / MIX_RISK_REVIEW` and
  only the intentionality warning for 4.09 s leading and 1.02 s trailing
  silence. This is not D4: human translation listening and explicit release
  approval are still required.
- A repeat Gemini listen on the renamed v25 exact path still passes audio
  grounding, but its low-end/master-pumping P0 is inconsistent with the prior
  v22 low-end pass. No further master or bass mutation is being accepted from
  that single variable result; the human vocal-boxiness report remains the
  controlling next-listen signal.

### Canonical current mix state - v37 - 2026-08-17

The strongest retained audible-song candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v37-chop-4260hz-cut-2026-08-17.wav`.
It is 24-bit PCM, 44.1 kHz stereo, 114.115 seconds, SHA-256
`42edcaa4aecfa5dbbfb5e45217393ca3069137c4ab886550d3b9b9e81462a40e`.

- The saved Ableton state leaves the Master unchanged. The male vocal EQ Eight
  correction is 316 Hz / -3.10 dB on track 8 (`9-6 Vocals`). The vocal-chop
  EQ Eight notch is 4.26 kHz / -4.33 dB / Q 4.21 on track 7 (`8-6 Vocals`),
  tightened from -3 dB after Gemini repeatedly identified 3.5-5.5 kHz resonance.
- Exact-file Gemini 3.7 returned `AUDIO_GROUNDING: PASS`. It heard the
  commercial bounce, transient punch, arrangement contrast, and tight vocal
  editing as working. The chop harshness improved from the prior P0 to P1,
  but remains the top audible issue; male 250-400 Hz clouding and kick/sub
  masking remain P1 follow-ups.
- Deterministic v37 audit is `D2 / MIX_RISK_REVIEW`: -4.45 dBTP true peak,
  -16.90 LUFS, 4.0 LU LRA, 15.30 dB crest, 0.857 correlation, and -0.322 dB
  mono loss. The only warning is the intentionality check for 4.09 s leading
  and 4.74 s trailing silence; no vocal stem was supplied, so vocal consistency
  remains unmeasured.
- Export hygiene: v30 and v32-v36 WAVs, matching `.wav.asd` sidecars, and
  generated audit reports were sent to the Windows Recycle Bin after v37 was
  audited. Retained are v37 and its evidence, v22 as the accepted reference,
  the main baseline evidence, and the source project/stems. This is still not
  D4; human translation listening and explicit owner release approval are
  required.

### Latest controlled mix pass — v43 — 2026-08-17

The current retained candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v43-group-l4-off-chop-3750hz-sibilance-7210hz-bass-5870hz-350db-male-316hz-400db-chop-4260hz-500db-2026-08-17.wav`.
It is 24-bit PCM, 44.1 kHz stereo, 114.115 seconds, SHA-256
`1ac71a217e5ddb5f6d1cb90d208b62dcca4917e3391f48c7ab3ced0d44b47bdb`.

- The saved Ableton state leaves the Master chain unchanged. The group L4
  test remains bypassed. The bass EQ is 58.7 Hz / -3.50 dB / Q 3.79, the
  male-vocal EQ is 316 Hz / -4.00 dB with the existing 101 Hz high-pass, and
  the vocal-chop EQ is 3.75 kHz / -2.50 dB plus 4.26 kHz / -5.00 dB / Q 4.21
  plus the existing 7.21 kHz / -3.00 dB cut.
- Exact-file Gemini 3.7 returned `AUDIO_GROUNDING: PASS`. The bass change
  moved low-end masking from v40 P0 to v41-v43 P1. Gemini still hears P1
  pitched-vocal resonance around 3.2-4.5 kHz, male low-mid boxiness/dryness,
  and drop vocal/synth masking. These remain testable mix risks, not release
  approval.
- Deterministic v43 audit is `D2 / MIX_RISK_REVIEW`: -5.04 dBTP true peak,
  -18.88 LUFS, 6.6 LU LRA, 17.33 dB crest, 0.890 correlation, and -0.246 dB
  mono loss. The only deterministic warning is the intentionality check for
  4.09 s leading and 4.74 s trailing silence; no vocal stem was supplied.
- Export hygiene: v37-v42 WAVs, `.wav.asd` sidecars, audit reports, Gemini
  reports, and 80 temporary screenshots were sent to the Windows Recycle Bin.
  Retained are v43 and its evidence, v22 as the accepted reference, baseline
  evidence, and the source project/stems. The source `.als` was not removed.
- Status remains D2 and needs human stereo/mono/translation listening. Do not
  call this release-ready until the owner accepts the candidate at normal and
  low level on headphones/speakers, in mono, and against the intended
  reference.

### Latest validated A/B — v44 retained, v45 rejected — 2026-08-17

The current retained candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v44-soothe-band3-4300hz-bass-5870hz-male-316hz-chop-4260hz-500db-2026-08-17.wav`.
It is 24-bit PCM, 44.1 kHz stereo, 114.115 seconds, SHA-256
`9bb71440c5a5c3cf7e22c9e5e093d2642f162826bd581625401e179ef13999f0`.

- The retained change is the existing soothe2 `band3 freq` moved from `8k9 Hz`
  to `4k3 Hz`, with soothe2 depth `-3.6` and band3 sensitivity `2.9 dB`
  unchanged. Waves Sibilance remains at its prior threshold `-23.3 dB`.
- Fresh Gemini 3.7 returned `AUDIO_GROUNDING: PASS`. It no longer centered its
  top finding on the prior 3.5-5.5 kHz resonance; it now reports a P1 4-7 kHz
  pitched-vocal sibilance issue, plus P1 kick/sub masking and male-vocal
  600 Hz-1.5 kHz masking. These are still hypotheses for human/A-B review.
- Deterministic v44 audit is `D2 / MIX_RISK_REVIEW`: `-5.05 dBTP`, `-18.89
  LUFS`, `6.5 LU LRA`, `17.32 dB crest`, `0.887` correlation, and `-0.253 dB`
  mono loss.
- v45 tested only a lower Sibilance threshold (`-31.7 dB`) and was rejected:
  Gemini escalated the result to a P0 hollow drop/over-compression concern.
  The live project was reverted, saved, and read back to the v44 settings.
- v44 is retained as the current candidate; v43 and v45 plus their sidecars and
  reports were recycled to the Windows Recycle Bin after the A/B decision. The
  source `.als`, v22 reference, baseline evidence, and v44 evidence remain
  retained. Status remains D2, not D4.

### Latest validated A/B — v44 retained, v46 rejected — 2026-08-17

The v46 experiment changed only the bass Compressor Release from the retained
v44 value of `61.8 ms` to `50.0 ms`; attack remained `0.18 ms`, sidechain
remained enabled, and the Master chain was not touched. Direct Gemini 3.7
returned `AUDIO_GROUNDING: PASS` for the exact v46 bounce, but still heard the
drop kick losing definition to sustained synth bass/sub energy around
100–250 Hz (01:35–01:50). The change therefore did not earn retention and was
reverted to `61.8 ms`, saved, and read back in Live.

v46 deterministic metrics were effectively unchanged from v44: `D2 /
MIX_RISK_REVIEW`, `-5.05 dBTP`, `-18.88 LUFS`, `6.6 LU LRA`, `17.31 dB`
crest, `0.888` correlation, and `-0.250 dB` mono loss. The v46 WAV, sidecar,
audit reports, and Gemini report were sent to the Windows Recycle Bin after
the decision. v44 remains the current retained candidate; the open gate is
human stereo/mono/translation listening, with the known remaining risks being
drop kick/sub separation, pitched-chop sibilance, and male-vocal low-mid
boxiness/masking.

### Latest controlled A/B - v50 retained, v47-v49 rejected - 2026-08-17

Three vocal/masking experiments were tested from the saved v44 baseline:

- v47 eased the male EQ Eight 316 Hz cut from `-4.0 dB` to `-2.0 dB`. Gemini
  still heard the male vocal as boxy/tubby and escalated drop-punch risk to P0;
  it was rejected.
- v48 raised the male Convology XT mix from `18%` to `22%`. Gemini still heard
  the same 300-500 Hz boxiness and a P0 limiter-pumping concern; it was
  rejected.
- v49 deepened the synth EQ Eight 390 Hz cut from `-1.5 dB` to `-3.0 dB`.
  Gemini escalated pitched vocal-chop harshness to P0 while male masking
  remained; it was rejected.

The retained v50 change is upstream of the vocal: track 2 (`2 synth`) Utility
Output is `-1.05 dB` (the Live parameter was verified after correcting its
nonlinear dB mapping). The Master chain was not changed. The exact v50 render
is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v50-synth-output-minus105db-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`09eb94a9f4e8de1ee5769cc94d99161d0072d0abc9619a50141c1de3333966ae`.

v50 deterministic audit is `D3 / MIX_RISK_REVIEW`: `-5.11 dBTP`, `-18.92
LUFS`, `6.8 LU LRA`, `17.34 dB` crest, `0.898` correlation, and `-0.229 dB`
mono loss. Fresh Gemini 3.7 returned `AUDIO_GROUNDING: PASS`; it heard solid
kick/sub punch and no P0 drop failure, while retaining P1 risks for pitched
vocal 3.8-6.5 kHz harshness and male 220-350 Hz boxiness. v50 is the current
candidate, not D4 release approval. Human stereo/mono/translation listening
and reference-level comparison remain required.

After the decision, v44 and the v47-v49 WAVs, sidecars, audit reports, Gemini
reports, and temporary screenshots were sent to the Windows Recycle Bin. The
source `.als`, stems, baseline evidence, v22 accepted reference, and v50
evidence remain retained.

### Latest controlled vocal A/B - v50 retained, v51-v52 rejected - 2026-08-17

- v51 increased the retained soothe2 band 3 sensitivity at 4.3 kHz from
  `2.9 dB` to the verified `3.6 dB`. Gemini still heard the same P1 pitched
  vocal harshness and male boxiness, with an added pre-drop dynamics concern;
  the change was reverted.
- v52 moved the male vocal's existing `+1.5 dB` high shelf from `5.00 kHz` to
  `7.84 kHz`. Gemini described the verse as thin, bone-dry, and recessed and
  restored a low-end masking P1; the change was reverted to `5.00 kHz`.

The saved Live state is back to v50: soothe2 band 3 sensitivity `2.9 dB`, male
high shelf `5.00 kHz / +1.5 dB`, synth Utility `-1.05 dB`, and the unchanged
Master chain. v51 and v52 WAVs, sidecars, audits, Gemini reports, and temporary
screenshots were sent to the Recycle Bin. v50 remains the best evidence-backed
candidate; no further automated vocal change is accepted without a human
stereo/mono/translation listen.

### Latest controlled de-essing A/B - v50 retained, v53 rejected - 2026-08-17

v53 changed only Waves Sibilance Stereo Range from `-19.2 dB` to `-21.6 dB`,
leaving the `-23.3 dB` threshold unchanged. Gemini still heard the same P1
pitched-chop harshness and male 350-500 Hz masking, while adding P1
sub-resonance/inconsistent low-end weight. The range was reverted to `-19.2
dB`, the Set was saved, and v53 plus its sidecar, reports, and screenshot were
sent to the Recycle Bin. v50 remains the current candidate.

### Latest validated vocal pass - v55 retained, v54 intermediate - 2026-08-17

The focused Gemini listen on v54 confirmed that enabling the existing track-7
Multiband Dynamics de-esser materially improved the pitched vocal chops,
especially the 7-10 kHz sibilance, without audible pumping. v55 kept that
de-esser and changed only the male track-8 EQ Eight 500 Hz band from `-1.5 dB`
to `-2.5 dB`.

Focused Gemini returned `AUDIO_GROUNDING: PASS` and explicitly heard improved
male-vocal intelligibility without a thin/hollow result. A full-track Gemini
pass initially returned a contradictory P0 chop-sibilance result; a bounded
repeat returned P1 chop harshness instead, consistent with the focused listen.
The disagreement is recorded rather than hidden, and human listening remains
required.

The saved v55 candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v55-male-500hz-minus25db-multiband-deess-synth-minus105db-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`f4dc1b6cd3f81e6849e52887fb77ccd6317f9d1594d39fafb56cbffd05a8cafb`.
Deterministic audit remains `D3 / MIX_RISK_REVIEW`: `-4.98 dBTP`, `-18.89
LUFS`, `6.9 LU LRA`, `17.31 dB` crest, `0.897` correlation, and `-0.229 dB`
mono loss. The Master chain is unchanged. v50 and v54 intermediate exports,
sidecars, audits, focused reports, and screenshots were sent to the Recycle
Bin; v55, baseline, and v22 remain.

### Latest validated male-vocal A/B - v56 retained, v55 superseded - 2026-08-17

The fresh Gemini 3.7 follow-up on v55 still heard 250-350 Hz chestiness in the
male English/Mandarin rap and recommended testing the existing -1.5 dB EQ cut
near 280 Hz. v56 changed only that existing track-8 EQ Eight bell from `434 Hz`
to the verified `282 Hz`; its gain stayed `-1.5 dB`, and the Master and all
other vocal/chop processing stayed unchanged.

Gemini returned `AUDIO_GROUNDING: PASS` and recommended `RETAIN`: it heard
cleaner low-mid chest resonance and improved Mandarin articulation in
`00:18-00:34` and `00:54-01:10`, without thinning, hollowing, or adding phase
artifacts. It also heard unchanged kick/sub impact, chop balance, drop
dynamics, and mono compatibility. Remaining audible risks are the abrupt
outro tail around `01:45-01:50`, smaller pitched-chop sharpness near 5 kHz,
and a possible drop sidechain recovery dip; these are deferred rather than
stacked into this A/B.

The saved v56 candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v56-male-280hz-minus15db-multiband-deess-synth-minus105db-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`C8BB827E35FE9AA4BD52D011B33BDD64FBFE21114489728A4BBAC20706257B8A`.
Deterministic audit remains `D3 / MIX_RISK_REVIEW`: `-4.98 dBTP`, `-18.86
LUFS`, `6.9 LU LRA`, `17.37 dB` crest, `0.897` correlation, and `-0.230 dB`
mono loss. The Set was saved and read back with the EQ at `282 Hz`; the Master
remains `L4 threshold -1.50 dB`, `ceiling -1.00 dB`, `35% stereo link`, and
Utility `-4.50 dB` output. v55 intermediate evidence was recycled after that
decision; v56 was subsequently superseded by v57, while baseline and v22
remain retained references.

### Latest Gemini release review - v56 retained unchanged - 2026-08-17

A second fresh Gemini 3.7 listen focused on the remaining chop and outro
concerns returned `AUDIO_GROUNDING: PASS` and recommended no processing change.
It judged the 4.5-6 kHz pitched-chop energy acceptable and genre-appropriate,
with no piercing fatigue, and judged the tape-stop/filtered ending at
`01:44-01:50` an intentional stylistic finish rather than an export defect.
It also heard solid kick/sub translation, musical sidechain motion, stable
stereo/mono vocal centers, and no need to touch the Master. A longer reverb or
delay tail remains an optional artistic preference, not a required repair.

The v56 candidate was re-audited against the accepted v22 reference. The
reference comparison passed the starting spectral-deviation heuristic; the
only deterministic warning remains the intentionality check for the recorded
leading/trailing silence. This closes the automated mix-change loop for now:
do not stack another EQ, de-esser, or Master change without new human listening
evidence.

### Latest translation A/B - v57 retained, v56 superseded - 2026-08-17

The translation-focused Gemini 3.7 listen on v56 identified the only material
playback-specific risk as a narrow 3.2-3.8 kHz bite on the pitched chops,
especially on phones and earbuds. v57 changed only the existing track-7
Multiband Dynamics `Mid-High Crossover` from `3.50 kHz` to the verified
`3.20 kHz`; the high-band threshold (`-24.0 dB`), ratio (`1:0.57`), attack
(`1 ms`), release (`70 ms`), all other tracks, and the Master were unchanged.

Fresh Gemini returned `AUDIO_GROUNDING: PASS` and recommended `RETAIN`: the
chop resonance was softened across the intro and chorus cycles without
dulling the hook, causing pumping, narrowing the stereo image, or masking the
female lead. It still reports residual male 280-450 Hz weight and possible
drop/top-end issues as separate P1/P2 hypotheses; they are not folded into this
decision.

The saved v57 candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v57-multiband-crossover-3200hz-male-280hz-synth-minus105db-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`BF34F331EBC78FFD61BA5FAF0EDB26B8946BD4C9F26BC7187FBE0670A6C38644`.
Deterministic audit is `D2 / MIX_RISK_REVIEW`: `-5.03 dBTP`, `-18.85 LUFS`,
`6.9 LU LRA`, `17.26 dB` crest, `0.897` correlation, and `-0.230 dB` mono
loss. The Set was saved and read back; v56 intermediate artifacts will be
recycled after the decision, with v57, baseline, and v22 retained.

### Latest male-vocal and chop A/B - v59 retained, v57-v58 superseded - 2026-08-17

The translation pass on v57 still left a small male 280-450 Hz weight, so v58
changed only the existing track-8 EQ Eight 282 Hz bell from `-1.5 dB` to
`-2.0 dB`. Gemini returned `AUDIO_GROUNDING: PASS` and recommended `RETAIN`:
the extra 0.5 dB reduced chestiness without thinning the English/Mandarin rap,
and explicitly warned not to cut the male vocal further.

The remaining chop bite was then tested separately: v59 moved only track-7
Multiband Dynamics `Mid-High Crossover` from `3.20 kHz` to `3.00 kHz`, leaving
the accepted `-24.0 dB` high threshold, `1:0.57` ratio, `1 ms` attack, and
`70 ms` release unchanged. Gemini returned `AUDIO_GROUNDING: PASS` and
recommended `RETAIN`: the 3.0-3.4 kHz resonance was rounded off without dulling
the hook, causing phase artifacts, or reducing brightness, mono focus, or
energy. Remaining observations are minor transition swell, outro percussion
top-end, and backing-vocal depth; none justifies another automated change yet.

The saved v59 candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v59-male-280hz-minus20db-multiband-3000hz-synth-minus105db-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`63D09A0434F13ECD38E9EEEC67A12C47B1C499508E95C71F9E89C9E4FD48BD97`.
Reference comparison passed; deterministic values are `-5.06 dBTP`, `-18.84
LUFS`, `6.9 LU LRA`, `17.27 dB` crest, `0.896` correlation, and `-0.231 dB`
mono loss. The Set was saved and read back; the Master is unchanged. v57 and
v58 intermediate artifacts were recycled after this decision, with v59,
baseline, and v22 retained.

### Latest female-vocal balance A/B - v60 retained, v59 superseded - 2026-08-17

The first explicit female-focused Gemini review confirmed that the female hook,
`8-6 Vocals`, and `5 backing_vocals` are balanced against the male `9-6 Vocals`
rap, with stable center/mono focus and good phone/earbud translation. It did
identify brief approximately 7.5 kHz sibilance spikes on bright playback, so
v60 changed only the existing visible track 8 (`8 6 Vocals female`, historically
`8-6 Vocals`, MCP `track_index=7`) `Sibilance Stereo` threshold from `-23.3 dB`
to `-21.3 dB`;
its `-19.2 dB` range, the rest of the vocal chains, and the Master stayed
unchanged. Visible track 9 (`9 6 Vocals male`, historically `9-6 Vocals`, MCP
`track_index=8`) is the male English/Mandarin rap.

The follow-up Gemini 3.7 A/B returned `AUDIO_GROUNDING: PASS` and recommended
`RETAIN`: the female hook stayed bright and open without lisping, dulling, or
being pushed backward, while the level relationship with the backing vocals and
male rap remained intact. Mono stability and narrow-band translation also
remained clean. Remaining observations are male low-mid chestiness, an outro
sub tail, and a small pre-chorus transition splash; these are deferred rather
than stacked into this vocal change.

The saved v60 candidate is
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v60-female-sibilance-threshold-2026-08-17.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`87CC146B79B8BC913E83B283C52F8BFBEAC07B45461243FD962F25EAAC84AA32`.
Deterministic audit remains `D3 / MIX_RISK_REVIEW`: `-5.03 dBTP`, `-18.85
LUFS`, `6.9 LU LRA`, `17.28 dB` crest, `0.897` correlation, and `-0.230 dB`
mono loss. The Set was saved and read back at the `-21.3 dB` threshold; the
Master remains unchanged. v59 is now the superseded comparison export; keep
only v60, baseline, v22, and the current v60 evidence package.

### Latest release-oriented Gemini review - v60 retained unchanged - 2026-08-17

A fresh Gemini 3.7 release pass returned `AUDIO_GROUNDING: PASS` and
`RETAIN`. It found no P0 or P1 release blocker: the female lead level and
de-essing, male rap intelligibility, backing-vocal depth, kick/sub, dynamics,
stereo/mono center, and phone/earbud translation all passed. It specifically
did not support another male low-mid cut because the male chain already has
overlapping 282/316/356/500 Hz reductions and no remaining boxy or hollow
defect was material enough to justify stacking more EQ.

The report records only optional P2 polish ideas (small percussion ducking,
pre-chorus space automation, a riser notch, and intro chop crossfades). None
is release-blocking or justified without a new focused A/B and human preference
decision. The current visible track map is track 8 `8 6 Vocals female`
(`track_index=7`) and track 9 `9 6 Vocals male` (`track_index=8`); the saved Set
has no unsaved marker and the Master remains unchanged. D4 owner listening is
still required.

The arrangement-boundary check was reconciled: `get_arrangement_clips` returns
times in beats, not seconds. The latest clip boundary `239.435` at 130 BPM is
approximately `110.5` seconds; with the intentional render start and tail, the
retained 62-bar v60 export at `114.462` seconds covers the complete intended
arrangement. No separate full-arrangement replacement render is required.

### Final pleasantness and translation review - v60 retained unchanged - 2026-08-17

The latest exact-file Gemini 3.7 review returned `AUDIO_GROUNDING: PASS` and
`RETAIN`. It heard a cohesive, polished candidate with controlled female
sibilance, clear female/male balance, intelligible Mandarin consonants,
appropriate backing-vocal depth, defined kick/sub interaction, natural
dynamics, stable stereo/mono phase, and smooth phone/earbud translation.

Gemini identified only an optional P2 polish: automate the visible track 8
female `Convology XT` wet mix from `16%` to approximately `17.5%` during
`00:34-00:46` if more pre-chorus bloom is artistically desired. It explicitly
said to leave the mix unchanged otherwise, so no new global wet-mix change was
accepted. The current v60 candidate and saved Live state remain authoritative;
the owner D4 listening gate is still open. Use
[`docs/D4_RELEASE_LISTENING_CHECKLIST.md`](docs/D4_RELEASE_LISTENING_CHECKLIST.md)
for the final owner approval.

### Instrumental EDM review and export boundary - 2026-08-18

The latest direct Gemini 3.7 Flash review of the retained v60 WAV passed
`AUDIO_GROUNDING: PASS` and returned `RETAIN`. It was instructed to ignore
vocal and Master changes and focus on visible tracks 1-5 / MCP indices 1-4
(`1 fx`, `2 synth`, `3 bass`, `4 drums`) plus their groups. Gemini's highest
priority instrumental issue was reduced sub foundation and kick/body impact in
the second drop (`01:49-02:20`), followed by low-mid synth accumulation around
`250-450 Hz`, a pre-drop riser breath, possible upper-mid mono thinning, and
high-hat energy around `9-14 kHz`. It also confirmed that drum transients,
arrangement pacing, vocal-chop placement, and general low-end mono behavior are
working well.

The first reversible A/B proposal used the existing bass `EQ Eight` band 3 at
`58.7 Hz` and changed only its gain from `-3.5 dB` to `-2.0 dB`, preserving the
existing 32 Hz high-pass, bass-mono Utility, sidechain routing, vocals, and
Master. Live readback confirmed the temporary change, but because the bounce
range was not comparable it was reverted; the saved Set and authoritative v60
remain at `3 bass` / `EQ Eight` / `3 Gain A` = `-3.50 dB`.

The first bounce was rejected as incomparable: v61 rendered `110.769 s`, while
the authoritative v60 is `114.462 s` and contains intentional start/tail
silence. No Gemini conclusion or acceptance is attached to v61. The project
must restore and verify the v60 render range before another instrumental A/B.

The MCP-facing `export_audio` contract and `tools/live_export.py` now validate
absolute WAV output, Main-only rendering, PCM format, bar.beat.tick start,
positive length, and optional expected duration. It reports a structured
blocker until a guarded Windows UI bridge can verify Live's segmented fields
and completed output. Ableton's public Live Object Model does not expose a
native offline `Song.export_audio` function, so a shortcut alone must never be
treated as a successful render.

## Done means

The project reaches **D4**, the evidence package is reproducible, the final
master passes the hard technical checks, all material feedback has a recorded
decision, and the owner has listened and approved the release candidate.

Until then, the status is **in progress**, **blocked by missing evidence**, or
**needs human listening**—never “finished” because the limiter, AI, MCP, or
automated report says so.
