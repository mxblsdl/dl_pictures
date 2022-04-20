import moviepy.editor as mpe
from os import remove


def add_sound(video, audio, fps, clean_up=False):
    # Load audio and video clips
    my_clip = mpe.VideoFileClip(video)
    audio_background = mpe.AudioFileClip(audio)

    # Set the suration of the audio to length of video clip
    audioclip = audio_background.set_duration(my_clip.duration)

    # Apply audio to video
    final_clip = my_clip.set_audio(audioclip)

    output = video.replace(".avi", ".mp4")

    final_clip.write_videofile(output, fps=fps, audio_codec="aac")

    # Delete original file if no longer needed
    if clean_up:
        remove(video)
