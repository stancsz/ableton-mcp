# EVAL.md — EDM Mix, Group Mastering, and Release Evaluation

This document is the evaluation contract for the Ableton EDM Set described in
[`GOAL.md`](GOAL.md). It answers one question:

> Does the current candidate have enough musical, technical, and listening
> evidence to move to the next production stage or to be approved for release?

This is an evidence gate, not a request to make the track louder, a plugin
score, or a substitute for the owner's listening decision. Passing a software
test, an MCP command, a meter, or an AI review does not prove that the track is
finished.

## 1. Evaluation truth model

Every result must distinguish what was observed from what is still a
hypothesis:

`exact artifact / Live readback → observation → risk or hypothesis → test → decision`

Use these outcomes:

- **PASS** — the required behavior is demonstrated by the specified evidence.
- **FAIL** — a required behavior is contradicted by the evidence; do not
  advance the stage.
- **BLOCKED** — the required artifact, render range, bridge, reference, or
  listening path is unavailable or unverifiable.
- **DEFERRED** — a non-release-blocking issue is intentionally left open with
  an owner-visible reason and a named follow-up decision.
- **RETAIN / REVERT** — the result of a reversible A/B decision. Neither word
  means D4 approval.

Deterministic measurements, Gemini observations, and human listening notes must
remain separate. If Gemini returns `AUDIO UNAVAILABLE`, the result is
**BLOCKED**, not a listening pass. Promote an audio observation only when the
exact file, model/version, `AUDIO_GROUNDING: PASS`, and timestamped observation
are recorded.

A grounded Gemini report is bound to the exact WAV hash it heard. Every new A/B
candidate requires a fresh listen on that exact file; never carry a `RETAIN`
decision from an earlier hash to a new candidate.

## 2. Current evaluation entry point

The current retained candidate is v60:

`C:\Users\stanc\Downloads\maybe-edm-mix-vocal-chops-audible-song-v60-female-sibilance-threshold-2026-08-17.wav`

- Format: 24-bit PCM WAV, 44.1 kHz, stereo.
- Duration: `114.462 s`.
- SHA-256:
  `87CC146B79B8BC913E83B283C52F8BFBEAC07B45461243FD962F25EAAC84AA32`.
- Deterministic state recorded in `GOAL.md`: `D3 / MIX_RISK_REVIEW`,
  `-5.03 dBTP`, `-18.85 LUFS`, `6.9 LU LRA`, `17.28 dB` crest,
  `0.897` correlation, and `-0.230 dB` mono loss.
- The Master was unchanged for the v60 vocal pass.

v61 is **rejected evidence** for comparison because its render was shorter
than v60 (`110.769 s` versus `114.462 s`). Restore and verify the authoritative
render range before accepting another instrumental A/B. Do not compare
candidates with different Main-path ranges, intentional start silence, or tail
coverage.

The intended delivery target and two or three level-matched references must be
named before final Master loudness is judged. Until then, loudness is
**BLOCKED**, not failed and not approved.

## 3. Evidence maturity gates

| Gate | Meaning | Minimum evidence | May advance? |
|---|---|---|---|
| D0 | No reliable render | No authoritative WAV | No |
| D1 | Technically readable | Exact PCM WAV decodes; path, format, hash, and duration recorded | Only to measurement |
| D2 | Measurable mix risk | Integrity, peak/true peak, loudness context, dynamics, spectrum, stereo, and mono checks complete | Only to contextual comparison |
| D3 | Contextual comparison | Level-matched references and relevant group/full-mix comparisons complete | Only to owner listening |
| D4 | Human approved | Owner completes stereo, mono, low-volume, translation, musical, and reference listening | Release approval |

A clean deterministic report is never D4. A `RETAIN` response from Gemini is
never D4. D4 belongs to the owner who listened to the exact final candidate.

## 4. Stage gates

### E0 — Scope and provenance

**Purpose:** prove that the candidate and the evaluation target are the same
thing.

Pass only when all are recorded:

- exact `.als` or authorized checkpoint path;
- exact WAV path, SHA-256, sample rate, bit depth, channel layout, and duration;
- Live version, tempo, render path, start, length, and export settings;
- intended delivery target: streaming, DJ/club, label demo, or explicitly named
  multiple versions;
- two or three relevant references with source, version, and level-matching
  method;
- current visible track names and MCP indices for every changed group or track.

Missing provenance is **BLOCKED**. Never fill it with a filename guess or a
generic EDM assumption.

### E1 — Render and technical integrity

Run the local mix audit on the exact PCM WAV. Confirm:

- the file decodes without error and has the expected duration;
- the Main path, render start, length, and tail are comparable to the accepted
  candidate;
- no unexpected leading/trailing silence, clipping, broken routing, accidental
  mute/solo, or truncated arrangement is present;
- sample peak and true peak are recorded; the delivery candidate is at or below
  `-1 dBTP`;
- LUFS, LRA, crest, spectrum, stereo correlation, and mono loss are recorded
  as context, not as a universal loudness score;
- deterministic warnings are separated from audible conclusions.

Any hard technical failure is **FAIL**. An intentional silence or stylized tail
may be **DEFERRED** only when its intentionality is documented and the owner
accepts it at D4.

### E2 — Vocal group bus

**Purpose:** finish the vocal group as a controlled musical bus, not merely a
set of individually processed tracks.

Evaluate lead, English/Mandarin rap, pitched chops, backing vocals, group
dynamics, and vocal-group returns in the full mix. Confirm:

- lead and rap remain intelligible at low monitoring volume;
- female hook remains the focal point without harsh sibilance, lisping, or
  being pushed backward;
- male rap retains consonants and character without material boxiness, hollowness,
  or masking;
- backing vocals provide depth without muddy center buildup;
- chops retain brightness and hook identity without piercing 3–5 kHz energy,
  pumping, or mono collapse;
- verse, hook, and drop have intentional dry/wet and center/width contrast;
- group compression/limiting is not serially fighting the instrumental group or
  the Master limiter;
- the final vocal-group chain, bypass states, and important parameters are read
  back from Live and saved.

Required evidence:

1. before/after or retained-baseline reference;
2. one meaningful variable per A/B, unless a bounded linked change is justified;
3. comparable post-FX/post-Master render;
4. deterministic audit and, when used, grounded timestamped listening notes;
5. `RETAIN`, `REVERT`, or `DEFER` decision with reason.

An unresolved P0 vocal failure is **FAIL**. A P1 vocal issue must be fixed or
explicitly deferred with an owner-visible reason before D4; “Gemini said
RETAIN” is not sufficient.

### E3 — Instrumental group bus

**Purpose:** finish the kick, bass, sub, drums, synths, and FX foundation before
asking the Master to solve group-level problems.

Evaluate:

- kick/sub ownership, phase, ducking, and second-drop foundation;
- bass movement and low-end mono stability;
- synth buildup around `250–450 Hz` and masking of the vocal group;
- drum transient/body balance and drop impact;
- pre-drop riser breath and transition cleanliness;
- upper-mid mono stability and high-hat energy around `9–14 kHz`;
- energy arc, contrast, and pacing across intro, build, drop, contrast, return,
  and ending.

The current instrumental review is a prioritized test list, not a confirmed
defect list. Each item must be confirmed or rejected by a comparable A/B and
listening evidence. Do not change bass, synth, or Master parameters merely to
respond to a generic genre expectation.

Pass requires that the instrumental group no longer masks the vocal group,
loses intended drop impact, or collapses in mono on the accepted candidate. A
shorter or otherwise incomparable render is **BLOCKED** and cannot produce a
`RETAIN` decision.

### E4 — Overall Master

**Purpose:** prepare a production-ready Master after the vocal and instrumental
groups are stable.

Before touching the Master:

- save a checkpoint and preserve the accepted group candidate;
- inspect the pre-master and confirm group problems are not being hidden by the
  final limiter;
- inventory the installed plugin options and choose a tool for the measured
  problem rather than defaulting to another stock processor;
- define the delivery target and level-matched references.

Evaluate the Master for:

- controlled transients and depth rather than maximum loudness;
- no audible serial-limiting collapse, pumping, or flattened drop impact;
- vocal intelligibility and low-end movement preserved;
- tonal balance and stereo width that survive the named references;
- true peak at or below `-1 dBTP` for the delivery candidate;
- loudness, LRA, crest, and short-term movement judged against references and
  delivery intent, not a fixed universal LUFS target;
- a fresh post-FX/post-Master bounce with matching range and complete tail.

At least two level-matched Master candidates are required when the Master is
changed materially. Record why the selected candidate wins and why the other is
rejected or retained as a reference. A louder file does not win by loudness
alone.

For this evaluation, a Master change is material when it changes the limiter
threshold or ceiling, reorders the chain, or produces a difference of at least
`1 dB` integrated LUFS between candidates. Any of those conditions requires two
level-matched candidates and a fresh E1/E4 evaluation.

Any later mix, return, or FX change invalidates the previous final-Master
evidence. Re-render and re-run E1 and E4 before advancing to D4.

### E5 — Full mix, return tracks, and FX polish

**Purpose:** make the full production feel mature EDM rather than merely
technically clean.

Evaluate every active return by musical role:

- high-pass and low-pass filtering prevent mud and uncontrolled brightness;
- sends support verse/hook/drop contrast instead of washing out the center;
- reverb and delay tails are intentional and do not obscure transitions;
- backing vocals gain depth without losing lyric support;
- vocal chops, risers, impacts, and transitions have clear space and timing;
- stereo width adds immersion without phasey or hollow mono collapse;
- automation, fades, and ending behavior feel deliberate;
- clean electronic elements frame the textured vocal character.

This stage is not permission to add devices or redesign the arrangement without
evidence. Keep the change bounded, render the same range, and re-check the
Master after any material return/FX move.

### E6 — Translation and D4 owner listening

The owner must listen to the exact final candidate in all of these states:

- normal-volume stereo;
- low-volume stereo;
- mono fold-down;
- headphones;
- phone or small speaker;
- level-matched comparison against the accepted references.

The owner must specifically check vocal intelligibility, female-hook priority,
male/female handoff, kick/sub punch, sibilance, vocal depth, transition tails,
width, phase, and hollow or metallic artifacts.

The owner records one of:

- **APPROVE D4** — no release-blocking issue remains;
- **REQUEST ONE SPECIFIC REVISION** — one passage, one audible problem, and one
  reversible test are named;
- **DEFER RELEASE** — reason and next review condition are recorded.

Vague discomfort is not an Ableton action. Convert it into a timestamped
observation and one bounded test before reopening the A/B loop.

## 5. Promotion rules

Advance a candidate only when:

1. the current stage's required artifacts exist;
2. no P0 issue is open;
3. every material change has a readback, save, comparable render, audit, and
   decision;
4. P1 issues are fixed or explicitly owner-deferred;
5. the next stage does not rely on a stale or incomparable bounce.

Release is **not approved** unless E0–E6 are complete and the maturity gate is
D4. A candidate can be musically promising and still be **BLOCKED** by missing
references, a bad render range, an unavailable audio listener, or missing owner
approval.

## 6. Evidence package

Retain only the evidence needed to reproduce the active decision:

- source `.als` and dated checkpoint;
- selected candidate WAV and SHA-256;
- accepted reference and reference-level method;
- deterministic audit report;
- grounded Gemini report, if used;
- screenshots or Live readback for UI-only changes;
- stage decision log with `PASS`, `FAIL`, `BLOCKED`, `DEFERRED`, `RETAIN`, or
  `REVERT`;
- final D4 owner listening record.

Superseded WAVs, `.wav.asd` sidecars, temporary screenshots, and superseded
reports may be moved to the Windows Recycle Bin after the decision. Never
permanently delete the source Set, source stems, or an artifact still under
audit.

## 7. Evaluation record template

Copy this block for each candidate or material A/B:

```text
Candidate:
Date/time:
Stage: E0 / E1 / E2 / E3 / E4 / E5 / E6
Exact WAV path:
SHA-256:
Exact .als/checkpoint:
Render start/length and expected duration:
Change under test:
Tracks/devices/parameters read back:
Reference(s) and level-match method:
Deterministic audit:
Gemini: PASS / AUDIO UNAVAILABLE / not used
Timestamped observation(s):
Human listening observation(s):
Result: PASS / FAIL / BLOCKED / DEFERRED
Decision (A/B): RETAIN / REVERT / DEFER
Decision (E6 only): APPROVE D4 / REQUEST ONE SPECIFIC REVISION / DEFER RELEASE
Reason:
Next gate:
Owner approval: pending / approved / deferred
```

## 8. Final definition

The evaluation is complete only when the saved Set, final post-FX/post-Master
WAV, audit evidence, reference comparison, and D4 owner decision all describe
the same candidate. Until then, report the exact open gate instead of calling
the track finished.
