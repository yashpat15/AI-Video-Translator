# AI Video Translator

## Overview
The AI Video Translator is a web application designed to translate video content into multiple languages using advanced AI models. This tool enables users to upload videos, extract audio for transcription, and translate spoken language using OpenAI's Whisper model and Google Cloud Text-to-Speech. It is particularly useful for content creators and businesses looking to make video content accessible in various languages.

## Features
- **Speech-to-Text Transcription**: Utilizes OpenAI's Whisper to accurately convert spoken language from videos into text.
- **Multilingual Translation**: Supports translation into multiple languages, enhancing accessibility for a global audience.
- **Text-to-Speech Conversion**: Converts translated text back into audio, which is then merged back into the video.
- **User-Friendly Interface**: Offers a clean, responsive web interface that simplifies the process of uploading videos and retrieving the translated output.
- **Video Processing**: Merges translated audio with the original video to provide a seamless viewing experience in the selected language.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Flask
- **AI Models**: OpenAI Whisper, Google Cloud Text-to-Speech
- **Video Processing**: FFmpeg, MoviePy

## Getting Started

### Prerequisites
- Python 3.8 or later
- FFmpeg (for video and audio processing)
- Google Cloud Platform account (for Text-to-Speech API)
- Git (for cloning the repository)

### Installation
1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ai-video-translator.git
cd ai-video-translator
```
2. *Set up a virtual environment and activate it:**
   ```bash
   venv\Scripts\activate

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
``` bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/google-cloud-service-account-file.json"
```

### Usage
1. **Run the application:**
```bash
python app.py
```

2. **Navigate to the application:**
Open your web browser and go to `http://127.0.0.1:5000`. Upload a video, select a target language, and submit it for processing.

3. **Download the translated video:**
Once the translation process is complete, download the video directly from the web interface.

