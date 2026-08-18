---
name: ableton-mix-audit
description: >-
  Audit an Ableton Live mix for technical safety, mix-maturity risks, vocal and
  low-end consistency, stereo/mono compatibility, loudness, dynamics, spectral
  balance, and release readiness. Combine read-only Live/MCP inspection and a
  local deterministic WAV audit with an optional, explicitly authorized Gemini
  listening review. Use when the user asks whether a mix is mixing well,
  sounds mature, is ready to master or release, needs a mix QC report, or wants
  deterministic checks plus a second set of ears.
---

# Ableton Mix Audit

Produce an evidence-bounded mix audit. The outcome is a risk profile and a
human-listening checklist, not a fabricated 0-100 quality score. Metrics prove
technical properties or proxies; Gemini supplies timestamped listening
hypotheses; neither proves that the song is ready without human A/B listening.

## Non-negotiable boundaries

- Read the current Live session before editing. Preserve unrelated changes and
  do not alter the Master chain during an audit.
- Prefer a saved project and an authoritative full Main-path render in lossless
  WAV. If no exact render path is supplied, ask before exporting a copy; never
  search personal folders or overwrite the source.
- Use the legacy Ableton MCP for session, track, clip, device, routing, and
  Master inspection when available. On Live editions without Extensions, use
  Live's export UI for the audio render and this skill's local analyzer.
- Treat device presence, screenshots, meter readings, a successful MCP call,
  or a Gemini text response as configuration/review evidence only. Do not say
  that a mix sounds professional unless a human actually listened.
- Do not auto-fix during an audit. If the user later requests a fix, change one
  meaningful variable, render the same Main path, level-match the A/B, and
  record keep/revert/defer evidence.
- Treat exploratory renders as temporary evidence. After a verified A/B or
  Gemini pass, retain only the current named candidate and any explicitly
  accepted reference. On Windows, send superseded WAVs to the Recycle Bin
  together with their Ableton `.wav.asd` sidecars and generated audit reports.
  Never permanently delete source `.als` files, source stems, retained
  references, or an artifact still being audited.

## Project-learned Ableton operating rules

Read [`../../docs/ABLETON_MIXING_PLAYBOOK.md`](../../docs/ABLETON_MIXING_PLAYBOOK.md)
before editing this project. It records the verified control loop and the
current vocal map. The essential rules are:

- Map returned track names to visible Live numbers and zero-based MCP indices;
  do not trust a stale screenshot. Current visible track 8 / MCP index 7 is
  `8 6 Vocals female`, while visible track 9 / MCP index 8 is
  `9 6 Vocals male`.
- Inspect first, ask Gemini for one ranked audible hypothesis, change one
  meaningful parameter, read it back, save in Live, render the same Main path,
  and re-audit before another change.
- Prefer the best installed plugin for the job (Pro-Q 4/Pro-MB/soothe2 for
  dynamic resonance, Pro-DS/Sibilance for sibilance, Vocal Rider/Pro-C 2 for
  uneven level, RX for repair); do not stack processors merely because they
  are available.
- Keep the Master unchanged unless the user explicitly authorizes a Master
  change. Do not add another low-mid cut when existing overlapping cuts already
  explain the hypothesis; a fresh listen can justify deferring it.
- Use the direct Gemini audio route and require `AUDIO_GROUNDING: PASS` plus
  timestamped observations. On `AUDIO UNAVAILABLE`, start a new chat, upload
  the exact file again, and retry once; Antigravity text/image output is not
  audio evidence here.
- Retain only the current candidate, accepted reference, and reproducibility
  evidence. Recycle superseded WAVs, `.wav.asd` sidecars, temporary screenshots,
  and superseded reports after each accepted A/B.
- Verify Live's segmented Render Start/Length fields after UI edits. If the
  range differs from the authoritative A/B range, cancel the export instead of
  producing an incomparable candidate.

## Audit modes and evidence states

Use `mix` for mix-risk analysis, `pre-master` for headroom/dynamics before a
master chain, and `release` for delivery checks. Use these decision states:

- `NOT_AUDITABLE`: no valid authoritative render or required input is missing.
- `TECHNICAL_FAIL`: decode, integrity, or hard delivery failure.
- `MIX_RISK_REVIEW`: deterministic warnings need investigation.
- `HUMAN_LISTENING_REQUIRED`: evidence exists but audible gates remain.
- `READY_FOR_HUMAN_RELEASE_DECISION`: no known automated blocker; the user
  still owns the final release decision.

Use evidence levels as maturity of the audit, not as a quality grade:

- `D0`: no reliable render;
- `D1`: file/project is technically readable;
- `D2`: loudness, dynamics, spectrum, and stereo risks checked;
- `D3`: reference and relevant stem checks added;
- `D4`: human stereo/mono/translation A/B completed.

## Workflow

### 1. Establish the baseline

Record the Live title and unsaved marker, tempo, transport state, sample rate,
project length, track/group names, routing, mute/solo/arm state, device order,
and the complete Master chain. Map tracks by returned names and topology, not
stale UI numbers. Record the exact render path and a hash when possible.

For a useful first run, request:

- one full-track WAV;
- optional vocal, drums, and bass stems;
- optional level-matched reference tracks;
- the user's genre/delivery brief.

Without stems, report kick/bass attribution, vocal masking, and stem phase as
`unknown` rather than guessing.

### 2. Run the local deterministic audit

Run the bundled script on the exact supplied WAV:

```powershell
python skills/ableton-mix-audit/scripts/mix_audit.py `
  "C:\path\full-mix.wav" `
  --mode mix `
  --reference "C:\path\reference.wav" `
  --vocal "C:\path\vocal.wav" `
  --json-out "C:\path\audit\mix-audit.json" `
  --report-out "C:\path\audit\mix-audit.md"
```

The analyzer accepts PCM WAV and never silently converts or uploads it. It
always reports unavailable optional measurements rather than inventing them.
It checks file integrity, duration/silence, sample peak, optional ffmpeg
LUFS/LRA/true peak, crest factor, section-level RMS proxy, L/R correlation,
mono loss, spectral bands, level-matched reference deviation, and optional
vocal active-window dynamics. Read `references/check-matrix.md` for
interpretation and limits.

Important interpretation rules:

- `true peak <= -1 dBTP` is a conservative release-delivery gate, not proof of
  a good mix;
- pre-master headroom is a target to compare with the brief, not a universal
  pass/fail number;
- vocal median mismatch around 1 dB and active-window spread around 6 dB are
  A/B starting heuristics, not genre-independent failures;
- spectral warnings are strongest against a level-matched reference; without
  one, describe the spectrum but do not call it wrong;
- negative correlation or mono loss is a reason for a width/mono A/B, not an
  automatic order to collapse the track.

### 3. Optional Gemini listening audit

Use `$gemini-mix-feedback` as the browser/upload layer. Require the exact local
path, classify it as `full-track` or `stem`, and name Google Gemini as the
destination. One attachment is the default. Obtain action-time confirmation
immediately before Send; never automate sign-in, CAPTCHA, or security prompts.

Ask Gemini to listen before answering and return, for each of the top issues:

```text
priority P0/P1/P2 -> timestamp -> audible observation -> likely cause
-> testable Ableton action -> confidence
```

Require it to say `AUDIO UNAVAILABLE` if it could not access or hear the file.
Treat that result, filename-only commentary, or generic notes without audio
timestamps as `unverified`. Do not give Gemini local metrics first in the
initial listening pass; avoid anchoring its ears to the machine's hypothesis.

### 4. Reconcile evidence

- Deterministic warning + Gemini timestamped agreement: high-priority A/B
  candidate.
- Gemini-only finding: possible psychoacoustic, arrangement, or artifact issue;
  require human listening and a targeted Ableton test.
- Deterministic-only warning: machine risk; do not label it audible failure.
- No finding: no evidence found, not proof that the mix is mature.

Keep disagreements in the report. Never average the two sources into a single
score.

### 5. Close with human gates

List exact passages to hear in stereo and mono: vocal intelligibility, kick and
bass translation, pumping/transients, sibilance/harshness, depth, width,
tuning or phase artifacts, and a low-volume/reference comparison. The audit is
not release-approved until the user has listened and accepted those gates.

## Handoff format

End with the compact structure below and also preserve the JSON artifact:

```text
Baseline: [project state, render path, hash, format]
Decision: [state] / Evidence level: [D0-D4]
Hard gates: [pass/fail/unknown with measured values]
Deterministic warnings: [metric -> evidence -> risk]
Gemini findings: [verified/unverified, timestamp -> observation -> test]
Crosswalk: [agreement, disagreement, or machine-only risk]
Human listening required: [exact passages and checks]
Open risks: [only evidence-backed or explicitly unknown items]
```

Read `references/check-matrix.md` for check semantics and
`references/mix-audit.schema.json` before changing the report contract. The
existing `skills/gemini-mix-feedback/SKILL.md` remains the source of truth for
Windows Computer Use and Gemini upload safety.
