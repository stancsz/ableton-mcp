from pathlib import Path

from tools.gemini_audio_feedback import audio_mime_type, build_prompt


def test_audio_mime_type_accepts_common_mix_formats() -> None:
    assert audio_mime_type(Path("mix.WAV")) == "audio/wav"
    assert audio_mime_type(Path("mix.mp3")) == "audio/mpeg"


def test_prompt_requires_audio_grounding_and_timestamps() -> None:
    prompt = build_prompt("full-track", "focus on low-end translation")

    assert "listen to the entire attached full mix" in prompt
    assert "HEARD_AUDIO" in prompt
    assert "AUDIO UNAVAILABLE" in prompt
    assert "low-end translation" in prompt
