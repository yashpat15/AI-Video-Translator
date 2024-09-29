import whisper
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import ffmpeg
from app.audio_extraction import extract_audio_from_video
from app.text_translation import translate_text
from app.text_to_speech import text_to_speech
from app.video_processing import merge_audio_with_video

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    language = request.form.get('language', 'fr')  
    
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file:
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(video_path)
        
        return redirect(url_for('process_video', video_file=file.filename, language=language))
    
    return redirect(url_for('index'))

def convert_audio_to_wav(input_audio_path, output_audio_path):
    try:
        ffmpeg.input(input_audio_path).output(output_audio_path, ac=1, ar='16000').run()
        print(f"Audio converted to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error converting audio: {e}")
        return None

def whisper_transcribe(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

@app.route('/process/<video_file>')
def process_video(video_file):
    language = request.args.get('language', 'fr')
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file)
    audio_path = os.path.join(app.config['RESULT_FOLDER'], 'extracted_audio.wav')

    extract_audio_from_video(video_path, audio_path)

    converted_audio_path = os.path.join(app.config['RESULT_FOLDER'], 'converted_audio.wav')
    convert_audio_to_wav(audio_path, converted_audio_path)

    transcribed_text = whisper_transcribe(converted_audio_path)
    if not transcribed_text or transcribed_text.strip() == "":
        print("Error: Transcription is empty.")
        return redirect(url_for('index'))
    
    print(f"Transcribed Text: {transcribed_text}")

    translated_text = translate_text(transcribed_text, target_language=language)
    if not translated_text:
        print("Error: Translation failed.")
        return redirect(url_for('index'))

    translated_audio_path = os.path.join(app.config['RESULT_FOLDER'], 'translated_audio.mp3')
    text_to_speech(translated_text, translated_audio_path, language=language)

    output_video_path = os.path.join(app.config['RESULT_FOLDER'], 'final_output.mp4')
    merge_audio_with_video(video_path, translated_audio_path, output_video_path)

    return send_file(output_video_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

