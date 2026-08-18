#!/usr/bin/env python3
"""Deterministic, local-first WAV checks for the ableton-mix-audit skill.

This script intentionally does not edit Ableton, search for audio, convert
files, or upload anything. It accepts one explicit PCM WAV and reports both
measured values and unavailable optional measurements.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import wave
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import numpy as np
except ImportError:  # pragma: no cover - exercised by the documented fallback path
    np = None  # type: ignore


SCHEMA_VERSION = "1.0"
BLOCK_FRAMES = 4096
SPECTRUM_WINDOW = 4096
SPECTRUM_HOP = 2048
SPECTRUM_BANDS = (
    (20.0, 60.0),
    (60.0, 120.0),
    (120.0, 250.0),
    (250.0, 500.0),
    (500.0, 2000.0),
    (2000.0, 5000.0),
    (5000.0, 10000.0),
    (10000.0, 20000.0),
)


def db(value: float, floor: float = -120.0) -> float:
    if not math.isfinite(value) or value <= 0.0:
        return floor
    return 20.0 * math.log10(value)


def db_power(value: float, floor: float = -120.0) -> float:
    if not math.isfinite(value) or value <= 0.0:
        return floor
    return 10.0 * math.log10(value)


def parse_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        parsed = float(str(value).strip())
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decode_pcm(raw: bytes, sample_width: int) -> Any:
    """Decode little-endian PCM to a flat float array in [-1, 1)."""
    if np is not None:
        if sample_width == 1:
            values = np.frombuffer(raw, dtype=np.uint8).astype(np.float64)
            return (values - 128.0) / 128.0
        if sample_width == 2:
            return np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
        if sample_width == 3:
            values = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3).astype(np.int32)
            packed = values[:, 0] | (values[:, 1] << 8) | (values[:, 2] << 16)
            packed = np.where((packed & 0x800000) != 0, packed - 0x1000000, packed)
            return packed.astype(np.float64) / 8388608.0
        if sample_width == 4:
            return np.frombuffer(raw, dtype="<i4").astype(np.float64) / 2147483648.0
        raise ValueError("unsupported PCM sample width: %s" % sample_width)

    values: List[float] = []
    for offset in range(0, len(raw), sample_width):
        sample = raw[offset : offset + sample_width]
        if len(sample) != sample_width:
            break
        if sample_width == 1:
            values.append((sample[0] - 128.0) / 128.0)
        elif sample_width == 2:
            integer = int.from_bytes(sample, "little", signed=True)
            values.append(integer / 32768.0)
        elif sample_width == 3:
            integer = int.from_bytes(sample, "little", signed=False)
            if integer & 0x800000:
                integer -= 0x1000000
            values.append(integer / 8388608.0)
        elif sample_width == 4:
            integer = int.from_bytes(sample, "little", signed=True)
            values.append(integer / 2147483648.0)
        else:
            raise ValueError("unsupported PCM sample width: %s" % sample_width)
    return values


def _spectrum_step(
    pending: Any,
    mono: Any,
    sample_rate: int,
    spectrum_sum: Any,
    spectrum_windows: int,
    window_function: Any,
) -> Tuple[Any, Any, int]:
    if np is None:
        return pending, spectrum_sum, spectrum_windows
    if pending.size:
        combined = np.concatenate((pending, mono))
    else:
        combined = mono
    if combined.size < SPECTRUM_WINDOW:
        return combined, spectrum_sum, spectrum_windows

    window_count = 1 + (combined.size - SPECTRUM_WINDOW) // SPECTRUM_HOP
    last_start = (window_count - 1) * SPECTRUM_HOP
    if spectrum_sum is None:
        spectrum_sum = np.zeros(SPECTRUM_WINDOW // 2 + 1, dtype=np.float64)
    for start in range(0, last_start + 1, SPECTRUM_HOP):
        frame = combined[start : start + SPECTRUM_WINDOW] * window_function
        transformed = np.fft.rfft(frame)
        spectrum_sum += (np.abs(transformed) ** 2) / float(SPECTRUM_WINDOW)
    next_start = last_start + SPECTRUM_HOP
    return combined[next_start:], spectrum_sum, spectrum_windows + window_count


def spectral_metrics(spectrum_sum: Any, windows: int, sample_rate: int) -> Dict[str, Any]:
    if np is None or spectrum_sum is None or windows == 0:
        return {"status": "unknown", "reason": "numpy spectral analysis unavailable"}

    average_power = spectrum_sum / float(windows)
    frequencies = np.fft.rfftfreq(SPECTRUM_WINDOW, d=1.0 / sample_rate)
    total_mask = (frequencies >= 20.0) & (frequencies <= min(20000.0, sample_rate / 2.0))
    total_power = float(np.sum(average_power[total_mask]))
    if total_power <= 0.0:
        return {"status": "unknown", "reason": "spectrum contains no finite audible-band energy"}

    bands: Dict[str, float] = {}
    for low, high in SPECTRUM_BANDS:
        mask = (frequencies >= low) & (frequencies < min(high, sample_rate / 2.0 + 1.0))
        bands["%g-%gHz" % (low, high)] = db_power(float(np.sum(average_power[mask])) / total_power)

    centroid = float(np.sum(frequencies[total_mask] * average_power[total_mask]) / total_power)
    slope_mask = total_mask & (average_power > 0.0)
    slope = None
    if int(np.sum(slope_mask)) >= 2:
        slope = float(np.polyfit(np.log2(frequencies[slope_mask]), db_power_array(average_power[slope_mask]), 1)[0])
    return {
        "status": "measured",
        "bands_relative_db": bands,
        "spectral_centroid_hz": centroid,
        "tilt_db_per_octave": slope,
        "windows": windows,
    }


def db_power_array(values: Any) -> Any:
    if np is None:
        return values
    safe = np.maximum(values, 1e-30)
    return 10.0 * np.log10(safe)


def parse_loudnorm_output(stderr: str) -> Optional[Dict[str, Optional[float]]]:
    matches = re.findall(r"\{\s*\"input_i\".*?\}", stderr, flags=re.DOTALL)
    if not matches:
        return None
    try:
        payload = json.loads(matches[-1])
    except json.JSONDecodeError:
        return None
    return {
        "integrated_lufs": parse_float(payload.get("input_i")),
        "true_peak_dbtp": parse_float(payload.get("input_tp")),
        "lra_lu": parse_float(payload.get("input_lra")),
        "threshold_lufs": parse_float(payload.get("input_thresh")),
    }


def run_loudnorm(path: Path) -> Dict[str, Any]:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return {"status": "unknown", "reason": "ffmpeg was not found on PATH"}
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-i",
        str(path),
        "-af",
        "loudnorm=I=-14:TP=-1.0:LRA=7:print_format=json",
        "-f",
        "null",
        "-",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    parsed = parse_loudnorm_output(completed.stderr)
    if parsed is None:
        return {
            "status": "unknown",
            "reason": "ffmpeg loudnorm did not return parseable measurements",
            "returncode": completed.returncode,
        }
    parsed["status"] = "measured"
    return parsed


def percentile(values: Sequence[float], fraction: float) -> Optional[float]:
    if not values:
        return None
    if np is not None:
        return float(np.percentile(np.asarray(values, dtype=np.float64), fraction * 100.0))
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * fraction))))
    return float(ordered[index])


def analyze_wav(path: Path, run_loudnorm_metrics: bool = True) -> Dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(str(path))
    if path.suffix.lower() != ".wav":
        raise ValueError("only PCM .wav input is accepted; export a lossless WAV explicitly")

    with wave.open(str(path), "rb") as audio:
        channels = audio.getnchannels()
        sample_rate = audio.getframerate()
        sample_width = audio.getsampwidth()
        frame_count = audio.getnframes()
        if audio.getcomptype() != "NONE":
            raise ValueError("compressed WAV is not supported: %s" % audio.getcomptype())
        if channels < 1 or sample_rate < 1 or frame_count < 1:
            raise ValueError("WAV has no usable audio frames")

        sample_peak = 0.0
        sum_squares = 0.0
        sample_count = 0
        frames_read = 0
        left_sum = right_sum = left_square = right_square = cross_sum = 0.0
        mono_sum_squares = 0.0
        block_rms: List[float] = []
        spectral_pending = np.empty(0, dtype=np.float64) if np is not None else []
        spectrum_sum = None
        spectrum_windows = 0
        window_function = np.hanning(SPECTRUM_WINDOW) if np is not None else None

        while True:
            raw = audio.readframes(65536)
            if not raw:
                break
            decoded = decode_pcm(raw, sample_width)
            if np is not None:
                frame_values = decoded.reshape((-1, channels))
                frames_read += int(frame_values.shape[0])
                mono = np.mean(frame_values, axis=1)
                sample_peak = max(sample_peak, float(np.max(np.abs(frame_values))))
                sum_squares += float(np.sum(frame_values * frame_values))
                sample_count += int(frame_values.size)
                if channels >= 2:
                    left = frame_values[:, 0]
                    right = frame_values[:, 1]
                    left_sum += float(np.sum(left))
                    right_sum += float(np.sum(right))
                    left_square += float(np.sum(left * left))
                    right_square += float(np.sum(right * right))
                    cross_sum += float(np.sum(left * right))
                mono_sum_squares += float(np.sum(mono * mono))
                for start in range(0, mono.size, BLOCK_FRAMES):
                    block = mono[start : start + BLOCK_FRAMES]
                    block_rms.append(float(np.sqrt(np.mean(block * block))))
                spectral_pending, spectrum_sum, spectrum_windows = _spectrum_step(
                    spectral_pending,
                    mono.astype(np.float64, copy=False),
                    sample_rate,
                    spectrum_sum,
                    spectrum_windows,
                    window_function,
                )
            else:  # pragma: no cover - current test environment has numpy
                frames = [decoded[i : i + channels] for i in range(0, len(decoded), channels)]
                mono_block: List[float] = []
                for frame in frames:
                    if len(frame) != channels:
                        continue
                    frames_read += 1
                    mono_value = sum(frame) / float(channels)
                    mono_block.append(mono_value)
                    sample_peak = max(sample_peak, max(abs(value) for value in frame))
                    sum_squares += sum(value * value for value in frame)
                    sample_count += len(frame)
                    if channels >= 2:
                        left, right = frame[0], frame[1]
                        left_sum += left
                        right_sum += right
                        left_square += left * left
                        right_square += right * right
                        cross_sum += left * right
                    mono_sum_squares += mono_value * mono_value
                for start in range(0, len(mono_block), BLOCK_FRAMES):
                    block = mono_block[start : start + BLOCK_FRAMES]
                    block_rms.append(math.sqrt(sum(value * value for value in block) / len(block)))

        if frames_read != frame_count:
            raise ValueError(
                "WAV frame count mismatch: header says %s, decoded %s" % (frame_count, frames_read)
            )

    duration = frame_count / float(sample_rate)
    rms = math.sqrt(sum_squares / float(sample_count)) if sample_count else 0.0
    block_db = [db(value) for value in block_rms]
    active_blocks = [value for value in block_db if value > -50.0]
    leading_blocks = 0
    for value in block_db:
        if value <= -60.0:
            leading_blocks += 1
        else:
            break
    trailing_blocks = 0
    for value in reversed(block_db):
        if value <= -60.0:
            trailing_blocks += 1
        else:
            break

    result: Dict[str, Any] = {
        "sample_rate": sample_rate,
        "channels": channels,
        "bit_depth": sample_width * 8,
        "frame_count": frame_count,
        "duration_sec": duration,
        "sample_peak_dbfs": db(sample_peak),
        "rms_dbfs": db(rms),
        "crest_factor_db": db(sample_peak / rms) if rms > 0.0 else None,
        "leading_silence_sec": min(duration, leading_blocks * BLOCK_FRAMES / float(sample_rate)),
        "trailing_silence_sec": min(duration, trailing_blocks * BLOCK_FRAMES / float(sample_rate)),
        "block_rms_dbfs": {
            "p10": percentile(block_db, 0.10),
            "median": percentile(block_db, 0.50),
            "p90": percentile(block_db, 0.90),
            "spread_p90_p10": (
                percentile(block_db, 0.90) - percentile(block_db, 0.10)
                if block_db
                else None
            ),
        },
        "stereo": {},
        "spectral": spectral_metrics(spectrum_sum, spectrum_windows, sample_rate),
    }

    if channels >= 2:
        left_mean = left_sum / float(frame_count)
        right_mean = right_sum / float(frame_count)
        left_variance = max(0.0, left_square / float(frame_count) - left_mean * left_mean)
        right_variance = max(0.0, right_square / float(frame_count) - right_mean * right_mean)
        covariance = cross_sum / float(frame_count) - left_mean * right_mean
        denominator = math.sqrt(left_variance * right_variance)
        correlation = covariance / denominator if denominator > 0.0 else None
        stereo_rms = math.sqrt(sum_squares / float(sample_count))
        mono_rms = math.sqrt(mono_sum_squares / float(frame_count))
        result["stereo"] = {
            "correlation": correlation,
            "mono_rms_dbfs": db(mono_rms),
            "stereo_rms_dbfs": db(stereo_rms),
            "mono_loss_db": db(mono_rms / stereo_rms) if stereo_rms > 0.0 else None,
        }
    else:
        result["stereo"] = {"status": "unknown", "reason": "input is mono"}

    result["loudnorm"] = run_loudnorm(path) if run_loudnorm_metrics else {"status": "skipped"}
    return result


def check(
    check_id: str,
    status: str,
    check_class: str,
    message: str,
    evidence: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return {
        "id": check_id,
        "status": status,
        "class": check_class,
        "message": message,
        "evidence": evidence or {},
    }


def reference_deviation(main: Dict[str, Any], reference: Dict[str, Any]) -> Dict[str, Any]:
    main_bands = main.get("spectral", {}).get("bands_relative_db", {})
    ref_bands = reference.get("spectral", {}).get("bands_relative_db", {})
    deltas = {
        name: round(value - ref_bands[name], 3)
        for name, value in main_bands.items()
        if name in ref_bands
    }
    return {
        "band_share_delta_db": deltas,
        "max_abs_delta_db": max((abs(value) for value in deltas.values()), default=None),
    }


def build_checks(
    metrics: Dict[str, Any],
    mode: str,
    reference_metrics: Optional[Dict[str, Any]],
    vocal_metrics: Optional[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    checks: List[Dict[str, Any]] = []
    peak = metrics.get("sample_peak_dbfs")
    if peak is None:
        checks.append(check("sample_peak", "unknown", "hard_gate", "sample peak was unavailable"))
    elif peak >= -0.1:
        checks.append(check("sample_peak", "fail", "hard_gate", "decoded samples reach or nearly reach digital full scale", {"dbfs": peak}))
    elif peak >= -1.0:
        checks.append(check("sample_peak", "warn", "hard_gate", "sample peak is close to full scale", {"dbfs": peak}))
    else:
        checks.append(check("sample_peak", "pass", "hard_gate", "sample peak has measurable headroom", {"dbfs": peak}))

    loudnorm = metrics.get("loudnorm", {})
    true_peak = loudnorm.get("true_peak_dbtp")
    if true_peak is None:
        checks.append(check("true_peak", "unknown", "delivery_gate", "ffmpeg true peak was unavailable"))
    elif true_peak > 0.0:
        checks.append(check("true_peak", "fail", "delivery_gate", "true peak is above 0 dBTP", {"dbtp": true_peak}))
    elif mode == "release" and true_peak > -1.0:
        checks.append(check("true_peak", "warn", "delivery_gate", "release profile exceeds the conservative -1 dBTP ceiling", {"dbtp": true_peak}))
    else:
        checks.append(check("true_peak", "pass", "delivery_gate", "true peak was measured; no applicable hard failure", {"dbtp": true_peak}))

    duration = metrics.get("duration_sec", 0.0)
    leading = metrics.get("leading_silence_sec", 0.0)
    trailing = metrics.get("trailing_silence_sec", 0.0)
    if duration <= 0.0:
        checks.append(check("duration_and_trim", "fail", "hard_gate", "audio duration is zero"))
    elif leading > 1.5 or trailing > 1.5:
        checks.append(check("duration_and_trim", "warn", "proxy", "long leading or trailing silence needs an intentionality check", {"leading_sec": leading, "trailing_sec": trailing}))
    else:
        checks.append(check("duration_and_trim", "pass", "proxy", "no unusually long boundary silence detected", {"duration_sec": duration}))

    lra = loudnorm.get("lra_lu")
    crest = metrics.get("crest_factor_db")
    if lra is None and crest is None:
        checks.append(check("dynamics", "unknown", "proxy", "LRA and crest factor were unavailable"))
    elif mode in ("pre-master", "release") and ((lra is not None and lra < 3.0) or (crest is not None and crest < 6.0)):
        checks.append(check("dynamics", "warn", "proxy", "low dynamics proxy may indicate heavy control; listen before changing anything", {"lra_lu": lra, "crest_factor_db": crest}))
    else:
        checks.append(check("dynamics", "pass", "proxy", "dynamics proxies were measured without triggering the selected heuristic", {"lra_lu": lra, "crest_factor_db": crest}))

    spectral = metrics.get("spectral", {})
    if spectral.get("status") != "measured":
        checks.append(check("spectral_shape", "unknown", "proxy", "spectral analysis was unavailable", {"reason": spectral.get("reason")}))
    elif reference_metrics is None:
        checks.append(check("spectral_shape", "pass", "proxy", "spectral shape was measured descriptively; no reference was supplied", {"bands_relative_db": spectral.get("bands_relative_db")}))
    else:
        deviation = reference_deviation(metrics, reference_metrics)
        maximum = deviation.get("max_abs_delta_db")
        if maximum is not None and maximum >= 5.0:
            checks.append(check("reference_deviation", "warn", "proxy", "one or more relative spectral bands differ materially from the reference", deviation))
        else:
            checks.append(check("reference_deviation", "pass", "proxy", "relative spectral deviation stayed within the starting heuristic", deviation))

    stereo = metrics.get("stereo", {})
    correlation = stereo.get("correlation")
    mono_loss = stereo.get("mono_loss_db")
    if correlation is None:
        checks.append(check("stereo_correlation", "unknown", "proxy", "stereo correlation was unavailable", stereo))
    elif correlation < -0.2:
        checks.append(check("stereo_correlation", "warn", "proxy", "sustained negative correlation justifies a mono/width A/B", stereo))
    else:
        checks.append(check("stereo_correlation", "pass", "proxy", "full-file correlation did not trigger the phase-risk heuristic", stereo))
    if mono_loss is None:
        checks.append(check("mono_loss", "unknown", "proxy", "mono loss was unavailable", stereo))
    elif mono_loss <= -3.0:
        checks.append(check("mono_loss", "warn", "proxy", "mono summing loses more than the starting 3 dB heuristic", stereo))
    else:
        checks.append(check("mono_loss", "pass", "proxy", "mono loss did not trigger the starting heuristic", stereo))

    if vocal_metrics is None:
        checks.append(check("vocal_active_rms", "unknown", "proxy", "no vocal stem was supplied; vocal consistency is unmeasured"))
    else:
        vocal_blocks = vocal_metrics.get("block_rms_dbfs", {})
        spread = vocal_blocks.get("spread_p90_p10")
        if spread is not None and spread >= 6.0:
            checks.append(check("vocal_active_rms", "warn", "proxy", "vocal active-window dynamics need phrase-level listening or automation review", {"spread_p90_p10_db": spread, "vocal": vocal_blocks}))
        else:
            checks.append(check("vocal_active_rms", "pass", "proxy", "vocal active-window spread did not trigger the starting heuristic", {"vocal": vocal_blocks}))
    return checks


def make_summary(checks: Sequence[Dict[str, Any]], has_reference: bool, has_vocal: bool) -> Dict[str, Any]:
    counts = Counter(item["status"] for item in checks)
    if counts.get("fail", 0):
        decision = "TECHNICAL_FAIL"
    elif counts.get("warn", 0):
        decision = "MIX_RISK_REVIEW"
    elif counts.get("unknown", 0):
        decision = "HUMAN_LISTENING_REQUIRED"
    else:
        decision = "READY_FOR_HUMAN_RELEASE_DECISION"
    if has_reference or has_vocal:
        evidence_level = "D3"
    else:
        evidence_level = "D2"
    return {"decision": decision, "evidence_level": evidence_level, "counts": dict(counts)}


def make_report(result: Dict[str, Any]) -> str:
    summary = result["summary"]
    lines = [
        "# Ableton Mix Audit",
        "",
        "- Decision: `%s`" % summary["decision"],
        "- Evidence level: `%s`" % summary["evidence_level"],
        "- Source: `%s`" % result["source"]["path"],
        "- Duration: `%.2f s`" % result["source"]["duration_sec"],
        "",
        "## Measured values",
        "",
        "```json",
        json.dumps(result["metrics"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## Checks",
        "",
    ]
    for item in result["checks"]:
        lines.append("- **%s** `%s` (%s): %s" % (item["id"], item["status"], item["class"], item["message"]))
    lines.extend(
        [
            "",
            "## Human listening required",
            "",
            "Check stereo/mono vocal intelligibility, kick/bass translation, pumping and transients, harshness/sibilance, depth, width, artifacts, and level-matched references. Metrics do not close these gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_optional(path_value: Optional[str], label: str) -> Optional[Path]:
    if not path_value:
        return None
    path = Path(path_value)
    if not path.is_file():
        raise FileNotFoundError("%s file does not exist: %s" % (label, path))
    if path.suffix.lower() != ".wav":
        raise ValueError("%s must be an explicit PCM .wav file: %s" % (label, path))
    return path


def audit(
    audio_path: Path,
    mode: str = "mix",
    kind: str = "full-track",
    reference_path: Optional[Path] = None,
    vocal_path: Optional[Path] = None,
) -> Dict[str, Any]:
    metrics = analyze_wav(audio_path)
    reference_metrics = analyze_wav(reference_path) if reference_path else None
    vocal_metrics = analyze_wav(vocal_path) if vocal_path else None
    checks = build_checks(metrics, mode, reference_metrics, vocal_metrics)
    return {
        "schema_version": SCHEMA_VERSION,
        "source": {
            "path": str(audio_path.resolve()),
            "kind": kind,
            "sample_rate": metrics["sample_rate"],
            "channels": metrics["channels"],
            "bit_depth": metrics["bit_depth"],
            "duration_sec": metrics["duration_sec"],
            "sha256": sha256_file(audio_path),
        },
        "config": {
            "mode": mode,
            "reference": str(reference_path.resolve()) if reference_path else None,
            "vocal": str(vocal_path.resolve()) if vocal_path else None,
        },
        "metrics": metrics,
        "checks": checks,
        "summary": make_summary(checks, reference_path is not None, vocal_path is not None),
    }


def parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser(description="Run local deterministic checks on one explicit PCM WAV.")
    argument_parser.add_argument("audio", help="exact full-mix or stem .wav path")
    argument_parser.add_argument("--mode", choices=("mix", "pre-master", "release"), default="mix")
    argument_parser.add_argument("--kind", choices=("full-track", "stem"), default="full-track")
    argument_parser.add_argument("--reference", help="optional exact level-matched reference .wav")
    argument_parser.add_argument("--vocal", help="optional exact vocal stem .wav")
    argument_parser.add_argument("--json-out", help="optional output JSON path")
    argument_parser.add_argument("--report-out", help="optional Markdown report path")
    argument_parser.add_argument("--fail-on-fail", action="store_true", help="return exit code 1 when a hard check fails")
    return argument_parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parser().parse_args(argv)
    try:
        audio_path = Path(args.audio)
        reference_path = validate_optional(args.reference, "reference")
        vocal_path = validate_optional(args.vocal, "vocal")
        result = audit(audio_path, args.mode, args.kind, reference_path, vocal_path)
        payload = json.dumps(result, ensure_ascii=False, indent=2)
        if args.json_out:
            json_path = Path(args.json_out)
            json_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.write_text(payload + "\n", encoding="utf-8")
        if args.report_out:
            report_path = Path(args.report_out)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(make_report(result), encoding="utf-8")
        if not args.json_out and not args.report_out:
            print(payload)
        if args.fail_on_fail and result["summary"]["decision"] == "TECHNICAL_FAIL":
            return 1
        return 0
    except (FileNotFoundError, ValueError, wave.Error, OSError) as error:
        print("mix_audit: %s" % error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
