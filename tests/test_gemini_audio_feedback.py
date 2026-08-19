from pathlib import Path

import tools.gemini_audio_feedback as feedback

from tools.gemini_audio_feedback import (
    _cached_report_matches,
    _has_grounded_schema,
    audio_mime_type,
    build_prompt,
    validate_focus,
)


def test_audio_mime_type_accepts_common_mix_formats() -> None:
    assert audio_mime_type(Path("mix.WAV")) == "audio/wav"
    assert audio_mime_type(Path("mix.mp3")) == "audio/mpeg"


def test_prompt_requires_audio_grounding_and_timestamps() -> None:
    prompt = build_prompt("full-track", "focus on low-end translation")

    assert "listen to the entire attached full mix" in prompt
    assert "HEARD_AUDIO" in prompt
    assert "AUDIO UNAVAILABLE" in prompt
    assert "low-end translation" in prompt


def test_compact_prompt_caps_issue_count_and_excerpt_scope() -> None:
    prompt = build_prompt("excerpt", "kick/sub collision", "compact")

    assert "listen only to the attached excerpt" in prompt
    assert "Return at most three issues" in prompt
    assert "Do not generalize beyond this excerpt" in prompt


def test_taste_prompt_is_one_question_and_not_a_technical_report() -> None:
    prompt = build_prompt("full-track", "does the drop feel too boomy?", "taste")

    assert "ANSWER: yes/no or A/B choice" in prompt
    assert "ACTION: one mix action" in prompt
    assert "Do not write a technical tutorial" in prompt
    assert "do not list unrelated mix problems" in prompt


def test_taste_focus_is_limited_to_one_short_question() -> None:
    assert validate_focus("  does the hook feel too sharp or musical?  ", "taste") == (
        "does the hook feel too sharp or musical?"
    )


def test_taste_focus_rejects_multiple_questions() -> None:
    try:
        validate_focus("is it harsh? is it too loud?", "taste")
    except ValueError as error:
        assert "one question" in str(error)
    else:
        raise AssertionError("multi-question taste focus should be rejected")


def test_focus_rejects_a_long_multi_brief() -> None:
    try:
        validate_focus("x" * 241, "compact")
    except ValueError as error:
        assert "240 characters" in str(error)
    else:
        raise AssertionError("overlong focus should be rejected")


def test_release_prompt_is_bounded_to_complete_blockers() -> None:
    prompt = build_prompt("full-track", "release blockers only", "release")

    assert "At most three audible blockers" in prompt
    assert "Do not add an introduction" in prompt


def test_grounding_rejects_a_truncated_taste_response() -> None:
    partial = "HEARD_AUDIO\nANSWER: Piercing\nWHY: 0:08 - sharp"
    complete = partial + "\nWHY: 0:20 - bright\nACTION: NONE"

    assert not _has_grounded_schema(partial, "taste")
    assert _has_grounded_schema(complete, "taste")


def test_cache_key_requires_exact_scope() -> None:
    report = "\n".join(
        [
            "AUDIO_SHA256: ABC",
            "MODEL_REQUESTED: gemini-3.7-flash",
            "PROFILE: compact",
            "KIND: full-track",
            "FOCUS: kick sub",
        ]
    )

    assert _cached_report_matches(
        report,
        audio_hash="ABC",
        model="gemini-3.7-flash",
        profile="compact",
        kind="full-track",
        focus="  kick   sub ",
    )
    assert not _cached_report_matches(
        report,
        audio_hash="DIFFERENT",
        model="gemini-3.7-flash",
        profile="compact",
        kind="full-track",
        focus="kick sub",
    )


def test_cache_key_includes_generation_budget_when_supplied() -> None:
    report = "\n".join(
        [
            "AUDIO_SHA256: ABC",
            "MODEL_REQUESTED: gemini-3.7-flash",
            "PROFILE: taste",
            "KIND: full-track",
            "FOCUS: vocal clarity",
            "MAX_OUTPUT_TOKENS: 420",
            "THINKING_LEVEL: LOW",
        ]
    )

    assert _cached_report_matches(
        report,
        audio_hash="ABC",
        model="gemini-3.7-flash",
        profile="taste",
        kind="full-track",
        focus="vocal clarity",
        max_output_tokens=420,
        thinking_level="LOW",
    )
    assert not _cached_report_matches(
        report,
        audio_hash="ABC",
        model="gemini-3.7-flash",
        profile="taste",
        kind="full-track",
        focus="vocal clarity",
        max_output_tokens=240,
        thinking_level="LOW",
    )


def test_api_error_is_written_as_structured_unverified_report(
    tmp_path: Path, monkeypatch
) -> None:
    audio = tmp_path / "mix.wav"
    audio.write_bytes(b"RIFF-test-fixture")
    report_path = tmp_path / "gemini.md"

    def fail_request(*args, **kwargs):
        raise RuntimeError("Gemini API returned HTTP 400: unsupported setting")

    monkeypatch.setattr(feedback, "_request", fail_request)

    result = feedback.main(
        [
            str(audio),
            "--profile",
            "taste",
            "--focus",
            "judge vocal focus",
            "--thinking-level",
            "MINIMAL",
            "--output",
            str(report_path),
        ]
    )

    report = report_path.read_text(encoding="utf-8")
    assert result == 2
    assert "AUDIO_GROUNDING: UNVERIFIED" in report
    assert "unsupported setting" in report
    assert "AUDIO UNAVAILABLE" in report
