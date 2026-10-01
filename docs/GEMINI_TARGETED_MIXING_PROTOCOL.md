# Targeted Gemini Mixing Protocol

Gemini is most valuable here as a second set of human-like ears. It should not
spend prediction tokens reproducing information that Ableton, the local audit,
or an installed analyzer can already show. This protocol is the default for
iterative EDM mixing.

## The two-lane workflow

Use the smallest capable tool for each question:

| Question type | First evidence | Gemini question | Typical action |
|---|---|---|---|
| Spectrum, resonance, masking | Pro-Q 4 or Ozone Dynamic EQ graph | “Does this resonance make the part feel harsh or distracting?” | one narrow dynamic band |
| Sibilance or piercing hook | Pro-DS, Waves Sibilance, or dynamic Pro-Q band | “Is the hook painfully sharp, or is the brightness musical?” | adjust existing de-esser threshold/range |
| Kick/sub relationship | local LUFS/peak audit plus Pro-Q/Ozone low-end view | “Does the drop feel boomy, or intentionally heavy and controlled?” | one sidechain/low-end change |
| Vocal placement | fader, RMS, center/width, and chain readback | “Does the vocal feel emotionally forward, or buried behind the instrumental?” | one level or masking change |
| Depth and texture | reverb/delay returns, soothe2/Saturn/space chain | “Does this texture feel intentional and immersive, or distracting and cheap?” | one send, saturation, or repair change |
| Punch and pumping | Pro-C 2/CLA/L4/Pro-L gain-reduction display | “Does the groove breathe, or does compression make the drop feel flattened?” | one threshold/release change |
| Stereo translation | Ozone Imager/Utility plus correlation and mono loss | “Is the width exciting while staying solid in mono, or phasey?” | one width/utility change |

The visual lane answers *where* and *how much*. Gemini answers *whether the
result feels good, intentional, and emotionally useful*. Do not ask both tools
to solve the same measurable problem.

## One candidate, one question

Before a Gemini call, prepare:

1. One exact, validated WAV candidate.
2. One named issue and the plugin graph or meter observation that motivated it.
3. One question with one contrast and one decision: “too X, or intentionally
   Y?”
4. One reversible Ableton parameter that could test the answer.

Good questions:

```text
does the female hook still feel piercing in the 6-9 kHz region, or is the brightness controlled and musical? Judge this file alone.
does the male verse feel too dry and distant, or intentionally direct and intimate? Judge this file alone.
does the drop feel too boomy, or intentionally heavy and controlled? Judge this file alone.
does the vocal texture feel like a deliberate lo-fi character, or like a distracting artifact?
```

Bad questions combine several briefs (“check everything, compare all vocals,
master it, and tell me what plugins to add”). Split those into separate calls.
The helper rejects an overlong or multi-question `taste` focus so this mistake
does not silently spend output tokens.

## Subscription audio route

Use `python tools\gemini_audio_feedback.py <exact-authorized-wav-or-mp3>`.
The helper sends exact bytes as Chat `input_audio` to local Subroute at
`http://127.0.0.1:4000/v1/chat/completions` with `gemini-subscription`.
No Gemini API key, Vertex, or gcloud fallback is permitted. An optional
`SUBROUTE_API_KEY` authenticates only to the gateway. Require a completed
subscription response with provider usage and the timestamped grounded schema;
retain the response ID, route, and audio hash. The underlying model version is
not attested by the returned alias. The gateway verifies binary attachment reads
and disables Advisor for audio without changing its saved routing policy.

Only PCM WAV/MP3 up to 20 MiB is supported. Do not automatically convert or
compress a larger candidate; use an explicitly prepared compatible full file
for a release audit. An excerpt remains diagnostic evidence only.

## Profile and token routing

| Stage | Profile | Use | Requested output budget |
|---|---|---|---:|
| Fast musical A/B | `taste` | one human listening decision | 420 |
| Short issue triage | `compact` | up to three ranked issues when taste is not enough | 420 |
| Final release evidence | `release` | one complete full-track blocker/checks report | 600 |

Use `--no-cache` only when the same file and focus need a genuinely fresh
opinion. Output and thinking limits are subscription-backend-managed; these
budgets are requests, not enforced caps. A cached report is valid for the same
audio SHA, model, Subroute route/destination, profile,
kind, normalized focus, and generation budget. Do not run a release audit after
every parameter move; run it once after the candidate is selected.

## Decision loop

```text
MCP/readback + local audit
        -> one installed plugin graph or meter
        -> one targeted Gemini taste question
        -> one reversible MCP change
        -> save + validated export
        -> same question on the new exact WAV
        -> retain / revert / defer
```

Interpretation rules:

- `AUDIO_GROUNDING: PASS` plus `ACTION: NONE` means retain the candidate unless
  a stronger local or human reason contradicts it.
- The helper's PASS gate verifies the completed subscription route, provider
  usage, and timestamped response schema. It does not prove perceptual accuracy.
  The port-4000 synthetic smoke on 2026-10-01 completed successfully but missed
  a known pitch change at 5 seconds; see `docs/SUBROUTE_AUDIO_ROUTE_CHECK.md`.
- If Gemini and the visual evidence disagree, do not average them into a new
  setting. Narrow the question or defer the change.
- A taste pass is not a release verdict. Use the `release` profile only on the
  selected full-track candidate, then leave the D4 human stereo/mono/
  translation listen open.
- A stem or excerpt can diagnose a local texture, but cannot prove full-mix
  balance or release readiness.

## Plugin-first inspection order

Use the best already-installed analyzer in the affected chain. Prefer visual
inspection of Pro-Q 4, Ozone Dynamic EQ, soothe2, Pro-DS/Sibilance, Pro-C 2,
Pro-L 2, Ozone, or L4 before inserting another processor. If MCP exposes the
parameter, make the change through MCP and read it back. If only the plugin's
internal graph is visible in Live, use UI for inspection, record what was
seen, and require a fresh export before treating it as evidence.

This workflow is MCP-first even when Live's application-owned renderer needs
the guarded export bridge. Direct stdio MCP calls must set
`ABLETON_MCP_DISABLE_DATASET=true` unless the user separately opts into the
public Ableton MCP training dataset.
