import importlib.util
import math
import struct
import sys
import wave
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "skills" / "ableton-mix-audit" / "scripts" / "mix_audit.py"
SPEC = importlib.util.spec_from_file_location("mix_audit", SCRIPT)
mix_audit = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["mix_audit"] = mix_audit
SPEC.loader.exec_module(mix_audit)


def write_wav(path: Path, left, right=None, sample_rate=44100):
    if right is None:
        channels = [left]
    else:
        assert len(left) == len(right)
        channels = [left, right]
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(len(channels))
        handle.setsampwidth(2)
        handle.setframerate(sample_rate)
        frames = bytearray()
        for index in range(len(channels[0])):
            for channel in channels:
                sample = max(-1.0, min(0.999969, float(channel[index])))
                frames.extend(struct.pack("<h", int(round(sample * 32768.0))))
        handle.writeframes(frames)


def tone(seconds=2.0, amplitude=0.25, phase=0.0, sample_rate=44100):
    return [amplitude * math.sin(2.0 * math.pi * 440.0 * index / sample_rate + phase) for index in range(int(seconds * sample_rate))]


def test_healthy_stereo_file_has_core_metrics(tmp_path):
    samples = tone()
    path = tmp_path / "healthy.wav"
    write_wav(path, samples, samples)

    result = mix_audit.audit(path)

    assert result["schema_version"] == "1.0"
    assert result["source"]["channels"] == 2
    assert result["source"]["duration_sec"] == 2.0
    assert result["metrics"]["sample_peak_dbfs"] < -10.0
    assert result["metrics"]["stereo"]["correlation"] > 0.99
    assert result["summary"]["decision"] != "TECHNICAL_FAIL"


def test_full_scale_samples_are_a_hard_failure(tmp_path):
    path = tmp_path / "clipped.wav"
    samples = tone(amplitude=1.0)
    write_wav(path, samples, samples)

    result = mix_audit.audit(path)

    sample_check = next(item for item in result["checks"] if item["id"] == "sample_peak")
    assert sample_check["status"] == "fail"
    assert result["summary"]["decision"] == "TECHNICAL_FAIL"


def test_phase_inverted_stereo_is_reported_as_a_warning(tmp_path):
    samples = tone(amplitude=0.3)
    path = tmp_path / "phase.wav"
    write_wav(path, samples, [-value for value in samples])

    result = mix_audit.audit(path)

    correlation_check = next(item for item in result["checks"] if item["id"] == "stereo_correlation")
    mono_check = next(item for item in result["checks"] if item["id"] == "mono_loss")
    assert correlation_check["status"] == "warn"
    assert mono_check["status"] == "warn"


def test_cli_writes_json_and_report_without_uploading(tmp_path):
    audio = tmp_path / "cli.wav"
    output_json = tmp_path / "out" / "audit.json"
    output_report = tmp_path / "out" / "audit.md"
    samples = tone(amplitude=0.2)
    write_wav(audio, samples, samples)

    exit_code = mix_audit.main([
        str(audio),
        "--json-out",
        str(output_json),
        "--report-out",
        str(output_report),
    ])

    assert exit_code == 0
    assert output_json.is_file()
    assert output_report.is_file()
    assert '"schema_version": "1.0"' in output_json.read_text(encoding="utf-8")
    assert "# Ableton Mix Audit" in output_report.read_text(encoding="utf-8")
