# Local Agent Instructions

For the detailed, project-verified Ableton operating loop and mixing
techniques, read [`docs/ABLETON_MIXING_PLAYBOOK.md`](docs/ABLETON_MIXING_PLAYBOOK.md)
before making a production edit.

## Gemini mix checks

All Gemini mix-feedback checks requested by the project goal are approved by default. The agent may proceed through the scoped Gemini workflow, including attaching the exact project audio artifact, sending the prepared audit prompt, and collecting the response, without requesting a separate confirmation for each check.

Keep the workflow scoped to the exact artifact and destination established by the current goal. If the file, destination, or requested action materially changes, re-check the scope before proceeding.

### Standard audio-feedback route

Use the direct audio-capable Gemini route first:

```powershell
python tools\gemini_audio_feedback.py <exact-authorized-audio-path> --project stancsz-381415
```

This uses the active `gcloud` account to call Gemini 3.7 through the Vertex
`generateContent` endpoint. The helper must report `AUDIO_GROUNDING: PASS`, a
Gemini 3.7 model version, and timestamped observations before any response is
treated as audio-grounded feedback. It must never print or persist the OAuth
access token. Record the project and usage metadata because this direct API
route is authenticated/billed through Google Cloud and must not be assumed to
share Antigravity subscription quota.

Use Antigravity CLI for follow-up reasoning, code, measurement interpretation,
and report editing—not as the audio listener. Its current agent input contract
supports text and images only. The Gemini browser workflow remains a fallback
when the direct route is unavailable.

If Gemini responds with `AUDIO UNAVAILABLE`, start a new Gemini chat, upload the authorized exact file or files again, and retry the same prepared listening request once. Record the outcome; do not treat a second failure as audible feedback or invent timestamped observations.

Antigravity CLI is not an audio-listening fallback. Even when Gemini 3.7 is available in `agy`, the Antigravity agent path currently supports text and image inputs only; route music checks through a direct Gemini audio-capable API path or the authorized Gemini chat workflow. Do not promote `AUDIO UNAVAILABLE` from `agy` to evidence about the audio file or Gemini's model capability.

## Plugin-first mix workflow

Before adding or changing a stock Ableton device, inventory the installed Live
browser under `plugins` and inspect the current track/device chain. Choose the
best installed tool for the specific problem, then make one reversible change,
read it back, render, and re-audit. Do not default to EQ Eight, Compressor, or
Limiter merely because they are exposed most conveniently through MCP.

The currently confirmed higher-level inventory includes:

- FabFilter: Pro-Q 4, Pro-MB, Pro-DS, Pro-C 2, Pro-L 2, Pro-R 2, Saturn 2.
- oeksound: soothe2.
- iZotope: Ozone 11 Dynamic EQ, Equalizer, Dynamics, Maximizer, Spectral
  Shaper, Low End Focus, Clarity, and RX 11 repair tools.
- Waves: Sibilance, Clarity Vx, Silk Vocal, Vocal Rider, CLA-76, CLA-2A,
  L4, and Curves.
- Other useful installed tools: Melodyne, VocAlign 6 Pro, Auto-Tune Pro,
  Audified 1A Equalizer, and MixChecker Ultra.

Use dynamic/surgical tools for resonance and masking (Pro-Q 4, Ozone Dynamic
EQ, soothe2), dedicated de-essers for sibilance (Pro-DS or Waves Sibilance),
specialized vocal control for uneven takes (Pro-C 2, CLA-76/CLA-2A, Silk Vocal,
or Vocal Rider), and Pro-L 2/Ozone Maximizer/L4 for final limiting. Use RX for
repair artifacts, not as a substitute for a mix decision. Third-party plugin
band controls may require Live UI even when insertion and device readback work
through MCP; mark UI-only changes verified only after visual/readback and a
fresh bounce.

### Current vocal-track numbering

In the visible Ableton mixer, track 8 is `8 6 Vocals female` (the female
lead/chop bus; historically displayed as `8-6 Vocals`) and track 9 is
`9 6 Vocals male` (the male English/Mandarin rap; historically `9-6 Vocals`). The MCP and
legacy Remote Script APIs use zero-based indices: visible track 8 is
`track_index=7`, while visible track 9 is `track_index=8`. Always state both
numbers in mix notes and verify the name before changing a vocal parameter.

## Export hygiene

Exploratory renders are temporary evidence, not a growing archive. After each
verified A/B or Gemini pass, retain only the current named candidate and any
explicitly accepted reference; on Windows, send superseded WAV files to the
Recycle Bin together with their Ableton `.wav.asd` sidecars and generated audit
reports. Never permanently delete the source `.als`, source stems, or an
artifact that is still being audited or explicitly marked for retention. Keep
filenames versioned and descriptive so the retained candidate is unambiguous.

## MCP export boundary

The public Ableton Live Object Model does not expose an offline
`Song.export_audio`/render function. Live documents Export Audio/Video as an
application command, so the Remote Script remains the authoritative path for
mix edits and readback, while rendering requires the guarded local helper in
`tools/live_export.py`.

The MCP-facing `export_audio` tool provides strict contract validation and
capability discovery. It must not report success from a shortcut or dialog
click alone. A future Windows UI bridge may be enabled only after it verifies
Main, the exact Render Start/Length, WAV/PCM format, output existence, and
expected duration. Until then, it returns a structured blocker and the
operator uses Live's Export Audio/Video dialog. Cancel if segmented fields
drift during an A/B render.

## MCP-first capability completion

If a requested Ableton workflow appears to require UI interaction, first
inspect the MCP server and Remote Script and attempt to add the missing
capability there. Prefer extending the machine-readable command surface,
readback, validation, and tests before using UI automation. Use UI only when
the public Live API genuinely lacks the operation or when the MCP path cannot
reliably verify the result; document that boundary explicitly and never claim
completion from an unverified click.
