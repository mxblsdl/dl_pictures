import sys
sys.path.append("src/")

from movie import make_movie
import enhance
import add_sound

'''
Take cleaned photos and return a finished video composite with audio added.
The video will contain annotated month names white annotate=True

When audio is added this script will produce a video with and without sound
'''

# Define path file constants ----------------------------------

# Pictures ------------------------
input_path = "pi_pics/clean/june to oct"
output_path = "enhanced_pics/june to oct"

# Video ---------------------------
# An mp4 will also be created with audio
# TODO remove need for extension
video_name = 'videos/fall.avi'

# Audio ----------------------------
audio_file = "sound/inspo.mp3"

enhance.find_files_enhance(input_path = input_path, output_path = output_path, annotate=True)

# # Stich together movie of enhanced pictures
make_movie(image_folder=output_path, video_name=video_name, fps=3)

# add sound
# more files available here: https://www.chosic.com/free-music/all/
add_sound.add_audio(video=video_name, audio = audio_file, fps=3)

