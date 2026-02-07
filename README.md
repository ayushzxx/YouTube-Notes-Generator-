# 🎥 YouTube AI Notes Generator

An intelligent application that automatically generates comprehensive AI notes from YouTube videos. Simply paste a YouTube URL, and the application will:
- Download and extract audio from the video
- Transcribe the audio to text using Whisper
- Generate intelligent, structured notes using LangChain and OpenAI
- Export notes in both Markdown and PDF formats

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Requirements](#requirements)

---

## ✨ Features

- **Easy YouTube Integration**: Simply paste any YouTube URL
- **Advanced Audio Transcription**: Uses OpenAI's Whisper model for accurate transcription
- **AI-Powered Note Generation**: Leverages LangChain and OpenAI to create intelligent, well-structured notes
- **Multiple Export Formats**: Save notes as Markdown (.md) and PDF (.pdf)
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience
- **Real-time Processing**: Visual feedback during each step of the process

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software

1. **Python 3.8 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Git** (Optional, but recommended)
   - Download from [git-scm.com](https://git-scm.com/)
   - Used for version control

3. **FFmpeg**
   - Required by yt-dlp and Whisper for audio processing
   - **Windows Installation:**
     - Download from [ffmpeg.org](https://ffmpeg.org/download.html)
     - Or use Chocolatey: `choco install ffmpeg`
     - Or use Windows Package Manager: `winget install ffmpeg`
   - **Verification:** `ffmpeg -version`

4. **OpenAI API Key**
   - Sign up at [openai.com](https://openai.com)
   - Generate API key from your account dashboard
   - Keep this key safe and secret

---

## 🚀 Installation Guide

### Step 1: Clone or Download the Project

**Option A - Using Git (Recommended):**
```bash
git clone <repository-url>
cd Youtube-notes-generator
```

**Option B - Download ZIP:**
- Download the project as ZIP from the repository
- Extract the folder to your desired location
- Open terminal/command prompt and navigate to the folder

### Step 2: Create a Virtual Environment

Creating a virtual environment isolates your project dependencies and prevents conflicts.

**On Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### Step 3: Upgrade pip

Ensure you have the latest version of pip:

```bash
python -m pip install --upgrade pip
```

### Step 4: Install Required Dependencies

Install all required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web interface framework
- `yt-dlp` - YouTube video downloader
- `faster-whisper` - Audio transcription
- `langchain` - LLM framework (>=0.2.0)
- `langchain-openai` - OpenAI integration
- `langchain-core` - Core LangChain components
- `python-dotenv` - Environment variable management
- `fpdf` - PDF generation
- `markdown` - Markdown processing
- `openai` - OpenAI API client
- `pydantic` - Data validation

### Step 5: Set Up Environment Variables

Create a `.env` file in the project root directory:

**On Windows (Command Prompt):**
```bash
echo. > .env
```

**On Windows (PowerShell):**
```bash
New-Item -ItemType File -Path .env
```

**On macOS/Linux:**
```bash
touch .env
```

Open the `.env` file with your text editor and add:

```env
OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual OpenAI API key.

**⚠️ Important Security Notes:**
- Never commit `.env` file to version control
- Keep your API key confidential
- Rotate your key regularly if it's accidentally exposed

### Step 6: Verify Installation

Test that all dependencies are installed correctly:

```bash
python -c "import streamlit; import yt_dlp; import faster_whisper; import langchain; print('All dependencies installed successfully!')"
```

---

## ⚙️ Configuration

### Environment Variables

The application uses a `.env` file for configuration. Create a `.env` file in the project root with:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

### Optional Configuration

You can customize the following in your `.env`:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-3.5-turbo  # or gpt-4 for better quality
OPENAI_TEMPERATURE=0.7      # 0-1, lower = more deterministic

# Output Configuration
EXPORT_FOLDER=exports        # Folder for saving notes
```

---

## 💻 Usage

### Running the Application

1. **Make sure virtual environment is activated:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Start the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

3. **Access the web interface:**
   - The browser should automatically open to `http://localhost:8501`
   - If not, manually navigate to that URL

### Using the Application

1. **Paste a YouTube URL** in the text input field
2. **Click "Generate Notes"** button
3. **Wait for processing** (audio download → transcription → note generation)
4. **View the generated notes** in the application
5. **Find exported files** in the `exports/` folder:
   - `notes.md` - Markdown format
   - `notes.pdf` - PDF format (if applicable)

### Example YouTube URLs

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
https://www.youtube.com/watch?v=VIDEO_ID&t=START_TIME
```

---

## 📁 Project Structure

```
Youtube-notes-generator/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── README.md                   # This file
│
├── modules/
│   ├── youtube_audio.py       # YouTube audio download functionality
│   ├── whisper_stt.py         # Speech-to-text transcription
│   ├── notes_generator.py     # AI notes generation logic
│   └── __pycache__/           # Python cache (auto-generated)
│
├── exports/                    # Output folder (auto-created)
│   ├── notes.md              # Generated markdown notes
│   └── notes.pdf             # Generated PDF notes
│
└── temp/                       # Temporary files (auto-created)
    └── audio files
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit UI and orchestration |
| `modules/youtube_audio.py` | Handles YouTube video downloading and audio extraction |
| `modules/whisper_stt.py` | Transcribes audio to text using Whisper |
| `modules/notes_generator.py` | Generates AI notes using LangChain and OpenAI |
| `requirements.txt` | Lists all Python package dependencies |
| `.env` | Stores sensitive configuration (API keys) |

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. **"FFmpeg not found" Error**

**Problem:** Application can't find FFmpeg

**Solution:**
- Install FFmpeg using one of these methods:
  ```bash
  # Using Chocolatey (Windows)
  choco install ffmpeg
  
  # Using Windows Package Manager
  winget install ffmpeg
  
  # Using Conda
  conda install ffmpeg
  ```
- Verify installation: `ffmpeg -version`

#### 2. **"OPENAI_API_KEY not found" Error**

**Problem:** `.env` file not set up correctly

**Solution:**
- Verify `.env` file exists in the project root
- Check the file contains: `OPENAI_API_KEY=sk-xxxxx`
- Ensure no extra spaces or special characters
- Restart the Streamlit application after updating `.env`

#### 3. **"ModuleNotFoundError" for any package**

**Problem:** Dependencies not installed or virtual environment not activated

**Solution:**
- Ensure virtual environment is activated: `venv\Scripts\activate` (Windows)
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

#### 4. **YouTube URL Not Working**

**Problem:** Application can't download from certain YouTube videos

**Possible Causes:**
- Video is age-restricted or private
- Video region-locked to specific countries
- Content copyright restrictions
- yt-dlp needs update

**Solution:**
- Verify video is publicly accessible
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Try a different video to test

#### 5. **Slow Transcription or API Rate Limits**

**Problem:** Processing is very slow or getting rate limit errors

**Solution:**
- OpenAI API has usage limits
- Check your OpenAI account for usage and limits
- Consider upgrading your OpenAI API plan
- Use shorter videos for testing

#### 6. **Virtual Environment Not Working**

**Problem:** `venv\Scripts\activate` command not found

**Solution - Windows PowerShell:**
```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

---

## 📋 Requirements

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 4 GB | 8 GB+ |
| Disk Space | 2 GB | 5 GB+ |
| Internet | Required | Fast connection recommended |
| OS | Windows/Mac/Linux | Any |

### API Requirements

- **OpenAI API Key** with valid credits
- Active internet connection for API calls
- YouTube access for video downloading

### Python Packages

See [requirements.txt](requirements.txt) for the complete list of dependencies.

---

## 🤝 Support & Contribution

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Verify all prerequisites are installed
3. Check OpenAI API key validity and available credits
4. Ensure Internet connection is stable

For detailed logs:
```bash
streamlit run app.py --logger.level=debug
```

---

## 📝 License

This project is provided as-is for educational purposes.

---

## ⚡ Quick Start Checklist

- [ ] Python 3.8+ installed and verified
- [ ] FFmpeg installed and verified
- [ ] Project folder created and accessed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] pip upgraded
- [ ] Dependencies installed from requirements.txt
- [ ] `.env` file created with OpenAI API key
- [ ] Installation verified with test command
- [ ] Application started with `streamlit run app.py`
- [ ] Browser opened to `http://localhost:8501`

---

## 🎯 Next Steps

After successful installation:

1. Test with a short YouTube video
2. Monitor console for errors or warnings
3. Check the `exports/` folder for generated notes
4. Explore different video types to understand capabilities
5. Customize the notes generation logic in `modules/notes_generator.py` if needed

---

**Happy Note Taking! 📚✨**
