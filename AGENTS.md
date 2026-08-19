# Local Agent Instructions

For the detailed, project-verified Ableton operating loop and mixing
techniques, read [`docs/ABLETON_MIXING_PLAYBOOK.md`](docs/ABLETON_MIXING_PLAYBOOK.md)
before making a production edit.
For the targeted question matrix and Gemini token routing, also read
[`docs/GEMINI_TARGETED_MIXING_PROTOCOL.md`](docs/GEMINI_TARGETED_MIXING_PROTOCOL.md).

## Gemini mix checks

All Gemini mix-feedback checks requested by the project goal are approved by default. The agent may proceed through the scoped Gemini workflow, including attaching the exact project audio artifact, sending the prepared audit prompt, and collecting the response, without requesting a separate confirmation for each check.

Keep the workflow scoped to the exact artifact and destination established by the current goal. If the file, destination, or requested action materially changes, re-check the scope before proceeding.

### Standard audio-feedback route

Use the direct audio-capable Gemini route first:

```powershell
python tools\gemini_audio_feedback.py <exact-authorized-audio-path> --project stancsz-381415 --profile compact --focus "one issue"
```

This uses the active `gcloud` account to call Gemini 3.7 through the Vertex
`generateContent` endpoint. The helper must report `AUDIO_GROUNDING: PASS`, a
Gemini 3.7 model version, and timestamped observations before any response is
treated as audio-grounded feedback. It must never print or persist the OAuth
access token. Record the project and usage metadata because this direct API
route is authenticated/billed through Google Cloud and must not be assumed to
share Antigravity subscription quota.

### Token-efficient Gemini listening loop

Gemini text output is the expensive prediction side of this workflow. Keep
iterative A/B checks compact and scoped: use one exact candidate, one specific
focus, and preferably `--profile taste` (default `maxOutputTokens=420` and the
verified current-route `thinkingBudget=0` compatibility setting). Taste returns only an answer, two timestamped audible
reasons, and one action; it is for musical comfort, emotional focus, texture,
and A/B preference. Use `--profile compact` (`maxOutputTokens=420`) only when a
short ranked issue list is genuinely needed. Both profiles let the helper reuse
a matching report for the same audio SHA/model/focus. Use `--no-cache` only when
a genuinely fresh opinion is needed. Do not ask Gemini to restate the entire
mix history or write a long tutorial.

Do not ask the single-file helper to compare against an unattached version: ask
what the current file feels like, or attach/use a separately prepared comparison
workflow. The current `gemini-3.7-flash` endpoint rejected
`thinkingLevel=MINIMAL` during verification, so the helper intentionally uses
the accepted legacy zero-budget setting by default and records it in the
sidecar. `--thinking-level LOW` remains an explicit, opt-in experiment.

For a localized A/B, create an explicitly named 15--30 second PCM diagnostic
excerpt from the exact WAV and call `--kind excerpt --focus "..."`; treat that
answer as local troubleshooting evidence only, never as a release verdict.
After the final candidate is selected, run exactly one complete full-track
release audit with `--profile release` (the helper caps it at 600 output tokens)
and keep its report. This concentrates long output on the one decision that
actually needs it while preserving a full-file `AUDIO_GROUNDING: PASS` gate.

Use Antigravity CLI for follow-up reasoning, code, measurement interpretation,
and report editing—not as the audio listener. Its current agent input contract
supports text and images only. The Gemini browser workflow remains a fallback
when the direct route is unavailable.

If Gemini responds with `AUDIO UNAVAILABLE`, start a new Gemini chat, upload the authorized exact file or files again, and retry the same prepared listening request once. Record the outcome; do not treat a second failure as audible feedback or invent timestamped observations.

Antigravity CLI is not an audio-listening fallback. Even when Gemini 3.7 is available in `agy`, the Antigravity agent path currently supports text and image inputs only; route music checks through a direct Gemini audio-capable API path or the authorized Gemini chat workflow. Do not promote `AUDIO UNAVAILABLE` from `agy` to evidence about the audio file or Gemini's model capability.

### MCP dataset privacy boundary

Gemini mix-check approval does not authorize contributing Ableton prompts or
device settings to the open Ableton MCP training dataset. For direct stdio MCP
operations in this project, set `ABLETON_MCP_DISABLE_DATASET=true` unless the
user explicitly opts into that separate dataset contribution. Keep the
machine-readable MCP control/read/export workflow; do not relay the dataset
consent prompt as if it were Gemini approval.

### Recovering stale Codex Ableton access

Treat the Live Remote Script, the Codex stdio MCP process, Computer Use, and
Live's Export Audio/Video command as separate layers. A Live export crash can
remove the Remote Script socket on port 9877 without explaining a stale Codex
tool binding, and a successful direct stdio smoke proves only the server-to-Live
path, not that the current task's native `mcp__ableton__*` proxy has rebound.

For this machine, keep the Codex `ableton` MCP environment configured with both
`ABLETON_MCP_UI_EXPORT=1` and `ABLETON_MCP_DISABLE_DATASET=true`. If native
Ableton tools disappear or return `Transport closed` while Live and a fresh
stdio client still work, recover the Codex binding as follows:

1. Open Codex Settings with `Ctrl+,` and search settings for `MCP`.
2. Open the MCP servers manager. If it is not directly exposed, use Keyboard
   shortcuts to assign a temporary shortcut to `Configure MCP servers` and
   invoke it.
3. Use the manager's global `Restart` button. Expect the active MCP call to
   abort because all MCP transports are restarting, then continue in the next
   turn after the tool catalog rebinds.
4. Verify native `get_session_info` succeeds without a dataset-consent prompt.
   Separately verify Computer Use with the dedicated Node REPL runtime:
   `await import("@oai/sky")`, `list_windows`, then `get_window_state` for Live.
5. Remove any temporary keyboard shortcut created for recovery.

Do not kill an individual Ableton MCP child process to refresh its environment;
that can strand the current task's transport. A per-server off/on toggle,
`Ctrl+R` renderer reload, or restarting only `codex-code-mode-host.exe` can
respawn processes without refreshing the outer native tool proxy. Do not
restart Live unless Live itself is unresponsive or the Remote Script/socket is
actually absent. If a Computer Use action invalidates the Node REPL execution
context, reset the Node REPL and re-import `@oai/sky`.

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

## Evidence routing: visual first, Gemini taste second

For each suspected issue, route evidence by capability. Use MCP and local audit
for exact track/device state, parameter readback, LUFS, true peak, correlation,
and A/B hashes. Use the installed plugin meters or analyzers for visible
frequency peaks, dynamic gain reduction, de-essing activity, stereo width, and
limiter behavior (Pro-Q 4, soothe2, Pro-C 2, Pro-DS, Pro-L 2, Ozone, or the
best existing device in that chain). Use UI only when the plugin's internal
graph is not exposed through MCP, and record the visual observation.

Use Gemini's `taste` profile only after that preflight, with one human question
that contains one target, one contrast, and one decision:
whether the drop feels too boomy versus intentionally heavy, whether the vocal
feels emotionally forward, whether an A/B feels smoother without becoming dull,
or whether a texture feels intentional rather than broken. Ask for one answer,
two timestamps, and one action. Do not ask Gemini to recreate a spectrum
analyzer or write a generic five-section mix lecture. The loop is:

`MCP/local metrics -> one plugin visual graph -> one targeted Gemini taste check -> one MCP change -> same check`

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

The MCP-facing `export_audio` tool provides strict contract validation and a
guarded Windows bridge. When `ABLETON_MCP_UI_EXPORT=1` is explicitly enabled,
it drives Live's Export Audio/Video dialog, sets the project-verified Main
range, writes a filename in Downloads, and verifies the resulting WAV's
format, output existence, and expected duration. It must never report success
from a shortcut or dialog click alone. The current verified bridge is Windows
only, 44.1 kHz / 24-bit WAV, Main-only, and refuses to overwrite an existing
file. Cancel if segmented fields drift during an A/B render.

This is still an MCP operation: `export_audio` is the standard caller-facing
path and the Windows dialog is only its implementation bridge. The public Live
Object Model has no native offline render method, so the bridge must foreground
Live for the application-owned render step; callers must not start a separate
manual UI export. The bridge now uses exact clipboard filename replacement,
dynamic timeout handling, and post-render WAV/duration/format validation. A
direct stdio MCP smoke against the current repository is the fallback proof
when an already-running Codex client has a stale tool catalog; refresh/restart
that client before treating its advertised tools as authoritative.

For this Live/Common Dialog build, use a short unique basename for export
outputs (for example `mcp-v103.wav`) and rename/document the candidate after
the validated bounce. Long basenames can leave Live's internal filename cache
on the previous export even when the visible field appears changed. The bridge
must refuse overwrite confirmation and must fail fast if an existing WAV changes
while the requested output is absent; never treat that mismatch as a successful
MCP export.

## Antigravity/Gemini CLI boundary

`agy` is available as a Gemini-capable reasoning CLI and may be used for mix
planning, code inspection, and debugging. It is not currently an audio listener:
the verified smoke test against a local WAV returned `AUDIO_GROUNDING: FAIL` with
`unsupported mime type audio/wav`. Do not use an `agy` text response as audible
Gemini feedback or as a release decision. For listening feedback, use the
approved direct Gemini 3.7 audio route (or the documented browser upload fallback)
and require `AUDIO_GROUNDING: PASS` plus timestamps. `agy` remains a useful
secondary reasoning option, not a substitute for the audio-capable route.

The MCP-facing `save_set` tool is the standard save entry point. Because the
public Live Object Model also has no portable save function, its guarded Windows
bridge sends `Ctrl+S` only when Live's title reports a dirty Set and verifies
that the `*` marker disappears. It must return `saved` or `already_saved`; a
Save-As prompt or a lingering marker is a blocked result, not a successful
save. Before focusing Live it clears only known stale Export Audio/Video and
Save Audio File dialogs left by a failed diagnostic/export; this prevents a
modal dialog from swallowing Ctrl+S.

## MCP-first capability completion

If a requested Ableton workflow appears to require UI interaction, first
inspect the MCP server and Remote Script and attempt to add the missing
capability there. Prefer extending the machine-readable command surface,
readback, validation, and tests before using UI automation. Use UI only when
the public Live API genuinely lacks the operation or when the MCP path cannot
reliably verify the result; document that boundary explicitly and never claim
completion from an unverified click.

  After adding or changing an MCP tool, restart or refresh the MCP server/client
  before treating the tool catalog as authoritative. An already-running client
  can keep an older tool schema even when the local server source and direct
  registration check already contain the new tool.

  ### Mixer level readback

  `get_track_volume_info` and `set_track_volume_value` are the preferred MCP
  path for static track-level trims. They read/write Live's normalized mixer
  value and include `str_for_value()` samples, so changes must be recorded in
  displayed dB rather than guessed from the normalized number. In the current
  Live set, `0.85 = 0.0 dB` and `0.90 = +2.0 dB`; Track 9's verified v115 trim
  used the latter. `set_arrangement_clip_gain` is only a bounded fallback: Live
  rejected the requested +2 dB clip-gain move in this set, so it must not be
  treated as a general level-automation substitute. Phrase-specific rides and
  breakpoint envelopes remain UI-only until a tested machine-readable write
  surface exists.

  ### Arrangement automation boundary

  The current Live Object Model exposes Arrangement clip markers and envelope
  presence/clearing, but not a reliable public write operation for inserting
  automation points or drawing a return/send envelope. Therefore local
  automation requests such as a phrase-specific reverb throw, return fade, or
  riser dip must remain explicitly `UI-only / unverified` until a machine-
  readable API is added and tested. Do not claim that a static device
  parameter change substitutes for time-specific automation. If UI control is
  available, use it only after recording the exact lane, time range, parameter,
  and post-change readback/fresh bounce; otherwise defer the change and keep
  the reproducible MCP candidate unchanged.
