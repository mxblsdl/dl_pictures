import moviepy.editor as mpe


def add_audio(video, audio, fps):
    # Load audio and video clips
    my_clip = mpe.VideoFileClip(video)
    audio_background = mpe.AudioFileClip(audio)
    
    # Set the suration of the audio to length of video clip
    audioclip = audio_background.set_duration(my_clip.duration)

    # Apply audio to video
    final_clip = my_clip.set_audio(audioclip)

    output = video.replace(".avi", ".mp4")

    final_clip.write_videofile(output,fps=fps, audio_codec="aac")