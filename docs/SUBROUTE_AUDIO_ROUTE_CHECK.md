# Subroute audio route check — 2026-10-01

The owner requested local Subroute on port 4000 instead of Gemini keys.
`tools/gemini_audio_feedback.py` now sends exact WAV/MP3 bytes to
`http://127.0.0.1:4000/v1/chat/completions` with `gemini-subscription`.
There is no Vertex/gcloud/direct-key fallback. The gateway's explicit audio
route disables Advisor for the request without changing saved policy.

Validation: 26 focused tests passed and `git diff --check` passed. Tests cover
exact audio bytes, localhost destination and proxy/redirect isolation, gateway
key redaction, cache separation, oversized input rejection, malformed responses,
unexpected models, missing usage, and truncated/refused listening responses.

A live taste request used a generated diagnostic WAV, not a project mix:

- PCM mono, 16 kHz, 16 bit, 10 seconds; 330 Hz for 0–5 seconds, then 880 Hz.
- SHA256: `6472470B2ED4A8F9A1EB49CCCFEC80E081261B0FF96D04EDBF645DAAF74B1D3B`.
- Response ID: `chatcmpl-agy-7a561309ac86`; model alias `gemini-subscription`.
- Finish reason: `stop`; helper schema gate: `AUDIO_GROUNDING: PASS`.
- Provider usage: 3351 prompt, 4172 completion, 7523 total tokens.
- Requested output budget: 420; subscription limits are backend-managed.
- The gateway does not attest the underlying model version.

The response incorrectly reported a steady tone and described 00:05 as the
finish. It missed the known change at 5 seconds. **Transport succeeded;
perceptual accuracy failed this synthetic check.** The helper's grounding gate
checks the completed route, usage, and response schema, not whether audible
claims are correct. This is not a mix or release verdict.

The original diagnostic WAV and response were retained in the task's temporary
directory as `ableton-subroute-route-smoke.wav` and
`ableton-subroute-route-smoke.md`. No project audio was uploaded for this check.
