from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    try:
       
        video = VideoFileClip(video_path)
        
        audio = video.audio
        audio.write_audiofile(output_audio_path)

        print(f"Audio extracted and saved to {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None
