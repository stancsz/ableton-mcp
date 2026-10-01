from pathlib import Path
import base64
import io
import json
import urllib.error

import pytest

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
    )
    assert not _cached_report_matches(
        report,
        audio_hash="ABC",
        model="gemini-3.7-flash",
        profile="taste",
        kind="full-track",
        focus="vocal clarity",
        max_output_tokens=240,
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
            "--output",
            str(report_path),
        ]
    )

    report = report_path.read_text(encoding="utf-8")
    assert result == 2
    assert "AUDIO_GROUNDING: UNVERIFIED" in report
    assert "unsupported setting" in report
    assert "AUDIO UNAVAILABLE" in report


def test_request_sends_exact_audio_to_local_gateway_without_google_credentials(tmp_path, monkeypatch):
    audio = tmp_path / "mix.wav"
    audio.write_bytes(b"RIFF-exact-authorized-bytes")
    monkeypatch.setenv("GEMINI_API_KEY", "unused-google-key")
    monkeypatch.setenv("SUBROUTE_API_KEY", "gateway-only-key")
    captured = []

    class Opener:
        def open(self, request, timeout):
            captured.append(request)
            assert timeout == 400
            return io.BytesIO(b'{"choices": []}')

    def build_opener(*handlers):
        assert handlers[0].proxies == {}
        assert handlers[1].redirect_request(None, None, 302, "", {}, "https://other.test") is None
        return Opener()

    monkeypatch.setattr(feedback.urllib.request, "build_opener", build_opener)
    feedback._request(audio, feedback.DEFAULT_BASE_URL, feedback.DEFAULT_MODEL, "listen", 420)
    request = captured[0]
    assert request.full_url == "http://127.0.0.1:4000/v1/chat/completions"
    assert request.get_header("Authorization") == "Bearer gateway-only-key"
    body = json.loads(request.data)
    assert body["model"] == "gemini-subscription"
    block = body["messages"][0]["content"][1]
    assert block["type"] == "input_audio"
    assert block["input_audio"]["format"] == "wav"
    assert base64.b64decode(block["input_audio"]["data"]) == audio.read_bytes()
    assert "unused-google-key" not in str(request.headers) + str(body)


@pytest.mark.parametrize("url", ["https://google.test", "http://localhost:4001", "http://key@localhost:4000", "http://localhost:4000/?key=secret"])
def test_gateway_scope_rejects_other_destinations(url):
    with pytest.raises(ValueError):
        feedback.resolve_base_url(url)


def test_cache_cannot_reuse_a_vertex_report_for_subroute():
    report = "\n".join([
        "AUDIO_SHA256: ABC", "MODEL_REQUESTED: gemini-subscription",
        "PROFILE: taste", "KIND: full-track", "FOCUS: vocal clarity",
    ])
    kwargs = dict(audio_hash="ABC", model="gemini-subscription", profile="taste",
                  kind="full-track", focus="vocal clarity", base_url=feedback.DEFAULT_BASE_URL)
    assert not _cached_report_matches(report, **kwargs)
    report += "\nROUTE: subroute-subscription\nBASE_URL: http://127.0.0.1:4000"
    assert _cached_report_matches(report, **kwargs)


@pytest.mark.parametrize("change,expected", [
    ({}, 0), ({"model": "codex-luna"}, 2), ({"usage": {}}, 2),
    ({"choices": {"bad": "response"}}, 2),
    ({"choices": [{"finish_reason": "length", "message": {"content": "HEARD_AUDIO\nANSWER: good\nWHY: 0:01 clear; 0:02 warm\nACTION: NONE"}}]}, 2),
    ({"choices": [{"finish_reason": "stop", "message": {"content": "AUDIO UNAVAILABLE"}}]}, 2),
])
def test_grounding_requires_completed_subscription_audio_response(tmp_path, monkeypatch, change, expected):
    audio = tmp_path / "mix.wav"
    audio.write_bytes(b"RIFF-fixture")
    output = tmp_path / "feedback.md"
    payload = {
        "model": "gemini-subscription", "id": "test-receipt",
        "usage": {"prompt_tokens": 50, "completion_tokens": 30, "total_tokens": 80},
        "choices": [{"finish_reason": "stop", "message": {"content": "HEARD_AUDIO\nANSWER: good\nWHY: 0:01 clear; 0:02 warm\nACTION: NONE"}}],
    }
    payload.update(change)
    monkeypatch.setattr(feedback, "_request", lambda *args: payload)
    assert feedback.main([str(audio), "--profile", "taste", "--focus", "vocal clarity", "--output", str(output)]) == expected
    report = output.read_text(encoding="utf-8")
    assert "ROUTE: subroute-subscription" in report
    assert "RESPONSE_ID: test-receipt" in report
    assert "backend-managed" in report
    assert ("AUDIO_GROUNDING: PASS" in report) == (expected == 0)


def test_transport_error_redacts_gateway_key(tmp_path, monkeypatch):
    audio = tmp_path / "mix.mp3"
    audio.write_bytes(b"ID3-fixture")
    monkeypatch.setenv("SUBROUTE_API_KEY", "sensitive-key")

    class Opener:
        def open(self, request, timeout):
            raise urllib.error.HTTPError(request.full_url, 401, "unauthorized", {}, io.BytesIO(b"sensitive-key rejected"))

    monkeypatch.setattr(feedback.urllib.request, "build_opener", lambda *args: Opener())
    with pytest.raises(RuntimeError) as error:
        feedback._request(audio, feedback.DEFAULT_BASE_URL, feedback.DEFAULT_MODEL, "listen", 420)
    assert "sensitive-key" not in str(error.value)
    assert "HTTP 401" in str(error.value)
    assert "rejected" not in str(error.value)  # central transport omits private provider bodies


def test_large_wav_is_rejected_without_request_or_conversion(tmp_path, monkeypatch):
    audio = tmp_path / "mix.wav"
    with audio.open("wb") as handle:
        handle.truncate(feedback.MAX_AUDIO_BYTES + 1)
    monkeypatch.setattr(feedback, "_request", lambda *args: pytest.fail("must not send oversized audio"))
    with pytest.raises(SystemExit) as error:
        feedback.main([str(audio)])
    assert error.value.code == 2
