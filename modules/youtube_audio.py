import yt_dlp
import os

def download_audio(url):
    os.makedirs("temp", exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "temp/audio.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }],
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "temp/audio.wav"
