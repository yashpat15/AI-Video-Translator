import speech_recognition as sr

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()


    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return None
