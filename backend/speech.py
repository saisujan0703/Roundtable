"""
Roundtable Speech-to-Text
=========================
Transcribes a PM's spoken product idea locally with faster-whisper, so recordings never leave the server.

- Model size comes from WHISPER_MODEL (default "base"; "small" is more accurate but slower on CPU).
  It is downloaded once on first use and cached by Hugging Face.
- The model loads lazily on the first transcription and is reused afterwards.
"""
from __future__ import annotations

import io
import os
import threading
import wave
from typing import Any, Optional

import numpy as np

WHISPER_RATE = 16000

_model: Optional[Any] = None
_model_lock = threading.Lock()


class SpeechUnavailable(RuntimeError):
    """faster-whisper is not installed or the model could not be loaded."""


def _get_model():
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                try:
                    from faster_whisper import WhisperModel
                except ImportError as e:
                    raise SpeechUnavailable("Voice input needs faster-whisper: pip install faster-whisper") from e
                try:
                    _model = WhisperModel(os.environ.get("WHISPER_MODEL", "base"), device="cpu", compute_type="int8")
                except Exception as e:
                    raise SpeechUnavailable(f"Could not load the Whisper model: {type(e).__name__}: {e}") from e
    return _model


def _decode_wav(audio: bytes) -> np.ndarray:
    """WAV bytes -> mono float32 at 16 kHz, as Whisper expects.

    Decoded here rather than by faster-whisper's PyAV path, which breaks on newer PyAV releases.
    st.chat_input records 16 kHz mono 16-bit WAV, but other rates and channel counts are handled too.
    """
    with wave.open(io.BytesIO(audio), "rb") as w:
        width, channels, rate = w.getsampwidth(), w.getnchannels(), w.getframerate()
        frames = w.readframes(w.getnframes())
    if width == 2:
        samples = np.frombuffer(frames, dtype="<i2").astype(np.float32) / 32768.0
    elif width == 4:
        samples = np.frombuffer(frames, dtype="<i4").astype(np.float32) / 2147483648.0
    elif width == 1:
        samples = (np.frombuffer(frames, dtype=np.uint8).astype(np.float32) - 128.0) / 128.0
    else:
        raise ValueError(f"Unsupported WAV sample width: {width * 8}-bit")
    if channels > 1:
        samples = samples.reshape(-1, channels).mean(axis=1)
    if rate != WHISPER_RATE and len(samples):
        n = int(round(len(samples) * WHISPER_RATE / rate))
        samples = np.interp(np.linspace(0, len(samples) - 1, n), np.arange(len(samples)), samples).astype(np.float32)
    return samples


def transcribe(audio: bytes) -> str:
    """Return the text spoken in a WAV recording (what st.chat_input's mic produces)."""
    samples = _decode_wav(audio)
    if len(samples) < WHISPER_RATE // 4:  # under a quarter second: nothing to transcribe
        return ""
    segments, _info = _get_model().transcribe(
        samples,
        beam_size=1,
        vad_filter=True,  # skip leading/trailing silence so a quiet start doesn't produce filler text
    )
    return " ".join(s.text.strip() for s in segments).strip()
