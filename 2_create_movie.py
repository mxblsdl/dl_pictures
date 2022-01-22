from src import movie, add_sound


# Create movie ----------------------------------------------

# Video ---------------------------
# An mp4 will also be created with audio
video_name = "one_year.avi"
input_path = "enhanced_pics/jan to jan"

# Audio ----------------------------
audio_file = "sound/inspo.mp3"


# # Stich together movie of enhanced pictures
movie.movie(image_folder=input_path, video_name=f"videos/{video_name}", fps=5)

# add sound
# more files available here: https://www.chosic.com/free-music/all/
add_sound.add_sound(video=f"videos/{video_name}", audio=audio_file, fps=5)
