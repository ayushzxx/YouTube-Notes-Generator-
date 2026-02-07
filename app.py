import streamlit as st
from modules.youtube_audio import download_audio
from modules.whisper_stt import transcribe
from modules.notes_generator import generate_notes
from fpdf import FPDF
import os

st.set_page_config(page_title="YouTube AI Notes", layout="wide")
st.title("🎥 YouTube Video AI Notes Generator")

url = st.text_input("🔗 Paste YouTube URL")

if st.button("Generate Notes"):
    with st.spinner("Downloading audio..."):
        audio_path = download_audio(url)

    with st.spinner("Transcribing audio..."):
        transcript = transcribe(audio_path)

    with st.spinner("Generating notes..."):
        notes = generate_notes(transcript)

    st.subheader("📝 AI Generated Notes")
    st.write(notes)

    # Save Markdown
    os.makedirs("exports", exist_ok=True)
    md_path = "exports/notes.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(notes)

    # Save PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(True, 15)
    pdf.set_font("Helvetica", size=12)

    # Process notes to handle special Unicode characters that FPDF can't encode
    processed_notes = notes
    # Replace common smart quotes and dashes with ASCII equivalents
    char_map = {
        "—": "-",      # em dash
        "–": "-",      # en dash
        "'": "'",      # smart single quote
        "'": "'",      # smart single quote
        """: '"',      # smart double quote
        """: '"',      # smart double quote
        "…": "...",    # ellipsis
    }
    for old_char, new_char in char_map.items():
        processed_notes = processed_notes.replace(old_char, new_char)
    
    for line in processed_notes.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf_path = "exports/notes.pdf"
    pdf.output(pdf_path)

    st.download_button("⬇️ Download Markdown", open(md_path, "rb"), "notes.md")
    st.download_button("⬇️ Download PDF", open(pdf_path, "rb"), "notes.pdf")
