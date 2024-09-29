import ffmpeg
import os

def merge_audio_with_video(video_path, audio_path, output_path):
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        print(f"Video path: {video_path}")
        print(f"Audio path: {audio_path}")
        print(f"Output path: {output_path}")

        input_video = ffmpeg.input(video_path)
        input_audio = ffmpeg.input(audio_path)

        output = ffmpeg.output(input_video.video, input_audio, output_path, vcodec='copy', acodec='aac', strict='experimental')

        ffmpeg.run(output)
        print(f"Video with translated audio only saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error merging audio with video: {e}")
        return None
