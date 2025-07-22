from moviepy.editor import VideoFileClip, AudioFileClip

def merge_audio_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    final = video.set_audio(audio)
    output_path = "static/final_videos/final_output.mp4"
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

    return output_path
