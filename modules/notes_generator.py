from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
import os

# Ensure .env is loaded if present (helps when Streamlit doesn't auto-load it)
env_path = Path(__file__).resolve().parents[1] / ".env"
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if not line or line.strip().startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"')
        os.environ.setdefault(k, v)

# Prefer OPENAI_API_KEY, fall back to OPENROUTER_API_KEY
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    model="mistralai/mistral-7b-instruct"
)

# Also set the openai package global api_key so the underlying client sees it
try:
    import openai as _openai
    if api_key:
        _openai.api_key = api_key
except Exception:
    pass

prompt = ChatPromptTemplate.from_template("""
You are an expert note-taker.

From the transcript below:
1. Generate clear NOTES
2. Extract KEY POINTS (bullet list)
3. Write a concise SUMMARY

Transcript:
{text}
""")

def generate_notes(text):
    chain = prompt | llm
    return chain.invoke({"text": text}).content
