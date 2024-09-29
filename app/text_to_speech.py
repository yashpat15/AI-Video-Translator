from gtts import gTTS

def text_to_speech(text, output_audio_path, language='en'):

    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_audio_path)
        print(f"Speech saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")
        return None
