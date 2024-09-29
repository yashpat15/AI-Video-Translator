def translate_text(text, target_language='fr'):
    from googletrans import Translator
    translator = Translator()
    
    try:
        text_chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
        translated_chunks = []

        for chunk in text_chunks:
            translated = translator.translate(chunk, dest=target_language)
            translated_chunks.append(translated.text)
            
        translated_text = " ".join(translated_chunks)
        print(f"Translated text: {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None
