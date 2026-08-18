# Mix audit check matrix

The matrix separates hard technical gates, useful proxies, and questions that
still require ears. Thresholds are starting heuristics. Prefer the user's
delivery brief and level-matched references over universal targets.

| ID | Evidence | Default interpretation | Class | Main limitation |
|---|---|---|---|---|
| `decode_integrity` | PCM WAV opens and has finite samples | Fail on unreadable, empty, or malformed input | Hard gate | Does not prove musical quality |
| `duration_and_trim` | Duration plus leading/trailing RMS windows | Warn on suspicious silence or abrupt trim | Proxy | Intentional intros/outros are valid |
| `sample_peak` | Maximum decoded sample | Fail at/near 0 dBFS; warn near ceiling | Hard gate | Sample peak is not true peak |
| `true_peak` | ffmpeg `loudnorm` input true peak | Apply `<= -1 dBTP` only for conservative release delivery | Delivery gate | A mix can be quiet and poor |
| `loudness` | Integrated LUFS, short-term proxy, LRA | Compare with brief and references | Proxy | Loudness is not balance |
| `dynamics` | Crest factor and block RMS spread | Low values can indicate over-control | Proxy | Genre and arrangement change the target |
| `section_rms` | Block/window RMS changes | Locate abrupt section jumps for listening | Proxy | Automatic section boundaries are approximate |
| `spectral_shape` | Relative energy in eight frequency bands | Describe first; compare against reference to warn | Proxy | Tonal taste is not a fixed target |
| `stereo_correlation` | Windowed/full L/R correlation | Sustained negative values justify phase A/B | Proxy | Wide music can correlate poorly intentionally |
| `mono_loss` | Stereo RMS versus mono-sum RMS | Large loss justifies mono/width A/B | Proxy | Other elements can mask cancellation |
| `reference_deviation` | Level-matched band-share delta | Flag large band deviations for listening | Proxy | Reference choice controls the conclusion |
| `vocal_active_rms` | Active-window p10/median/p90 | Around 1 dB lane mismatch or 6 dB spread is an A/B starting point | Stem proxy | One vocal file cannot prove full-mix placement |
| `low_end_attribution` | Kick/bass stem comparison | Only run when stems exist | Unknown otherwise | Full mix cannot identify the cause |
| `live_session_hygiene` | MCP/UI state, routing, devices, saves | Report accidental mute/solo/bypass/routing risks | Deterministic config | Device presence is not audible success |

## Status semantics

- `pass`: the measured property did not trigger the configured heuristic;
- `warn`: a proxy or delivery risk needs review;
- `fail`: a hard technical gate failed;
- `unknown`: the input or tool needed for the check is absent.

The analyzer does not turn `unknown` into `pass`. A report with no warnings is
still closed with a human-listening gate.

## Reference comparison

Compare relative band shares after level matching. Do not compare raw FFT
levels from files with different loudness and call the louder file brighter.
The bundled analyzer reports the delta; the user decides whether a difference
is intentional.
