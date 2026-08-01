---
name: ableton-vocalign
description: >-
  Run and verify real-time Synchro Arts VocAlign alignment in Ableton Live
  using Ableton MCP for session, track, clip, browser, device, and transport
  inspection, and Live UI control for manual audio alignment, sidechain
  routing, Vocalign capture, and artifact-safe settings. Use when aligning a
  vocal dub, harmony, ad-lib, or backing vocal to a guide track; when a request
  mentions VocAlign, sidechain vocal alignment, guide/dub capture, or manual
  pre-alignment; or when documenting the evidence and limitations of this
  workflow.
---

# Ableton VocAlign

Use this skill to align a vocal target to a guide in a live Ableton session,
with an explicit manual pre-pass, phrase-scoped Vocalign capture, conservative
artifact controls, and evidence-based handoff.

The default outcome is a configured and tested Live session, not a saved Set,
rendered file, or claim of final audio quality. Do not save, bounce, freeze, or
overwrite user work unless the user asks for that separately.

## Tool boundary

Use the legacy Ableton MCP for:

- get_session_info, get_track_info, and get_arrangement_clips;
- browser discovery and load_instrument_or_effect;
- set_arrangement_time, start_playback, and stop_playback.

Use the Live UI through the available Computer Use/node-repl bridge for:

- dragging audio clips or changing the arrangement grid;
- opening third-party plugin editors;
- selecting the Vocalign sidechain source and tap point;
- pressing Vocalign Capture and changing its controls.

The legacy MCP surface does not provide reliable warp-marker editing, precise
audio-position editing, sidechain routing, or third-party plugin parameter
writes. Do not invent MCP calls for those operations. After every UI action,
refresh the accessibility/screenshot state before the next action; element
indices and screenshots become stale.

## Workflow

### 1. Inspect and map the session

1. Stop playback and read get_session_info. Record the tempo, current
   position, playing state, track count, and whether the Live title already
   contains an unsaved-change marker.
2. Read get_track_info for the guide and target candidates. Ableton MCP uses
   zero-based indices; user-facing track numbers are normally one-based. Map
   by track name and position, never by number alone.
3. Read get_arrangement_clips for every guide and target. Compare phrase
   starts, ends, gaps, and lengths. Do not assume matching clip counts or
   matching clip names.
4. Confirm that both guide and target are audio tracks and that the intended
   phrases are present before changing anything.

For a request phrased as "track 8 to track 11" and "track 9 to track 12," the
initial mapping is usually guide MCP indices 7 and 8, target MCP indices 10
and 11. Verify this from the session instead of hardcoding it.

### 2. Manually pre-align before Vocalign

1. Set a fine arrangement grid, preferably 1/16 or finer for vocal starts,
   before dragging clips. A one-bar grid is too coarse for this operation.
2. Align obvious phrase starts, consonant entrances, and large gaps manually.
   Make the smallest reversible correction; do not stretch or warp audio when
   only a clip-start correction is needed.
3. Refresh the arrangement and independently reread the clip list after each
   meaningful correction. Record the old and new start positions.
4. If a drag snaps to an unintended bar or beat, undo immediately, refresh,
   and leave the original position rather than stacking an unverified edit.
5. Treat a target that is already within a small fraction of a beat as
   "close enough for Vocalign" if the available grid makes a finer edit risky.

A proven test result was target track 11's first clip moving from beat 7.618 to
beat 8.000 to match its guide. A target track 12 clip at beat 42.500 versus a
guide at beat 42.250 was left unchanged after a coarse-grid drag snapped to
the wrong position and was undone.

### 3. Insert VocAlign and route the guide

1. Discover the plugin rather than assuming its URI:

   get_browser_items_at_path("plugins")

   Then inspect the Synchro Arts folder and locate VocAlign 6 Pro VST.
2. Call load_instrument_or_effect on each target audio track. Re-read
   get_track_info and confirm that a VocAlign 6 Pro VST device was appended
   to each intended target.
3. Select one target at a time in Live, open its Vocalign editor, and set the
   sidechain source to the corresponding guide track.
4. Verify the route visually for both targets. The tested mapping was:

   | Target | Guide | Live sidechain tap |
   | --- | --- | --- |
   | track 11 | track 8 | "8-6 Vocals", "Post FX" |
   | track 12 | track 9 | "9-6 Vocals", "Post FX" |

   Use "Post FX" only when the guide chain has no delay, reverb, or other
   time-changing effect during capture. Otherwise choose a cleaner guide tap
   that contains the intended dry timing information.

### 4. Capture phrase by phrase

Use Vocalign's real-time VST3 workflow:

1. Work on one phrase or clearly bounded arrangement range at a time.
2. Make the intended arrangement range active and avoid leaving an old
   Vocalign overview region selected.
3. In Vocalign, arm the orange Capture control under Dub.
4. Start Ableton playback, let the guide and target phrase pass, then stop.
5. Confirm that Vocalign displays Guide, Dub, and a purple Output waveform.
6. Stop playback and inspect before moving to the next phrase.

The real-time capture guide is documented by Synchro Arts at:
https://www.synchroarts.com/manuals/VocAlign6Pro/Manual/HTML/quick-start-guide-for-vst3-real-time.html

Live/VST3 has an important quirk: when a previous overview region is selected,
Capture or playback may follow that region and jump away from the arrangement
playhead. If the host position or plugin timeline jumps unexpectedly, stop,
reselect the intended phrase, reread session state, and do not blindly repeat
the capture. A visible purple output proves that a region processed; it does
not prove that every target clip was captured.

### 5. Start with conservative artifact controls

For a normal vocal dub, use this starting profile:

- Match Timing: on.
- Match Pitch: off unless pitch matching is explicitly requested.
- Alignment Rule: Normal Flexibility.
- Maximum Shift: cap it conservatively, such as 70 ms after manual cleanup.
- Smart Align: leave off for gap-heavy phrase captures when gap jumping is a
  risk; test it later only if auditioning shows a benefit.
- High Resolution: off for ordinary vocals; enable only when the source
  warrants it and the extra processing time is acceptable.
- Formant Shift: neutral, 0%.

Normal Flexibility is the safe first pass. High Flexibility can compromise
quality when it stretches too far. For gaps, a bounded Maximum Shift is safer
than allowing points to move without limit. See Synchro Arts' timing-control
guidance:
https://www.synchroarts.com/manuals/VocAlign6Pro/Manual/HTML/adjusting-the-automatic-time-and-pitch-matching.html

These are starting controls, not a substitute for listening. If the dub
needs more than the shift cap, fix the arrangement manually or raise the cap
only after hearing the result.

### 6. Verify and hand off

Before reporting completion:

1. Stop playback and reread get_session_info; it must report
   is_playing: false.
2. Reread both target tracks and confirm the Vocalign devices remain on the
   intended tracks.
3. Reread target arrangement clips and report exact manual position changes.
4. Confirm in the Live UI that each sidechain source is still correct.
5. Confirm purple Output is visible for each claimed captured region.
6. Audition guide and target together across phrase starts, sibilants, breaths,
   held vowels, and gaps. A human listening pass is required before claiming
   artifact quality.
7. State clearly whether the result is live-plugin processing only or has been
   rendered/bounced. Do not imply a rendered file exists when it does not.
8. Preserve the user's existing unsaved state and do not save unless asked.

## Failure modes and recovery

- Wrong track: stop and remap from names plus get_track_info; never
  "correct" a device on an assumed index.
- Wrong manual snap: undo once immediately, refresh the UI, and verify the
  original clip start with get_arrangement_clips.
- Blank Vocalign editor: verify the plugin window is open, the sidechain
  source is set, the guide contains audio in the active range, and the target
  is not muted or bypassed.
- No purple Output after Capture: verify that Capture was armed before
  playback, both signals actually passed through the active range, and the
  correct guide tap was selected.
- Capture follows an old region: clear or reselect the Vocalign overview
  range, set the arrangement position again, stop any playback, and confirm
  the host position before retrying.
- Unexpected transport state: stop playback first, then inspect. Never
  assume a failed tool response had no side effect.
- Plugin settings unavailable through MCP: use the Live plugin UI and
  record only settings visibly confirmed there. Third-party devices may expose
  only Device On through get_track_info.

## Evidence standard

Separate these claims:

- Configured: device inserted and sidechain visibly routed.
- Processed: Vocalign shows a purple Output for a captured region.
- Aligned: clip positions and/or Vocalign output were compared against the
  guide.
- Approved: a human listened and accepted timing, tone, and artifacts.

Never promote "configured" or "processed" to "approved." A successful MCP
response, a visible device, or a subagent report is not evidence of audible
alignment.
