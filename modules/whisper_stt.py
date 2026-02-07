from faster_whisper import WhisperModel

_model = None

def get_model():
    global _model
    if _model is None:
        _model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )
    return _model


def transcribe(audio_path):
    model = get_model()
    segments, info = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)
    return text
