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

### Top production-readiness checklist - current gate

Keep this list at the top of the work. Do not call the song production-ready
until each audio item is either retained with a same-range A/B and Gemini or
human listening result, or explicitly deferred by the owner.

- [ ] **P0 vocal sibilance/harshness:** test the female/lead vocal peaks heard
  around `01:14` and in the choruses, especially `5.5-8 kHz` sibilance and
  narrow `3.5 kHz` bite. Prefer a light dynamic de-esser or dynamic EQ test;
  do not stack another broad static high cut.
- [ ] **P1 vocal masking:** test the male verse around `00:20` against synth and
  bass buildup in `200-500 Hz`. Use a level-matched synth-side A/B (dynamic
  ducking or a small musical cut) and verify that the male Mandarin diction
  improves without thinning the drop.
- [ ] **P2 low-end transition:** test the `00:44` chorus/drop transition for
  sustained sub decay masking the kick. Compare a bounded bass sidechain
  release/ducking A/B at the same Main range.
- [ ] **Dynamics:** verify that chorus punch is not being slightly squashed;
  compare crest/LRA and level-matched stereo listening after the low-end A/Bs.
- [x] **Stereo/mono/depth baseline:** Gemini heard a wide, spacious image,
  acceptable mono compatibility, and coherent wet/dry depth on v143. Recheck
  after any masking or low-end change.
- [ ] **Release handoff:** owner must approve normal-volume, low-volume,
  stereo, mono, headphones, speakers, and earbud translation; confirm final
  reference comparison, saved Set, exact WAV, and no accidental mute/solo.
- [ ] **MCP audit hygiene:** repair the active Remote Script mismatch so group
  and Master readbacks work before relying on automation for the final audit.

Full-song Gemini evidence for this checklist is preserved at
`C:\Users\stanc\Downloads\mcp-v143-full-song-gemini-release.txt`; it is
grounded to the exact v143 WAV and does not replace the owner's final listen.

The first P0 test is rejected: v144 changed Track 8 (`8 6 Vocals female`, MCP
index 7) Sibilance Stereo `Range` from `0.25` to `0.33`. The exact same-range
render was `C:\Users\stanc\Downloads\mcp-v144-female-sibilance-range033-52bar.wav`;
Gemini returned grounded `ANSWER: no`, still hearing piercing 6-8 kHz
sibilance at `00:13` and `00:36`. The parameter was restored to `0.25` and the
Set was saved. Do not repeat this broad Range test; use a real focused dynamic
de-esser or dynamic EQ A/B for the open P0.

The installed FabFilter Pro-DS was located through the Ableton browser, but
the MCP load operation could not insert it onto the hidden vocal child track:
Live returned `The given Track is invisible`. No device was added. The next P0
attempt must first expand/expose the vocal group through a verified UI action
or add a safe MCP capability for hidden child tracks, then read back the chain
before rendering.

The current work is a vocal-only recovery pass after the owner reported that
the mix quality had decreased. Freeze Tracks 1-5, returns, and the Master;
inspect and change only Tracks 8/9. Continue to use a scripted/MCP batch
preflight before any Gemini or UI round-trip; make one bounded vocal batch,
save and read it back through MCP, then use one focused Gemini check and one
exact render. The earlier v139 strict whole-vocal gate remains evidence for the
intentional chop envelope, not permission to stack more processing.

Work in this order, with a comparable full Main-path render after every accepted
vocal stage:

1. **Finish the vocal group bus.** Balance lead, rap, chops, and backing vocals;
   control masking, sibilance, harshness, dynamics, and vocal-group returns;
   preserve intelligibility, character, center stability, and musical contrast
   between verse, hook, and drop. Confirm that group compression/limiting is not
   fighting the Master limiter.
2. **Defer the instrumental group bus.** Resolve kick/bass/sub ownership,
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

### Current vocal-only entry point

The current tranche is limited to Tracks 8/9. The saved state now retains the
v129 male back-half clip correction, Track 8 (`8 6 Vocals female`, MCP index 7)
at approximately `+1 dB`, Track 9 (`9 6 Vocals male`, MCP index 8) at `+2 dB`,
and a new, isolated Track 9 EQ Eight fallback for the Pro-Q band that MCP cannot
write. The current comparable full-mix candidate is v141's verified 52-bar,
96.000-second render; it retains v131's clarity treatment, restores the second
male clip's raw gain to `0.6`, and carries the accepted female soothe2 depth
trim. After reopening the Set, the vocal faders had drifted to 0 dB; v143
restored the evidence-backed Track 8/9 fader values and tightened the existing
isolated male low-mid EQ cut. The v143 exact 52-bar render is now the vocal
follow-up candidate. Instrumental v140/v141 changes remain frozen and are not
being re-evaluated in this pass. The longer 62-bar
range remains useful for silence/tail diagnosis but is not the selected natural
delivery boundary.

The male level question is now settled at the clip level: v129's second male
arrangement clip correction to raw gain `0.6` was retained, and v136 restored
that value after a state-drift check found it had silently returned to `0.4`.
The v141 complete-range A/B is the current full-mix candidate. Do not move the
male fader blindly or stack more compression; future level work must read back
every vocal clip gain before export and use the same exact range.

Vocal-only acceptance order:

1. Verify clip boundaries and phrase-level consistency for Tracks 8/9.
2. Test the smallest level/automation change that keeps Mandarin rap diction
   centered without making the hook or drop jump forward.
3. Review resonance/veil, sibilance, compression/release, and FX returns only
   after level consistency is stable.
4. Run one complete-range export, local dynamics audit, and focused Gemini
   listen; retain, revert, or defer the candidate with exact evidence.

Instrumental A/B work is explicitly deferred until this vocal tranche closes.

### Vocal recovery pass - v143 retained pending owner finish - 2026-08-18

After reopening the saved Set, MCP readback showed both vocal faders at raw
`0.850000` (0 dB), inconsistent with the retained vocal balance: Track 8
female raw `0.874942` (approximately +1 dB) and Track 9 male raw `0.900000`
(approximately +2 dB). MCP restored those values. The existing isolated Track
9 native EQ Eight low-mid bell was tightened from `-1.5 dB / Q proxy 0.3767` to
`-2.5 dB / Q proxy 0.6800`; no female high-frequency cut, instrument, return,
or Master parameter was changed.

The exact Main render is
`C:\Users\stanc\Downloads\mcp-v143-vocal-faders-male-lowmid-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`D16962D4060DD17AF34126BEF05FA9D54BFD6AAB4044A0AE5541975F66151A29`.
The local release audit measured `-14.22 LUFS`, `-1.14 dBTP`, `7.9 LU LRA`,
`0.922855` correlation, and `-0.1708 dB` mono loss. Gemini 3.7 Flash returned
grounded `PASS`: vocal/instrument separation, controlled dynamics, centered
leads, and duet interaction were working. Remaining bounded vocal items are
female 5.5-7 kHz peak harshness and occasional chop micro-clicks; male
low-mid veil is reduced but should not receive another broad EQ cut without
owner listening. This is not D4-approved or release-ready yet.

Historical v118 entry-point record (superseded by the v127 state above):

Start from the retained v118 candidate and its saved Live state. The verified
MCP export range is `1.1.1 / 52.0 bars` (96.000 s), which Gemini confirmed as
the natural musical ending. v61 remains the full-range comparison reference;
v66 is the accepted natural-boundary clip-marker cleanup and v118 supersedes
v117 with the verified male level trim re-read, synth low-mid A/B, and Master
true-peak trim. Keep the remaining decisions conservative and
evidence-backed.
Close or explicitly defer the known remaining instrumental questions (second-drop
sub/kick foundation, `250–450 Hz` synth buildup, pre-drop riser breath,
upper-mid mono stability, and `9–14 kHz` hat energy) before committing a new
overall Master candidate. Name the intended delivery and level-matched
references before deciding what “production-ready” loudness means.

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
positive length, and expected duration. The explicitly opt-in Windows bridge
now drives the verified segmented-field sequence and reports success only
after the WAV is stable and readable. Ableton's public Live Object Model does
not expose a native offline `Song.export_audio` function, so this is an MCP
call with a guarded application-dialog implementation rather than a native
Remote Script render call.

### MCP export bridge smoke and current instrumental baseline - 2026-08-18

The MCP-facing bridge was exercised against the current Live Set with
`ABLETON_MCP_UI_EXPORT=1` and the exact project range `1.1.1 / 62.0 bars`.
It returned `status: exported` and verified Main, 44.1 kHz, 24-bit PCM,
stereo, 114.461542 seconds, and 30,286,604 bytes. The smoke artifact was
`C:\Users\stanc\Downloads\maybe-edm-mcp-export-bridge-smoke-2026-08-18-f.wav`;
its SHA-256 is
`A77A918E8D856ED417910A95CFBF0CB3D932E0702829BD1D498DDDE3253193CB`.
The bridge's current verified scope is Windows, Main-only, 44.1 kHz / 24-bit
WAV, Downloads output, no overwrite, and post-render WAV validation.

Current Live readback after the smoke is stopped playback, 130 BPM, 9 tracks,
unchanged Master, and bass `3 bass` / `EQ Eight` band 3 at 58.7 Hz / -3.50 dB.
The direct local audit of the smoke is `D3 / MIX_RISK_REVIEW`: `-4.89 dBTP`,
`-18.82 LUFS`, `4.6 LU LRA`, `18.78 dB` crest, `0.850` correlation, and
`-0.340 dB` mono loss. The hash and small metric differences versus v60/v60
rebounce show that Live/plugin renders are not byte-identical; no bass change
is being credited from this smoke.

Fresh Gemini 3.7 Flash listening on that exact MCP-generated WAV returned
`AUDIO_GROUNDING: PASS`. It retained kick/sub impact, vocal masking, dynamics,
stereo/mono behavior, hats, and translation. It offered P2 hypotheses for
300-450 Hz synth density and a pre-drop riser tail, while the proposed P1
dead-space/click-tail timestamps extend beyond the 114.462-second file and
conflict with prior v60 release reviews; they are therefore deferred for a
human/export-tail check rather than applied blindly. No instrumental A/B is
accepted yet; the saved mix remains at the v60 bass setting.

### Accepted instrumental bass A/B - v61 retained - 2026-08-18

The single-variable A/B changed only the saved `3 bass` / `EQ Eight` band 3
gain at `58.7 Hz` from `-3.50 dB` to `-2.00 dB`; the 32 Hz high-pass,
120 Hz bass-mono Utility, sidechain routing, vocal tracks, and Master were
unchanged. The MCP Remote Script returned the exact parameter readback, and
the Set was saved with no `*` marker.

The same MCP-facing `export_audio` bridge produced the comparable candidate
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v61-bass-58hz-carve-minus2db-mcp-2026-08-18.wav`,
24-bit PCM, 44.1 kHz stereo, 114.462 seconds, SHA-256
`9B778AA3E8CE7C319D44E42745C4201C71A22C29D52B5935FE3AE20956E23D39`.

Fresh Gemini 3.7 Flash on that exact file returned `AUDIO_GROUNDING: PASS`
and `RETAIN`: it heard more essential 808/sub foundation and warmth through
the verse and Drop 2, with no kick loss, runaway masking, headroom problem,
phase issue, or translation regression. Its remaining P1/P2 observations are
separate vocal-chop resonance/sibilance and minor transient masking; no extra
instrumental processing was stacked into this A/B. The deterministic v61
audit is `D3 / MIX_RISK_REVIEW`: `-5.09 dBTP`, `-18.82 LUFS`, `4.7 LU LRA`,
`18.64 dB` crest, `0.849` correlation, and `-0.342 dB` mono loss. v61 is now
the current mix candidate; v60 remains the comparison reference. D4 owner
stereo/mono/translation listening is still required.

### Accepted natural-boundary and female-vocal A/B - v65 retained - 2026-08-18

Gemini 3.7 Flash first reviewed a narrow `88-108 s` excerpt from the exact v61
WAV and confirmed that the musical phrase and spatial decay finish by about
`96.0 s`; the isolated event near `106 s` is an orphan vocal-stutter artifact.
The MCP-facing bridge then exported v64 at `1.1.1 / 52.0 bars`, exactly
`96.000 s`. Gemini returned `AUDIO_GROUNDING: PASS` and `RETAIN`: the second
drop, final vocal/reverb decay, and musical ending remain intact, while the
long dead-air gap and orphan event are gone.

The one-variable v65 A/B kept that same boundary and changed only Track 8
(`8 6 Vocals female`) `Sibilance Stereo` Range from `-19.2 dB` to `-24.0 dB`.
MCP readback confirmed normalized value `0.50` / display `-24.0 dB`; the Set
was saved with no `*` marker. Gemini returned `AUDIO_GROUNDING: PASS` and
`RETAIN`: female 3.8 kHz / 7.5 kHz edge is smoother without lisping, dullness,
or intelligibility loss, and kick/bass, male vocal, stereo, and ending do not
regress.

Retained candidate:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v65-female-sibilance-range24db-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`4F16DCB0F756360EC653425D9A36C03B85EE683DBC19649DEC75775D2B975DAF`.
The deterministic audit remains conservative: `-17.9 LUFS` integrated,
`-5.0 dBTP` input true peak, `3.7 LU`
LRA; the master ceiling is `-1.0 dBTP` in the delivery-normalization check.
The remaining Gemini observations are P1/P2 mix hypotheses (female bridge
1.3-1.6 kHz, male 250-320 Hz, synth recovery, final-drop air, and a short sub
release); they require another bounded A/B or owner deferral, not blind
stacking. D4 owner stereo/mono/low-volume/translation approval remains open.

### Accepted male-vocal clarity A/B - v67 retained - 2026-08-18

The one-variable v67 A/B kept the verified `1.1.1 / 52.0 bars` / `96.000 s`
range, the v66 final-content marker trim, and the v65 female-vocal setting.
Only visible Track 9 (`9 6 Vocals male`, MCP `track_index=8`) EQ Eight Band 5
Frequency A moved from `291 Hz` to `320 Hz`; its Gain A remained `-2.00 dB`.
MCP readback confirmed both values and the Set was saved with no `*` marker.

Retained candidate:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v67-male-320hz-carve-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`3509AAF6D7FF16D670849FB6DF858E5A0842C7411D23E187AB9B15C016238C64`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.01 dBTP`,
`-17.88 LUFS`, `3.6 LU LRA`, `16.02 dB` crest, `0.865` correlation, and
`-0.304 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS` and `RETAIN`: the 320 Hz
notch de-muddies the male Mandarin/English rap around `0:21-0:38` and
`1:05-1:22` without thinning the chest tone or regressing the female vocal,
low end, stereo cohesion, or natural ending. Its next bounded hypotheses are
male consonant peaks around `3.5 kHz`, a small kick/sub overlap below `60 Hz`,
an `800 Hz` riser buildup, intro chop side-channel energy around `2.5 kHz`,
and a slightly forward clap/snare. They are not accepted edits. D4 owner
stereo/mono/low-volume/translation approval remains open.

### Accepted vocal polish A/Bs - v68, v69, v70 retained - 2026-08-18

Three bounded vocal refinements were tested against the preceding saved
candidate, each with the same MCP export range and a fresh Gemini 3.7 listen.
v68 enabled Track 9 male EQ Eight Band 6 A at `3.50 kHz`, `-1.20 dB`, `Q
2.10`; Gemini returned `AUDIO_GROUNDING: PASS` and `RETAIN`, hearing smoother
Mandarin consonant transients without a diction or presence loss. v69 changed
Track 8 female Sibilance Stereo Range from `-24.0 dB` to `-26.0 dB`; Gemini
returned `PASS / RETAIN`, hearing less 7-9 kHz chop splatter without lisping,
dullness, or loss of lead focus. v70 enabled Track 8 female EQ Eight Band 6 A
at `2.86 kHz`, `-1.20 dB`, `Q 2.78`; Gemini returned `PASS / RETAIN`, hearing
less piercing upper-mid bite in the chops while preserving sustained-lead
intelligibility and the male rap.

Current retained candidate:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v70-female-chop-2860hz-cut-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`E56DD72BE38A657F78B0FE2F58697EC4A80860835602656C8FFAA7D549938CEA`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.03 dBTP`,
`-18.10 LUFS`, `3.7 LU LRA`, `16.13 dB` crest, `0.872` correlation, and
`-0.288 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini's remaining notes are P2: localized female bridge sibilants at
`6.5-7.2 kHz`, a `3.8-4.2 kHz` vocal-stack overlap, mild male `240-280 Hz`
chestiness, a brighter intro-FX transient, and final-hook percussion air.
They remain hypotheses for separate A/Bs or owner deferral; no further change
is stacked into v70. D4 owner stereo/mono/low-volume/translation approval
remains open.

### Accepted mix-balance A/Bs - v71, v72, v73, v74 retained - 2026-08-18

Four further bounded passes were exported through the MCP-facing bridge and
audited by Gemini 3.7. v71 changed Track 8 Sibilance Stereo Threshold from
`-21.3 dB` to `-23.3 dB` while keeping Range at `-26.0 dB`; Gemini returned
`PASS / RETAIN` for the female bridge fricatives without lisping or lost air.
v72 increased existing Track 8 soothe2 Band 1 sensitivity at `331 Hz` from
`4.5 dB` to `6.0 dB`; Gemini returned `PASS / RETAIN` for the female
pre-chorus 250-400 Hz articulation without stripping warmth. v73 changed the
existing Track 2 (`2 synth`) EQ Eight Band 2 A to `320 Hz`, `-1.50 dB`,
`Q 1.83`; Gemini returned `PASS / RETAIN` for clearer female articulation
without losing synth warmth or drop punch. v74 raised the final Track 9 male
Utility Output from `+6.0 dB` to `+7.2 dB`; Gemini returned `PASS / RETAIN`,
hearing stronger verse lyric authority without masking the female lead,
kick/sub, or snare.

Current retained candidate:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v74-male-output72db-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`33941FD13F1282A06C3A79EE1BF9546FC6D0D24E9F0786A28CFAB0188C3D2652`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.05 dBTP`,
`-17.71 LUFS`, `3.9 LU LRA`, `15.84 dB` crest, `0.870` correlation, and
`-0.292 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini's remaining items are now localized P1/P2 hypotheses: a male-to-female
dry/wet transition seam, vocal-chop/hat overlap around `6.5-8.2 kHz`, a small
45-65 Hz kick/sub density issue, a riser low-mid buildup, and a slightly
brisk final tail. The current candidate is stable and the remaining fixes
need automation/returns or a separate explicit A/B; no Master-chain change
has been stacked. D4 owner stereo/mono/low-volume/translation approval
remains open.

### Export-range A/B rejections - v62/v63 - 2026-08-18

Two controlled export-boundary trials used the same saved Set and the same
MCP-facing `export_audio` bridge; only the render length changed. v62 used
`54.0` bars and v63 used `53.0` bars. Gemini 3.7 Flash returned
`AUDIO_GROUNDING: PASS` for both exact WAVs and rejected both: v62 cut into the
second drop, while v63 hard-cut the active drop at approximately `01:36` and
omitted the outro. These are export-range failures, not evidence against the
accepted v61 mix, the later v65 boundary, or MCP export reliability.

v61 remains the retained full-range comparison reference; v74 was the current
release candidate. The v62/v63 WAVs,
Ableton sidecars, and Gemini reports are superseded temporary evidence and
were sent to the Windows Recycle Bin after their decisions. The separate tail
diagnostic confirmed a real silent gap plus a residual vocal-chop artifact in
the source arrangement; the v65 delivery range removes both audibly. A later
clip-level cleanup may still improve the Set itself, but it is not being
substituted for the verified v67 delivery candidate.

Superseded smoke WAVs, their sidecars/audits/Gemini report, the manual export
smoke, the v60 rebounce, and this turn's temporary screenshots were sent to
the Windows Recycle Bin. The then-current v74 evidence package, v61 comparison,
baseline, and source project remain retained.

### Accepted instrumental polish A/Bs - v75 through v79 retained - 2026-08-18

The next five changes were each isolated, MCP-read-back, exported through the
MCP-facing `export_audio` bridge, and sent to Gemini 3.7 Flash as a fresh exact
file. v75 inserted a native EQ Eight on Track 5 (`4 drums`) and cut Band 2 A at
`9.50 kHz` by `-1.00 dB`, Q `2.10`; Gemini returned `AUDIO_GROUNDING: PASS /
RETAIN`, hearing less cymbal hash and better vocal-chop separation without
losing drum punch. v76 retuned the existing Track 8 female Band 7 A to `3.80
kHz`, `-1.20 dB`, Q `2.50`; Gemini returned `PASS / RETAIN`, hearing restored
consonant bite and articulation without a harsh clash. v77 changed the existing
Track 9 male Band 2 A to `250 Hz`, `-1.50 dB`, Q `2.92`; Gemini returned
`PASS / RETAIN`, hearing less lower-mid roominess and a cleaner verse-to-hook
handoff. v78 changed the existing Track 2 synth Band 3 A to `1.49 kHz`,
`-1.50 dB`, Q `1.34`; Gemini returned `PASS / RETAIN`, hearing clearer female
formant space without sacrificing synth weight, width, or drop impact.

v79 changed only the existing Track 3 (`3 bass`) Compressor Release from
`61.8 ms` to `82.6 ms`; attack remains `0.18 ms`, sidechain remains On, the
sidechain EQ remains an `80 Hz` high-pass, and LookAhead remains `0 ms`. MCP
readback confirmed the exact release and unchanged sidechain controls. The
Set was saved with no `*` marker. Gemini returned `AUDIO_GROUNDING: PASS /
RETAIN`: the longer release clears the kick's `45-55 Hz` transient pocket in
both drops without choking the sub sustain, adding pumping, or loosening the
groove. It also confirmed the female hook, stereo/mono low end, and translation
remain stable.

Current retained candidate:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v79-bass-release82ms-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`6F3A7FF5FCAC5028DA9C5527DA43304A5FEBE92AAD7AB9ADB7213A3F13978B53`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.07 dBTP`,
`-17.78 LUFS`, `4.0 LU LRA`, `15.92 dB` crest, `0.871` correlation, and
`-0.291 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`. Gemini's remaining actionable
items are localized: male `220-320 Hz` thickness against synth layers, drop
vocal-chop/high-synth energy around `6.5-8.5 kHz`, dry/rigid pre-drop snare
roll and riser tail, a brief low-end transition gap, and a slightly abrupt
final `350 ms` decay. The first three are hypotheses for separate bounded
tests; return/automation-point writing is outside the reliable public MCP/LOM
surface and therefore remains deferred unless a machine-readable command is
implemented. No Master-chain change has been stacked. D4 owner stereo/mono,
low-volume, translation, and release approval remain open.

The v75-v78 intermediate WAVs and their evidence are superseded by v79 and are
sent to the Windows Recycle Bin after this decision. Keep v79, v61, their
current audit/Gemini evidence, and the source Set.

### Accepted male-vocal dynamic-EQ A/B - v80 retained - 2026-08-18

v80 made one bounded change to Track 9 (`9 6 Vocals male`): Pro-Q 4 Band 8
was created in the plug-in UI as a dynamic bell at `260 Hz`, `Q 1.600`, and
its dynamic range was then set and read back through the MCP device-parameter
command as `-1.80 dB`. Existing EQ Eight bands, vocal levels, female vocal,
bass release `82.6 ms`, arrangement boundary, and Master chain were unchanged.
This is the working pattern for plug-ins whose internal bands are not fully
exposed by Live's public LOM: UI only for creation/inspection, MCP for the
exposed parameter write/readback, and MCP-facing `export_audio` for the render.

The Set was saved with no `*` marker. The v80 WAV was exported through the
MCP-facing bridge using `1.1.1` and `52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v80-male-proq4-dynamic260hz-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`0B4E760C9193E1E88E1F93A0C4525A9B211C0D6DB4EB3EBCE386BE7B04B0D728`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.04 dBTP`,
`-18.94 LUFS`, `4.8 LU LRA`, `16.71 dB` crest, `0.900` correlation, and
`-0.223 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, hearing the
dynamic 260 Hz cut tame resonant chestiness and lower-mid clutter without
thinning the male rap or reducing intelligibility. Its next actionable items
are a `2.5-3.5 kHz` transition/riser spike, female vocal-chop splash at
`6.5-8 kHz`, mild `45-60 Hz` kick/sub crowding, a wide backing-vocal buildup,
and a slightly abrupt final reverb-tail clamp. D4 owner stereo/mono,
low-volume, translation, and release approval remain open.

Keep v80 as the current retained candidate and v61 as the comparison
reference. Do not stack another change without a new single-variable A/B.

### Accepted female-chop de-essing A/B - v81 retained - 2026-08-18

v81 made one bounded MCP-controlled change to Track 8 (`8 6 Vocals female`):
the existing `Sibilance Stereo` Range moved from `-26.0 dB` to `-28.0 dB`;
threshold remained `-23.3 dB`, with detection, mode, and lookahead unchanged.
No new plug-in was inserted and the male Pro-Q 4 dynamic bell, vocal levels,
bass release, arrangement boundary, and Master chain were unchanged. The Set
was saved with no `*` marker and rendered through MCP-facing `export_audio`
using the same `1.1.1` / `52.0`-bar boundary:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v81-female-sibilance-range28-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`D5C16950EB43B530413951DC049A95EA3A38EBB84BBDE9E6F808253D1BE79A99`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.06 dBTP`,
`-18.95 LUFS`, `4.8 LU LRA`, `16.72 dB` crest, `0.900` correlation, and
`-0.223 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, hearing less
high-frequency sibilance splash in the hook chops around `00:58-01:00` and
`01:31-01:35` while preserving air, intelligibility, and male-rap clarity.
Next actionable items are P2: a `7.5 kHz` transient shelf dip on the chop
transition, a `12.5 kHz` high cut on the chop stereo-delay/widener return, a
`380 Hz` / `-1.0 dB` verse-synth cut, narrower male backing-vocal doubles, and
a smoother final-tail fade. D4 owner stereo/mono, low-volume, translation,
and release approval remain open.

v80 remains the immediately preceding retained comparison. Keep v81 as the
current candidate and do not stack another change without a fresh bounded A/B.

### Accepted synth-to-male-vocal masking A/B - v82 retained - 2026-08-18

v82 made one bounded MCP-controlled change to Track 2 (`2 synth`): the unused
EQ Eight Filter 6 A was enabled as a Bell at `381 Hz`, `-1.00 dB`, `Q 2.03`.
The Track 8 de-esser (`-28.0 dB` Range / `-23.3 dB` Threshold), Track 9
Pro-Q 4 dynamic bell (`260 Hz`, `Q 1.6`, `-1.80 dB`), vocal levels, bass
release, arrangement boundary, and Master chain were unchanged. MCP readback
confirmed all five EQ parameters. The Set was saved with no `*` marker and
rendered via MCP-facing `export_audio` at `1.1.1` / `52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v82-synth-381hz-cut-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`0C94F3EAE403DA2964D0E6A55C9AA95E7A6F855B002C18066AEDA67ABB45FF35`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.00 dBTP`,
`-18.95 LUFS`, `4.8 LU LRA`, `16.75 dB` crest, `0.901` correlation, and
`-0.220 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, hearing the
381 Hz dip declutter the low-mid accumulation behind the male rap around
`00:36-00:45` without reducing synth warmth, body, or drop punch. Next
actionable items are P1/P2: slightly widen or lower the male 260 Hz dynamic
bell, soften female chop transients around `6.5-7.8 kHz`, duck the FX/riser
by `-2.5 dB` just before the drop, trim a delay/reverb return around
`01:10-01:13`, and smooth the final `01:34-01:36` tail. The last three need
automation or return-envelope control that is not reliably exposed by the
public MCP/LOM surface. D4 owner stereo/mono, low-volume, translation, and
release approval remain open.

v81 remains the immediately preceding retained comparison. Keep v82 as the
current candidate and do not stack another change without a fresh bounded A/B.

### Accepted male-vocal dynamic-Q A/B - v83 retained - 2026-08-18

v83 made one bounded Pro-Q 4 change to Track 9 (`9 6 Vocals male`): the
existing Band 8 dynamic bell stayed at `260 Hz` and `-1.80 dB` dynamic range,
but its Q widened from `1.600` to `1.300`. The Q was created/inspected in the
plug-in UI because the public Live parameter surface does not expose all
third-party band controls; MCP then read back `Band 8 Q = 1.300`. Track 2's
`381 Hz / -1.00 dB / Q 2.03` synth cut, Track 8's `-28.0 dB` sibilance range,
vocal levels, bass release, arrangement boundary, and Master chain were
unchanged. The Set was saved with no `*` marker and rendered through the
MCP-facing `export_audio` bridge at `1.1.1` / `52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v83-male-proq4-q13-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`BBE9DBB99911046B8B3B0DD7C1E58A7C4FDFD8403568D60E304E20FA5AB6BD3D`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.06 dBTP`,
`-18.95 LUFS`, `4.8 LU LRA`, `16.69 dB` crest, `0.901` correlation, and
`-0.220 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, hearing the wider
dynamic cut clear the lingering `220-320 Hz` chest/box resonance during the
dense `00:36-00:45` delivery without thinning fundamental weight or diction.
Its next actionable items are a `3.5-6 kHz` transition-fill transient buildup
at `00:34-00:36`, a dynamic sidechained `3.2 kHz` synth dip in Verse 2, a
female `2.2 kHz` dynamic-formant cut, a pre-drop sub low-pass sweep, and a
smoother final vocal-chop reverb tail. Phrase-specific automation and return
envelope writing remain outside the reliable public MCP/LOM surface; do not
pretend a static change is equivalent. D4 owner stereo/mono, low-volume,
translation, and release approval remain open.

v82 remains the immediately preceding retained comparison. Keep v83 as the
current candidate and do not stack another change without a fresh bounded A/B.

### Accepted female-bridge dynamic-formant A/B - v84 retained - 2026-08-18

v84 retuned the existing dynamic Pro-Q 4 Band 4 on Track 8 (`8 6 Vocals
female`) to `2200 Hz`, `-1.50 dB`, `Q 2.500`. The band was already dynamic;
the plug-in menu showed `Disable Dynamics`, so no duplicate de-esser or EQ
band was inserted. The UI was used only because Live's public parameter map
does not expose the complete third-party band surface; MCP readback confirmed
the selected Band 4 Q as `2.500`, and the visual plug-in readback confirmed all
three values plus dynamic mode. Track 9's male `260 Hz / Q 1.300 / -1.80 dB`
dynamic bell, Track 2's `381 Hz / -1.00 dB / Q 2.03` synth cut, Track 8's
Sibilance `-28.0 dB` range, vocal levels, bass release, arrangement boundary,
and Master chain were unchanged. The Set was saved with no `*` marker and
rendered through MCP-facing `export_audio` at `1.1.1` / `52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v84-female-proq4-dyn2200hz-q25-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`6001365685FFB123301561030012969D11BC04A7B7A8271F425941A0222AE63A`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.11 dBTP`,
`-19.06 LUFS`, `4.8 LU LRA`, `16.70 dB` crest, `0.903` correlation, and
`-0.217 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, hearing the
`2200 Hz` dynamic bell smooth the female bridge's `00:48-00:54` nasal formant
spike while preserving articulation, presence, and top-end air. Its next
items are a slightly stronger male `240-280 Hz` dynamic reduction, a
`3.5-5 kHz` pre-drop riser wash, `6.5-7.2 kHz` vocal-chop resonance, wider
synth mono-energy management below `300 Hz`, and the strict `96.0 s` final
tail cutoff. The time-specific riser/return automation and boundary extension
remain outside the reliable public MCP/LOM write surface. D4 owner
stereo/mono, low-volume, translation, and release approval remain open.

v83 remains the immediately preceding retained comparison. Keep v84 as the
current candidate and do not stack another change without a fresh bounded A/B.

### Accepted synth-to-male-vocal masking A/B - v85 retained - 2026-08-18

v85 made one bounded MCP-controlled change to Track 2 (`2 synth`): the
existing EQ Eight Band 4 B moved from `390 Hz / -1.50 dB / Q 1.21` to
`455 Hz / -2.50 dB / Q 1.41`. MCP readback confirmed `455 Hz`, `-2.50 dB`,
and `Q 1.41`. Track 8 female processing, Track 9 male Pro-Q 4 dynamic bell,
bass release, arrangement boundary, and Master chain were unchanged. The Set
was saved with no `*` marker.

The v85 WAV was exported by a direct stdio call to the current repository's
MCP `export_audio` tool (not a manually initiated UI export), using
`1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v85-synth455hz-cut-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`0E6D296DD395ECAC32993EEA8BC91CC20564497F25769EC37C4922092F03CD4`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.10 dBTP`,
`-19.07 LUFS`, `4.8 LU LRA`, `16.72 dB` crest, `0.903` correlation, and
`-0.217 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`, explicitly hearing
cleaner low-mid separation and improved male English/Mandarin intelligibility
in `00:21-00:38` and `01:05-01:20` without thinning synth warmth or reducing
drop punch. Its next ranked issues are pre-drop riser high-mid clutter at
`00:44-00:48` and `01:27-01:31`, kick/sub bloom at `50-70 Hz` in the drops,
localized vocal-chop resonance at `6.5-7.2 kHz`, and a subtle final-tail
low-mid rumble. The riser and return-envelope fixes remain outside the
reliable public MCP/LOM write surface. D4 owner stereo/mono, low-volume,
translation, and release approval remain open.

v84 remains the immediately preceding retained comparison. Do not stack the
next change without a fresh single-variable A/B.

### Accepted kick/sub sidechain-release A/B - v86 retained - 2026-08-18

v86 made one bounded MCP-controlled change to Track 3 (`3 bass`): the existing
Compressor sidechain Release moved from `82.6 ms` (`value=0.25`) to `98.9 ms`
(`value=0.27`). MCP readback confirmed the track name, device, parameter, and
display value. Track 2's accepted `455 Hz / -2.50 dB / Q 1.41` synth cut,
both vocal chains, bass sidechain mode/EQ, arrangement boundary, and Master
chain were unchanged. The Set was saved with no `*` marker.

The v86 WAV was exported through a direct stdio call to the current
repository's MCP `export_audio` tool at `1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v86-bass-release99-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`D984638280707344251FF50F74FCD5D3EC5ECA8A9E11855999D09D40B6A7A397`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.10 dBTP`,
`-19.10 LUFS`, `4.7 LU LRA`, `16.76 dB` crest, `0.902` correlation, and
`-0.218 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`: the longer release
clears the kick/sub overlap in both drops (`00:48-01:05` and `01:31-01:48`)
without choking sustain, adding unnatural pumping, or weakening the groove.
It also confirmed stable male/female vocal focus, mono low end, vocal-chop
air, and final decay. Its next bounded P2 hypotheses are the pre-drop riser
build at `2.5-4.0 kHz` (`00:44-00:48`, `01:27-01:31`) and a slight male
`220-250 Hz` chest resonance. The riser action is time-specific automation
outside the reliable public MCP/LOM write surface; D4 owner stereo/mono,
low-volume, translation, and release approval remain open.

v85 remains the immediately preceding retained comparison. Do not stack the
next change without a fresh single-variable A/B.

### Accepted male-vocal dynamic-frequency A/B - v87 retained - 2026-08-18

v87 made one bounded third-party parameter change to Track 9 (`9 6 Vocals
male`): the existing Pro-Q 4 dynamic Band 8 center moved from `260 Hz` to
`235 Hz`. Dynamic range remained `-1.80 dB` and Q remained `1.300`; the
visual Pro-Q readback and the refreshed MCP parameter readback confirmed the
new frequency. Track 2's `455 Hz / -2.50 dB / Q 1.41` synth cut, Track 3's
`98.9 ms` bass sidechain release, female vocal chain, arrangement boundary,
and Master chain were unchanged. The Set was saved with no `*` marker.

The v87 WAV was exported through the current repository's MCP `export_audio`
tool at `1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v87-male-proq4-dyn235hz-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`E9D5D9F87281550A279F427449C9F2E16D179AD4E2F315B9B6B8EFA23228747B`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-5.16 dBTP`,
`-19.10 LUFS`, `4.8 LU LRA`, `16.70 dB` crest, `0.902` correlation, and
`-0.218 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`: the 235 Hz
dynamic center attenuates the male verse's 220-250 Hz box/chest buildup at
`00:22-00:44` and `01:06-01:27` without thinning weight, harming Mandarin or
English diction, changing the female hook focus, or disturbing kick/sub
punch, mono low end, vocal-chop air, riser transitions, or final decay. All
remaining observations are P2 maintenance notes; no further change is
accepted until a new problem is demonstrated. D4 owner stereo/mono,
low-volume, translation, and release approval remain open.

v86 remains the immediately preceding retained comparison. Do not stack the
next change without a fresh single-variable A/B.

### Accepted EDM master-gain A/B - v88 retained - 2026-08-18

v88 made one bounded MCP-controlled Master change: the existing Master Utility
Output moved from `-4.50 dB` (`value=-0.128571`) to `-0.50 dB`
(`value=-0.014286`) after the existing L4 Ultramaximizer. L4 remained on with
`-1.50 dB` threshold, `-1.00 dB` ceiling, and `x16` oversampling. Track 2
synth, Track 3 bass release, both vocal chains, arrangement boundary, and all
other Master parameters were unchanged. MCP readback confirmed the Master,
device, parameter, and `-0.50 dB` display value; the Set was saved with no
`*` marker.

The v88 WAV was exported through MCP `export_audio` at `1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v88-master-minus05db-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`92E6407131826D5299F4866507B9914B6E1C8BF9E5AC95A9264C6F98468DC259`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-1.23 dBTP`,
`-15.10 LUFS`, `4.8 LU LRA`, `16.61 dB` crest, `0.902` correlation, and
`-0.219 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`: the +4 dB master
gain raises commercial EDM impact without flattening kick/snare transients,
choking the sidechain groove, harshening vocal chops, pushing vocals back, or
damaging mono translation. Its next P1 is mild male proximity/boxiness at
`280-380 Hz` during `00:20-00:34`; its P1 sibilance note at `01:13-01:27`
is a separate hypothesis requiring a narrow A/B. No new Master change is
accepted until the vocal fixes are decided. D4 owner stereo/mono, low-volume,
translation, and release approval remain open.

v87 remains the immediately preceding retained comparison. Do not stack the
next change without a fresh single-variable A/B.

### Accepted male Pro-Q activation A/B - v89 retained - 2026-08-18

v89 made one bounded MCP-controlled state change to Track 9 (`9 6 Vocals
male`): the existing Pro-Q 4 `Device On` parameter moved from `Off` to `On`.
The intended dynamic Band 8 remained `235 Hz`, `-1.80 dB` dynamic range, and
`Q 1.300`; MCP readback confirmed the track, device, and `Device On = On`.
The Master Utility `-0.50 dB` output, L4 ceiling, Track 2 synth cut, Track 3
bass release, female vocal chain, arrangement boundary, and all other Master
parameters were unchanged. The Set was saved with no `*` marker.

The v89 WAV was exported through MCP `export_audio` at `1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v89-male-proq4-on-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`77B963AF318B0387F0C13222A6294EB5C56B6A82EF4C121F912CE63653133CD1`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-1.10 dBTP`,
`-15.38 LUFS`, `5.5 LU LRA`, `17.00 dB` crest, `0.899` correlation, and
`-0.225 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`: activating the
intended dynamic EQ tightens male low-mid chest congestion and unmasks
conversational diction without hollowing warmth or upsetting stereo groove,
limiter headroom, kick/sub, or mono focus. Remaining items are P2: slight
`320-360 Hz` buildup in sustained male phrases at `00:21-00:38`, female chop
brightness around `6.5 kHz`, mild Verse 2 `80-120 Hz` masking, and a wide synth
low-mid interaction. No new Master change is accepted. D4 owner stereo/mono,
low-volume, translation, and release approval remain open.

v88 remains the immediately preceding retained comparison. Do not stack the
next change without a fresh single-variable A/B.

### Accepted male-vocal dynamic-Q A/B - v90 retained - 2026-08-18

v90 made one bounded third-party parameter change to Track 9 (`9 6 Vocals
male`): the existing Pro-Q 4 dynamic Band 8 Q widened from `1.300` to
`1.050`; frequency stayed `235 Hz`, dynamic range stayed `-1.80 dB`, and the
plugin stayed On. The visual Pro-Q readback and refreshed MCP parameter
readback confirmed `Band 8 Q = 1.050`. Master Utility `-0.50 dB`, L4 ceiling,
Track 2 synth cut, Track 3 bass release, female vocal chain, arrangement
boundary, and all other Master parameters were unchanged. The Set was saved
with no `*` marker.

The v90 WAV was exported through MCP `export_audio` at `1.1.1 / 52.0` bars:
`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v90-male-proq4-q105-mcp-2026-08-18.wav`
(52 bars, 96.000 s, 44.1 kHz, 24-bit stereo). SHA-256 is
`55E8639F73EE1F4DB08A486FC555836134886B5884021EFD39D77C595F1D2BA6`.
The deterministic release audit is `D2 / MIX_RISK_REVIEW`: `-1.21 dBTP`,
`-15.39 LUFS`, `5.5 LU LRA`, `16.89 dB` crest, `0.899` correlation, and
`-0.225 dB` mono loss. The only proxy warning is the intentional `4.09 s`
leading silence; trailing silence is `0.0 s`.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS / RETAIN`: widening the
dynamic notch reins in residual `320-360 Hz` boxiness during sustained male
phrases at `00:21-00:38` without making the vocal thin, hollow, or less
intelligible. It confirmed the female chop brightness, Verse 2 low-end
separation, kick/synth punch, mono translation, loudness, and final tail are
stable. Remaining notes are P2 and explicitly optional; no further automated
change is stacked. D4 owner stereo/mono, low-volume, translation, and release
approval remain open.

v89 remains the immediately preceding retained comparison. Keep v90 as the
current candidate and do not stack another change without a new demonstrated
problem and fresh single-variable A/B.

### MCP-first export bridge and current vocal/low-end A/Bs - v99-v103 - 2026-08-18

The MCP workflow is now the standard path for edits, save, export, audit, and
Gemini review. `save_set` used the guarded MCP save bridge and verified the
Live title marker cleared. `export_audio` successfully produced validated
96.000 s, 44.1 kHz, 24-bit stereo Main bounces when given a short unique
basename in Downloads. The public LOM still has no native offline renderer,
so the caller-facing operation remains MCP while the internal compatibility
bridge foregrounds Live's renderer. The bridge now fails fast if a requested
output is absent but an existing WAV changes, and refuses overwrite prompts.

The long-basename v100 attempt exposed a Live Common Dialog filename-cache
defect: the requested path was not produced and the old v87 WAV was rewritten,
so that path no longer matches its historical v87 SHA and must not be used as
the v87 comparison. The MCP call correctly returned a blocker on the failed
attempt; the actual audio was recovered under a separate filename only for
diagnostic listening. Short names (`maybe-edm-v100...`, `maybe-edm-v101...`,
and finally `mcp-v103.wav`) are now required for the Live save-dialog step.

v99 enabled the existing Track 4 drums EQ Eight `High Pass 12dB @ 40 Hz`.
Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS`, but still heard female
4.5-7.5 kHz harshness, male masking, and kick/sub inconsistency; it was not
accepted alone. v100 tested female Sibilance Stereo Range `-32 -> -36 dB` and
did not close the harshness. v101 moved the existing female EQ Eight Band 7
from `3.80 -> 3.29 kHz` at unchanged `-1.20 dB / Q 2.50`; Gemini moved the
female issue from P0 to P1 and was the better bounded direction. v102 tested
soothe2 Band 3 sensitivity `2.9 -> 4.5 dB`; Gemini added limiter/low-end
concerns without a clear vocal win, so it was rejected and reverted to `2.9
dB`.

The current saved candidate is `mcp-v103.wav` (SHA-256
`38D12E54F07B8AA6BB0B7BABED0363B61578600246B5DB00B676CDB1909646E3`). Its
deterministic audit is `D2 / MIX_RISK_REVIEW`: `-16.25 LUFS`, `-1.22 dBTP`,
`0.900` correlation, and `-0.222 dB` mono loss. Gemini 3.7 Flash returned
`AUDIO_GROUNDING: PASS`; latest audible priorities are P0 drop sub/bass
overpowering and master pumping, P2 male 350-500 Hz/sibilance, and P2
remaining 3.2/4.1 kHz vocal-chop resonance. The project is saved with no
dirty marker. D4 owner stereo/mono, low-volume, translation, and release
approval remain open; do not call this release-ready until the owner listens.

### Low-end A/B follow-up and export/save bridge hardening - v104-v105 - 2026-08-18

v104 tested Track 3 bass EQ Eight `58.7 Hz / Q 3.79` from `-2.0 -> -3.5 dB`.
The MCP bounce was recovered and locally audited at `-16.29 LUFS`, `-1.26
dBTP`, `0.898` correlation, and `-0.228 dB` mono loss. Gemini 3.7 Flash
returned `AUDIO_GROUNDING: PASS` but still heard P0 kick/sub collision and
P1 female upper-mid resonance/male masking; the EQ cut was not accepted.

v105 then tested the existing Track 3 bass Compressor release from `68.3 ->
82.6 ms`, with the bass EQ at `-3.5 dB`. The MCP bounce is preserved as
`C:\Users\stanc\Downloads\mcp-v105.wav`, SHA-256
`2603AFA1235A9154D1EFB77A3A654CF2D2FCC63D890AAB8448852FF25C1D041D`, and the
local audit measured `-16.54 LUFS`, `-1.23 dBTP`, `0.921` correlation, and
`-0.176 dB` mono loss. Gemini requests returned Vertex `429
RESOURCE_EXHAUSTED` after retry, so v105 has no audible verdict and is not
accepted. The Live Set was reverted through MCP to the last Gemini-heard v103
state: bass `-2.0 dB` at 58.7 Hz and release `68.3 ms`, then saved with the
dirty marker cleared.

The save bridge now clears known stale Export Audio/Video and Save Audio File
dialogs before Ctrl+S; this fixed the apparent save failure caused by the
diagnostic UI inspection. The export bridge still correctly blocks when Live's
Common Dialog writes an unexpected cached path; short/cached-path export is a
documented compatibility workaround, not native LOM rendering.

### Antigravity CLI capability check - v106 - 2026-08-18

`agy` is installed and its model list includes Gemini 3.7 Flash variants. A
read-only smoke test against `mcp-v103.wav` nevertheless returned
`AUDIO_GROUNDING: FAIL` with `unsupported mime type audio/wav`. This proves the
current Antigravity CLI route can provide Gemini reasoning but cannot be used as
the project's audible mix reviewer. Keep it as a secondary planning/debugging
route; direct Gemini 3.7 audio upload remains the listening path and must still
produce `AUDIO_GROUNDING: PASS` with timestamps.

### Token-efficient Gemini listening workflow - v107 - 2026-08-18

The direct helper now defaults to a compact, issue-scoped response: at most
three timestamped issues, `maxOutputTokens=420`, the verified current-route
`thinkingLevel=LOW`, and one
short verdict/check line. It records the audio SHA, requested model, focus,
profile, kind, output cap, and usage metadata. A matching output report is
reused automatically when those scope keys match, so repeating a command does
not spend another Gemini prediction request; `--no-cache` forces a deliberate
fresh listen.

A real Gemini 3.7 Flash smoke against the exact v105 WAV returned
`AUDIO_GROUNDING: PASS` with `candidatesTokenCount=199` and no reported thought
tokens, versus the earlier unrestricted v105 report's `candidatesTokenCount=1310`
and `thoughtsTokenCount=773`. The compact result still identified the drop
kick/sub collision at `00:46` and supplied one actionable sidechain test. This
is an approximately 85% reduction in response tokens for an actionable A/B
check, while the final release gate remains one complete full-track
`--profile release` audit with the full WAV. The compact smoke report is
diagnostic evidence, not a new accepted mix decision.

The token-routing workflow was refined after a real `taste` smoke exposed that
the current `gemini-3.7-flash` endpoint rejects `thinkingLevel=MINIMAL`, and a
too-small output cap can leave only a partial answer after hidden reasoning.
The helper now defaults this endpoint to the empirically accepted
`thinkingLevel=LOW`, requires one concrete current-file question, and records
the setting. A focused LOW-level excerpt check returned
`AUDIO_GROUNDING: PASS` with 89 candidate tokens and a complete four-line
answer. `thinkingLevel=MEDIUM` remains an explicit option for a deliberate
final review; `MINIMAL` is not used because the endpoint rejected it.

### Bounded low-end and female-vocal taste A/Bs - v108-v110 - 2026-08-18

v108 tested Track 3 bass Compressor threshold `-25.9 -> -29.8 dB` through
MCP. Gemini compact listening returned `AUDIO_GROUNDING: PASS` but heard the
kick still smothering the sub and rejected the threshold direction. The Set was
restored to threshold `-25.9 dB` before the next test; v108 is not retained.

v109 then changed only the Track 3 bass Compressor Release from `68.3 -> 50.0
ms`, with threshold restored to `-25.9 dB`. The canonical MCP bounce is
`C:\Users\stanc\Downloads\mcp-v109.wav`, SHA-256
`CD86DE48018D1AB4E09BB242F86715D039D6A10D2CE430F2083FFC06862D101F`; local
audit measured `-16.44 LUFS`, `-1.23 dBTP`, `0.923` correlation, and `-0.171
dB` mono loss. Gemini's technical compact pass still detected 40--80 Hz
masking, but the targeted taste pass judged the pump intentional and said it
preserved kick punch and sub clarity at `00:07` and `01:17`, with `ACTION:
NONE`. Keep this as the current low-end candidate with the masking recorded as
an acceptable style risk pending the owner's D4 listen.

v110 changed only Track 8 (`8 6 Vocals female`, MCP index 7) Sibilance Stereo
Threshold from `-23.3 -> -27.5 dB`; Range stayed `-36.0 dB`, and the existing
EQ Eight/soothe2 chain and Master were unchanged. The MCP bridge wrote Live's
cached filename `Gemini 3.7 Flash Global Text Output - Predictions.wav`; the
fresh 24-bit/44.1 kHz/96.000 s file was format-audited and safely copied to
`C:\Users\stanc\Downloads\mcp-v110.wav`, SHA-256
`480A2C1B6D956B811BFABAC22AE58CD5A7291A2B3BB7CA9C59074A4A279C7253`. Its
local audit measured `-16.44 LUFS`, `-1.23 dBTP`, `0.923` correlation, and
`-0.171 dB` mono loss. Gemini 3.7 taste returned `AUDIO_GROUNDING: PASS`:
female hook/chops were smoother and forward without harshness, lisping,
dullness, or loss of clarity; `ACTION: NONE`. The Set is saved with no dirty
marker. D4 owner stereo/mono, low-volume, translation, and release approval
remain open; do not call this release-ready yet.

### Targeted male-vocal masking A/B - v111 - 2026-08-18

Before v111, Gemini 3.7 taste was asked one scoped question on `mcp-v110.wav`
and returned `AUDIO_GROUNDING: PASS`: the male English/Mandarin rap was still
masked by synths at `00:19` and `00:58`. Visual inspection of the active male
Pro-Q 4 graph showed deep dynamic cuts around 2 kHz, 4--5 kHz, 7 kHz, and 10
kHz; MCP readback showed Track 2 (`2 synth`, index 2) already had static cuts at
1.49 kHz (`-1.50 dB`) and 3.21 kHz (`-3.50 dB`).

The one-variable test deepened only Track 2 EQ Eight band 3 A from `-1.50 ->
-2.50 dB` at 1.49 kHz. The male chain, female chain, and Master were unchanged.
The direct stdio MCP call was run with `ABLETON_MCP_DISABLE_DATASET=true` so
the project operation did not opt into the separate public training dataset.
`save_set` returned `saved`, and `export_audio` returned a validated 96.000 s,
24-bit/44.1 kHz Main-path WAV at
`C:\Users\stanc\Downloads\mcp-v111.wav`.

The v111 local audit is D2 / `MIX_RISK_REVIEW`: `-16.44 LUFS`, `-1.24 dBTP`,
`0.9239` correlation, `-0.1687 dB` mono loss, 96.00 s, no hard clipping or
phase warning. Gemini taste on the exact v111 WAV returned
`AUDIO_GROUNDING: PASS` with 69 candidate tokens: it heard improved emotional
presence and intelligibility at `00:20` and `01:00`, with `ACTION: NONE`.
Retain v111 as the current male-vocal candidate. D4 owner stereo/mono,
low-volume, translation, full release audit, and release approval remain open.

### Targeted female-vocal veil A/B - v112 - 2026-08-18

Human listening reported that both vocals felt covered by a muffled/sandy layer
and lacked clarity, with the female vocal on Track 8 (`8 6 Vocals female`, MCP
index 7) worse than the male Track 9 (`9 6 Vocals male`, MCP index 8). Gemini's
targeted priority listen agreed that the female hook was the first clarity
problem: at `00:05` stutter/pitch-chop and phase smearing obscured articulation;
at `00:45` the hook was masked by resonant synth material. It proposed reducing
the female chop/gating or carving competing 2--4 kHz synths.

As a single, reversible texture test, MCP changed only Track 8 Convology XT
Mix (device 2, parameter 1) from `16% -> 10%`. The direct stdio call used
`ABLETON_MCP_DISABLE_DATASET=true`; readback confirmed `10%`, `save_set`
returned `saved`, and the guarded MCP export produced the validated
`C:\Users\stanc\Downloads\mcp-v112.wav` (24-bit/44.1 kHz, stereo, 96.000 s).
The first export attempt was blocked by a stale Export Audio/Video dialog; the
dialog was dismissed and the same MCP export then succeeded.

The v112 local audit is D2 / `MIX_RISK_REVIEW`: `-16.03 LUFS`, `-0.97 dBTP`,
`0.8974` correlation, `-0.2288 dB` mono loss, 96.00 s, no hard clipping,
phase, or dynamics failure. Gemini taste on the exact v112 WAV returned
`AUDIO_GROUNDING: PASS` with 77 candidate tokens and `ACTION: NONE`; it heard
clearer consonants and less veil without brittleness at `00:44`. Keep v112 as
the female-clarity candidate for the owner's direct listen, but do not infer
that the male track is solved or call the mix release-ready yet.

Owner follow-up listening confirms the female veil improved on v112. This is a
human-approved A/B direction, not yet a D4 release approval; keep the change
and avoid adding another broad high-frequency cut to Track 8.

A separate targeted Gemini taste check on v112 found the male verse already
direct and intelligible, with clear diction at `00:21` and `00:56`,
`ACTION: NONE`. This does not override the owner's broader “both vocals lack
clarity” impression; it narrows the next human check to whether the remaining
veil is female-specific or a whole-mix/instrumental masking issue.

The project now uses a targeted question matrix in
`docs/GEMINI_TARGETED_MIXING_PROTOCOL.md`: local metrics and one installed
plugin graph answer measurable questions, while Gemini gets one taste question
with one target/contrast/decision. The helper uses a 420-token safety cap for
iterative `taste`/`compact` checks and 600 for the one final release audit;
partial schemas are unverified rather than promoted as evidence.

### Full-song level and dynamics review - v113 review - 2026-08-18

Gemini's first compact pass was truncated and is retained only as an
unverified lead. A structured release-profile listen on the exact v112 export
returned `AUDIO_GROUNDING: PASS`: the male vocal is too quiet at
`00:31-00:43` by roughly `3.5-4.5 dB`, the second male verse has a similar
drop at `01:12-01:35`, and the female hook has high-mid transient jumps of
roughly `2-3 dB`. It recommended vocal level automation first, with only
gentle compression or instrumental masking changes afterward. A narrower
male-only taste check independently recommended a more conservative initial
`+2 to +3 dB` lift.

The exact v112 local audit remains D2 / `MIX_RISK_REVIEW`: `-16.03 LUFS`,
`-0.97 dBTP`, `LRA 6.0 LU`, `17.67 dB` crest factor, and `0.8974` stereo
correlation with `-0.2288 dB` mono loss. The master dynamics are not a hard
failure; the release risk is section-to-section vocal placement. Track 9 has
two male arrangement clips, so the timestamps were mapped to the rendered
timeline before attempting a ride.

The UI fallback was opened on Track 9 `Mixer > Track Volume`, but the first
breakpoint interaction did not produce a reliable machine-readable value and
Ableton then became unresponsive. No save or export was performed after that
interaction, so no v113 mix candidate is promoted. Stop further UI input until
Live recovers; then re-observe the automation lane, verify every breakpoint in
dB, save, export, audit, and run the same targeted Gemini listen. Do not call
the review a completed automation pass.

### v115 static male-level candidate and full-song dynamics review - 2026-08-18

The recovery path completed the MCP-first alternative to the failed UI ride.
The active Remote Script was upgraded and verified at v1.10.0 with
`get_track_volume_info` / `set_track_volume_value`. Live readback established
the current mixer mapping `0.85 = 0.0 dB` and `0.90 = +2.0 dB`; Track 9 was set
to `0.90`, saved, and exported to the exact v115 Main WAV. This is a static
track trim, not phrase-level automation.

The v115 local audit is `D2 / MIX_RISK_REVIEW` because vocal-stem dynamics and
owner listening are still separate gates, but the full-mix dynamics checks
pass: `-15.70 LUFS`, `-0.97 dBTP`, `LRA 5.2 LU`, `17.44 dB` crest factor,
`9.32 dB` block-RMS p90-p10 spread, `0.8990` correlation, and `-0.225 dB`
mono loss. Gemini returned grounded `PASS` for both male timestamps (`00:35`,
`01:03`) and for the whole-song level/dynamics flow, with no further action.
Keep v115 as the current candidate, retain v112 for level-matched A/B, and
wait for the owner's stereo/mono/low-volume translation approval before D4 or
cleanup of superseded exports.

### v116 instrumental low-mid A/B - 2026-08-18

Gemini's grounded instrumental review of v115 identified a specific problem:
the main synth stack built up around `250-450 Hz` at `01:08-01:13`, clouding
the riser and fighting the second-drop kick. Track 2 already contained an
MCP-readable EQ Eight bell at `320 Hz / -1.50 dB / Q 1.83`, so the reversible
MCP A/B deepened only that gain to `-2.50 dB`. Pro-Q 4 remains present on the
same track, but its internal bands are not exposed by the current Remote
Script; therefore this is explicitly a static proxy, not a claimed dynamic EQ
implementation.

The v116 Main bounce used the identical `1.1.1 / 52.0 bars` range and validated
at 96.000 s, 44.1 kHz, 24-bit stereo. Its local audit measured `-15.70 LUFS`,
`-0.97 dBTP`, `LRA 5.2 LU`, `17.43 dB` crest, `9.29 dB` block-RMS spread,
`0.9002` correlation, and `-0.222 dB` mono loss. Compared with v115, the
render changed materially (`rms_diff 0.000848`), while dynamics stayed stable.
Gemini returned grounded `RETAIN / ACTION: NONE`, hearing clearer riser/vocal
chops at `01:08` and tighter kick/sub separation at `01:13`. Keep v116 as the
current candidate; do not stack another low-mid cut without a new problem and
fresh A/B. D4 owner stereo/mono, low-volume, translation, and release approval
remain open.

### v117 Master true-peak trim A/B - 2026-08-18

The v116 audit measured `-0.97 dBTP`, which was just outside this project's
delivery requirement of at or below `-1.0 dBTP`. The active Remote Script was
not yet able to read the Master device chain after the controlled-restart
attempt, so the documented UI fallback was used: the selected Master chain
visually showed `L4 Ultramaximizer Stereo -> Utility`, and Utility Output was
changed from `-0.50 dB` to `-0.70 dB`. The exact parameter value was visually
read back before saving; no other device or track was changed.

The same MCP-facing export bridge produced the v117 Main WAV at the identical
`1.1.1 / 52.0 bars` range. The local audit is `D2 / MIX_RISK_REVIEW` with
`-16.24 LUFS`, `-1.17 dBTP`, `-1.17 dBFS` sample peak, `LRA 6.0 LU`,
`17.67 dB` crest, `10.76 dB` block-RMS spread, `0.8986` correlation, and
`-0.226 dB` mono loss. The delivery true-peak and dynamics checks now pass.
Gemini returned grounded `RETAIN / ACTION: NONE`, hearing no loss of vocal
forwardness, kick/sub impact, drop energy, or stereo space. Keep v117 as the
level-matched comparison while the final mixer state is re-read below; D4 owner
stereo, mono, low-volume, translation, reference, and release approval remain
open.

### v118 male level re-read and full-song dynamics review - 2026-08-18

Before the next review, a direct MCP read of the saved Live state found Track 9
(`9 6 Vocals male`) at `0.85 = 0.0 dB`, despite the earlier v115 ledger recording
the intended `0.90 = +2.0 dB` trim. This was a state-drift/recovery discrepancy,
not an assumption to ignore: MCP set the track back to `0.90`, read it back at
`+2.0 dB`, saved the Set, and produced a fresh identical-range Main bounce.

The v118 WAV is `C:\Users\stanc\Downloads\mcp-v118-male-plus2-rerender.wav`,
with `96.000 s`, 24-bit/44.1 kHz stereo. Its local audit is
`C:\Users\stanc\Downloads\mcp-v118-male-plus2-rerender-audit\mix-audit.md`
and remains D2 /
`MIX_RISK_REVIEW` with `-15.90 LUFS`, `-1.17 dBTP`, `LRA 5.2 LU`, `17.43 dB`
crest factor, `9.29 dB` block-RMS p90-p10 spread, `0.9002` correlation, and
`-0.222 dB` mono loss. Sample peak, true peak, dynamics, and stereo/mono proxy
checks pass; vocal active RMS is still unknown because no isolated vocal stem
was supplied.

The final targeted Gemini full-song check returned grounded `PASS`: restoring
Track 9 to +2 dB brought the male verse into proper focus and balanced it with
the female hook without over-compressing the mix bus. It cited `00:33` as clear
over the synth plucks and `01:18` as a punchy, contrasting drop, with
`ACTION: NONE`. This closes the automated level/dynamics iteration for now;
phrase-level automation is not claimed. D4 owner stereo, mono, low-volume,
translation, reference, and release approval remain open.

### Vocal-only batch workflow and complete-range recheck - 2026-08-18

The project workflow was tightened after an inefficient UI/export attempt.
`tools/vocal_review_batch.py` now performs one read-only MCP preflight for
Tracks 8/9: session timing, script capabilities, mixer values, device names,
and arrangement clip boundaries. The batch artifact for this pass is
`C:\Users\stanc\Downloads\vocal-review-batch-v127.json`. It confirmed Track 8
at raw `0.874942...` (the saved approximately `+1 dB` state) and Track 9 at
raw `0.90` (`+2 dB`), with vocal clips extending to beat `239.435` (about
`110.5 s`).

The UI export fallback was used once to verify the complete render range,
because the active Remote Script has no native offline render command. The
fields were visually confirmed as `1.1.1 / 62.0.0`; the resulting WAV is
`C:\Users\stanc\Downloads\mcp-v128-vocal-level-review-fullsong.wav`,
`114.461542 s`, 24-bit/44.1 kHz stereo, SHA-256
`CD8EE61CC0A21FB3C3BDF891C4F2E4B55345EFDDBA1496BBFC830E0064E22F04`.
The local audit is D2 / `MIX_RISK_REVIEW`: `-18.03 LUFS`, `-1.60 dBTP`,
`5.0 LU LRA`, `20.89 dB` crest, `0.9074` correlation, and `-0.206 dB` mono
loss. The long leading/trailing silence warning is intentional-range context,
not a vocal defect; vocal active RMS remains unknown without stems.

Two fresh Gemini requests for v128 were incomplete (`AUDIO_GROUNDING:
UNVERIFIED`), so neither partial comment is promoted to a finding. The prior
grounded focused v127 listen still supports a small male-level A/B, while the
conflicting broad listen prevents an automatic fader move. No new vocal EQ or
compression change is accepted yet. The next action is one complete-range,
vocal-only level/automation A/B, followed by one compact Gemini decision; the
instrumental tranche remains deferred.

The first MCP automation attempt was deliberately bounded: Track 9 clip gains
read back at `0.400000...` dB, and Live rejected `+1.5 dB` as out of range;
the only accepted test value (`0.5`) was a negligible `+0.1 dB`, so both clips
were restored to `0.4` and the Set was saved. This proves the current MCP
clip-gain fallback cannot implement the requested phrase ride. Do not count it
as a musical A/B; either expose a real envelope-write capability or use one
carefully isolated UI automation operation later.

### Accepted male back-half vocal level A/B - v129 retained - 2026-08-18

The first targeted vocal level A/B used the existing MCP clip-gain command on
Track 9 (`9 6 Vocals male`) clip 1, the Arrangement clip spanning beats
`122.0-172.7578` (the user's bars 31-43). The Live Object Model exposes this
clip property as a normalized `0.0-1.0` value; the repository command's legacy
argument is still named `gain_db`, so the raw readback must not be described as
a decibel number. The raw value moved from `0.400000...` to `0.600000...`;
Track 9's static fader stayed at `0.90` (`+2 dB`), Track 8 stayed at
`0.874942...` (about `+1 dB`), and no instrumental track or device changed.

The Set was saved with the dirty marker cleared. The complete `1.1.1 / 62.0`
bar Main render is
`C:\Users\stanc\Downloads\mcp-v129-male-second-clip-gain06-fullsong.wav`,
`114.461542 s`, 24-bit/44.1 kHz stereo, SHA-256
`D0C9B96B6B24B78D2350C913D772FCBBAE8E4609FF66E8C40A15A257F91B191D`.
Its local D2 audit is `MIX_RISK_REVIEW`: `-14.67 LUFS` loudnorm integrated,
`-1.33 dBTP`, `10.6 LU LRA`, `18.12 dB` crest, `0.9174` correlation, and
`-0.183 dB` mono loss. The long-range silence warning and unmeasured vocal
active RMS remain audit limitations, not release approval.

Gemini 3.7 Flash returned `AUDIO_GROUNDING: PASS` and `RETAIN`: at `00:58`
the later male diction remained sharp and balanced against the rhythm section;
at `01:14` its energy carried smoothly into the transition without a jarring
dynamic jump. This is the first retained complete-range vocal level A/B for
the bars 31-43 problem. It is clip-level correction, not true breakpoint
automation; the next phrase-specific ride still requires a tested envelope
writer or a carefully isolated UI operation. D4 owner stereo/mono,
low-volume, translation, reference, and release approval remain open.

A follow-up Gemini priority request on v129 and a 20-second Track 8 opening
excerpt both returned `AUDIO_GROUNDING: UNVERIFIED` because the response ended
after a fragment of the answer. They are retained only as failed/partial
checks; no harshness, sibilance, or upper-mid change was made from them. The
grounded vocal evidence therefore remains v129's level RETAIN plus the earlier
v112 female-veil RETAIN. Do not spend another full-track request on the same
question unless a new candidate or a human listening note supplies a narrower
contrast.

After switching the helper default to `thinkingLevel=LOW`, the same 20-second
Track 8 opening excerpt produced two complete grounded checks. Gemini first
identified the dominant sound as rhythmic stutter/gating rather than harsh
sibilance, then confirmed that the tightly grid-synced repeats read as
intentional EDM vocal-chop texture (`00:00` and `00:10`) and should be retained.
No Track 8 processing was changed: this is a classification of the existing
chop, not a request to remove it. It also confirms the new LOW-thinking route
returns complete four-line taste reports where the legacy zero-budget route
had returned fragments.

### v130 natural vocal delivery boundary and grounded release triage - 2026-08-18

The v129 complete 62-bar render contained a measured internal silence from
`94.882041` to `107.102426` seconds (`12.220385 s`), plus a trailing tail. The
same saved state was re-rendered through the guarded MCP-facing export bridge at
the previously verified natural `1.1.1 / 52.0 bars` boundary:
`C:\Users\stanc\Downloads\mcp-v130-v129-vocal-natural52-fullsong.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`6E07D38D82803821A1AC1E7171AE8EA78CFDBD84BCC3DAEC8F6C1EF98013BF4E`.
The deterministic audit measured `-14.66 LUFS`, `-1.33 dBTP`, `9.9 LU LRA`,
`17.39 dB` crest, `0.917476` correlation, and `-0.1830 dB` mono loss. It is
still D2 / `MIX_RISK_REVIEW`; vocal-active RMS and owner D4 listening remain
unmeasured/open.

The grounded release listen on this exact 52-bar file confirmed that the
natural boundary removes the long silence, then identified three separate
items: P0 male low-mid masking around `200-350 Hz` at `00:20`, P1 male
upper-mid harshness around `3.5-5 kHz` at `01:13`, and P2 female brightness/
depth at `00:08`. The P0 bass-side action is explicitly deferred because this
tranche is vocal-only; no instrumental or Master parameter was changed.

### Accepted vocal-only male harshness A/B - v131 retained - 2026-08-18

MCP readback confirmed that Track 9 Pro-Q 4 exposes only `Device On`; its
internal dynamic bands cannot be changed through the current Remote Script.
Track 9's old EQ Eight was bypassed with multiple configured bands, so it was
not enabled wholesale. Instead, MCP loaded one new native EQ Eight at the end
of the male chain and configured only its first active bell: normalized
frequency `0.787` (approximately `4.2 kHz`), gain `-2.5 dB`, Q proxy `0.68`
(approximately `3.5`). Track 8, the Master, and all instrumental tracks were
unchanged.

The Set was saved with no dirty marker. The verified Main render is
`C:\Users\stanc\Downloads\mcp-v131-male-42khz-static-proxy-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`8C9825B2394A281957A8B487B5433775B35E09CBB29CFEEBBD55205B26951EF3`.
Its local D2 audit measured `-14.88 LUFS`, `-1.34 dBTP`, `9.8 LU LRA`,
`17.48 dB` crest, `0.917986` correlation, and `-0.1818 dB` mono loss; the
only warning is the intentional-range silence proxy and vocal-active RMS is
unknown without a vocal stem. Gemini 3.7 Flash returned grounded `PASS / RETAIN`:
the cut tamed upper-mid bite while preserving diction at `00:20` and `01:13`.
This is a static vocal-only fallback, not a claim that Pro-Q dynamic EQ was
written.

### Rejected female brightness A/B - v132 reverted - 2026-08-18

To address the v130 P2, MCP deepened only Track 8 EQ Eight band 8 A from
`-4.0 dB` to `-5.0 dB` at approximately `7 kHz` (Q proxy `0.72`). The exact
v132 render was valid and auditable, but Gemini returned grounded `FAIL`: the
female vocal remained harsh/piercing and sounded hollowed out at `00:08` and
`00:44`, with no centered warmth. The parameter was immediately restored to
`-4.0 dB`, read back, saved, and the v131 state is therefore the current saved
candidate. Gemini's next suggestion is a fast narrow dynamic de-esser around
`6-8 kHz` with light `1-2 kHz` warmth; the detector-frequency control is not
currently MCP-exposed, so do not guess or stack another static high cut.

The vocal tranche remains in progress: retain v131 as the male clarity A/B,
retain the earlier human-approved female veil improvement, and defer the
female dynamic de-esser/UI observation plus owner D4 stereo/mono/low-volume
listen until the next bounded pass. Instrumental and bass-side changes remain
deferred.

### Female A/B triage and male clip-gain drift correction - v133-v136 - 2026-08-18

The next bounded female pass tested Track 8 Sibilance Stereo Detection `0.50 →
0.35` and Mode `0.50 → 0.75`, leaving Threshold and Range unchanged. The exact
v133 render was valid, but Gemini returned grounded `FAIL`: the harsh/piercing
behavior remained at `00:08` and `00:44`; Detection/Mode were restored to
`0.50/0.50` and saved. This confirms that another broad de-esser-mode change
is not yet justified.

v134 then tested Track 8 Ozone 11 Imager high-band width `0.7631579 → 0.65`.
Before promoting that A/B, the deterministic comparison exposed a more basic
state problem: v135 was about `3 dB` quieter only in the later male phrase.
MCP readback showed Track 9's second arrangement clip had drifted from raw gain
`0.6` back to `0.4`. Ozone width was restored to `0.7631579`; v134/v135 are
not valid female tonal decisions and were not promoted.

The bounded repair set Track 9's second arrangement clip back to raw gain
`0.6`, saved the Set, and exported the exact Main range as v136:
`C:\Users\stanc\Downloads\mcp-v136-restored-v131-clipgain06-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`51F51D268ABF198742DC8D8F00FEA08FD2E0194ED65F236D1B13543449CA36FA`.
The local D2 audit measured `-14.88 LUFS`, `-1.34 dBTP`, `9.8 LU LRA`,
`17.48 dB` crest, `0.917986` correlation, and `-0.1818 dB` mono loss; the
only warning remains the intentional-range silence proxy and vocal-active RMS
is unmeasured without a vocal stem.

Focused Gemini 3.7 Flash on the exact v136 file returned grounded `PASS` and
`ACTION: NONE`: at `00:58` the Mandarin entrance was stable, and at `01:14`
the English phrase resumed with matching presence and no volume jump. v136
therefore retains the v131 male clarity treatment plus the corrected clip
level. The female veil/brightness issue remains the next vocal-only question;
do not treat v134 as evidence for widening or narrowing it.

### Accepted female veil A/B - v137 retained - 2026-08-18

After the rejected v133 Sibilance mode A/B and the invalid/incomparable v134
width A/B, the next change used an existing advanced vocal processor rather
than another static high cut. Track 8 soothe2 depth was reduced only from
`0.3986404` to `0.3300000`; all other soothe2 and vocal parameters remained
unchanged.

The exact Main render is
`C:\Users\stanc\Downloads\mcp-v137-female-soothe-depth033-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`D281A89313646CDE48F96DC09F54ED6205847C43CAB522DADC474164CF105076`.
The local D2 audit measured `-14.79 LUFS`, `-1.34 dBTP`, `9.8 LU LRA`,
`17.37 dB` crest, `0.918562` correlation, and `-0.1805 dB` mono loss. The
Set was saved with the dirty marker cleared.

Focused Gemini 3.7 Flash returned grounded `PASS / RETAIN`: at `00:08` the
opening hook regained breath and articulation without brittleness, and at
`00:44` the melodic entry felt clear and natural rather than suppressed. This
is a small, evidence-backed veil reduction, not a claim that the female vocal
is finally D4-approved. The next check should be human level-matched stereo,
mono, and low-volume listening of v137 before another processor change.

### Accepted male low-mid cleanup A/B - v138 retained - 2026-08-18

The first complete vocal triage after v137 still identified a possible male
verse boxiness around `300-500 Hz` at `00:20`, but its suggested broad `+2 dB`
high-shelf change was intentionally rejected as too wide. A single-variable
MCP edit instead used the already isolated native Track 9 EQ Eight: filter 2
bell gain moved from `0.0 dB` to `-1.5 dB` at its existing approximately
`400 Hz` setting. No female, Master, instrumental, or clip-gain parameter was
changed.

The exact Main render is
`C:\Users\stanc\Downloads\mcp-v138-male-400hz-minus15-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`12E329D682BC9AB4864649062BD050D6B2607DB59C3BA8415AAA69678F055EF1`.
The local D2 audit measured `-14.95 LUFS`, `-1.37 dBTP`, `9.9 LU LRA`,
`17.57 dB` crest, `0.916835` correlation, and `-0.1845 dB` mono loss. The
Set was saved with the dirty marker cleared and playback was verified stopped.

The focused Gemini 3.7 Flash check returned grounded `PASS / RETAIN`: at
`00:20` the male verse separated more cleanly from the bass without losing
natural chest resonance, and at `00:28` the conversational Mandarin phrasing
kept clear syllabic articulation without sounding hollowed out.

An additional compact full-track triage was marked `UNVERIFIED` by the local
grounding contract. Its recommendation to reduce female stutter/glitch FX is
therefore only a hypothesis and conflicts with the earlier grounded
classification of the grid-synced chop as intentional texture; no FX change is
promoted until a narrow A/B or human approval resolves that conflict.

### Accepted female gate-tail A/B - v139 retained - 2026-08-18

The strict vocal-only Gemini gate on v138 returned grounded `CHANGE`, hearing
abrupt gate/stutter cutoffs at `00:00` and `00:44`. Track 8 had no dedicated
gate device; its active Multiband Dynamics high band had `Above Threshold
-24 dB`, `Above Ratio 0.75`, and a short release proxy of `1.8451` (about
70 ms). The smallest plausible exposed control was the high-band release,
changed to `2.1761` (about 150 ms). Sibilance, soothe2, clip gains, vocal
levels, male EQ, Master, and instrumental tracks were unchanged.

The first export attempt failed because Live did not open the Export Audio/
Video dialog. The guarded bridge was retried without changing the request and
then succeeded with the exact `1.1.1 / 52.0 bars` range. The v139 render is
`C:\Users\stanc\Downloads\mcp-v139-female-high-release150ms-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`AB1DDF426800452BCF1649AA99833A3040B1D2A1BB20FCBE5BBC61E9B0BDA9FF`.
The local D2 audit measured `-14.31 LUFS`, `-1.14 dBTP`, `7.8 LU LRA`,
`16.35 dB` crest, `0.921287` correlation, and `-0.1744 dB` mono loss; the
intentional leading-range silence warning remains, with no trailing silence.

Focused Gemini 3.7 Flash returned grounded `PASS / RETAIN`: at `00:00` the
stutter intro kept its rhythmic bounce without abrasive transient clicks, and
at `00:44` the hook entry was natural and clearly defined over the drop, with
no clipped tails. Because v139's loudness/dynamics proxies moved materially
from v138, the next human check must be level-matched before any further vocal
processing. Do not interpret this A/B as a final D4 release approval.

### Accepted synth-to-vocal upper-mid masking A/B - v140 retained - 2026-08-18

The strict whole-vocal Gemini gate on v139 returned grounded `PASS / RETAIN`:
the chop/gate envelopes were intentional and there were no unintentional
cutoffs or noise-floor pumps. Its only actionable mix note was P2 upper-mid
competition between vocal chops and synth leads around `3.5-4.5 kHz`.

Track 2 (`2 synth`, MCP index 2) already had an MCP-readable EQ Eight bell at
approximately `3.2 kHz`, `Q 2.0`; its gain was changed only from `-2.5 dB` to
`-3.5 dB` as a static proxy for the suggested dynamic sidechain dip. Vocal
tracks, bass, drums, Master, arrangement boundaries, and all other devices
were unchanged.

The exact Main render is
`C:\Users\stanc\Downloads\mcp-v140-synth-32khz-minus35-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`D6B22E684DC84FF6272A1084C2DA10E3AD39211D4944BBF254BAF030A7951A04`.
The local D2 audit measured `-14.31 LUFS`, `-1.14 dBTP`, `7.8 LU LRA`,
`16.35 dB` crest, `0.921841` correlation, and `-0.1731 dB` mono loss; the
intentional leading-range silence warning remains. Focused Gemini returned
grounded `PASS / RETAIN`: at `00:10` vocal-chop detail cut through the synth
attack cleanly, and at `01:28` the drop retained its brightness, drive, and
lead-chop presence.

The saved current candidate is now v140. Next instrumental checks should be
kick/sub dynamics, mono low-end translation, and the Master readback; do not
stack another upper-mid cut without a new timestamped problem.

### Accepted synth sidechain-tail A/B - v141 retained - 2026-08-18

The strict instrumental Gemini gate on v140 returned grounded `CHANGE`: drop
synth tails were being chopped by an aggressive gate/sidechain pattern at
`00:04` and `01:28`. Track 2 (`2 synth`, MCP index 2) has an active
sidechain Compressor (`S/C On=1`, `S/C Gain=0.4`) whose Release raw value was
changed only from `0.25` to `0.32`, targeting approximately `120-150 ms`.
The synth EQ, vocals, bass, drums, Master, and arrangement were unchanged.

The exact Main render is
`C:\Users\stanc\Downloads\mcp-v141-synth-sidechain-release032-52bar.wav`,
96.000 s, 24-bit/44.1 kHz stereo, SHA-256
`F5A855C7C3D22C9DB9E411E436E3C7A93EDA9744005A0E58B0740B7F7836C404`.
The local D2 audit measured `-14.31 LUFS`, `-1.14 dBTP`, `7.8 LU LRA`,
`16.34 dB` crest, `0.922292` correlation, and `-0.1721 dB` mono loss; the
intentional leading-range silence warning remains. Focused Gemini returned
grounded `PASS / RETAIN`: at `00:04` the synth tail ducks cleanly without
choking, and at `01:28` the drop breathes rhythmically with punchy low-end
impact.

The current full-mix candidate is v141. Next checks are the bass transition
and Master chain readback; do not change the synth release again without a new
timestamped problem.

### Export bridge and batch verification note - 2026-08-18

The MCP-facing export helper now retries foreground focus when Windows rejects
the first focus transfer, reuses an already-open Export Audio/Video dialog,
and uses a local keyboard fallback only when the normal shortcut does not
open the dialog. This reduces UI round-trips, but every export still requires
exact range, duration, format, SHA, local audit, and stopped-playback
verification. The v133-v136 drift diagnosis also establishes a new invariant:
read back arrangement clip gains immediately before a vocal export.

## Done means

The project reaches **D4**, the evidence package is reproducible, the final
master passes the hard technical checks, all material feedback has a recorded
decision, and the owner has listened and approved the release candidate.

Until then, the status is **in progress**, **blocked by missing evidence**, or
**needs human listening**—never “finished” because the limiter, AI, MCP, or
automated report says so.
