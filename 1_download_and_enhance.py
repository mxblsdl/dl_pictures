from src import download_pictures, enhance

"""
Take cleaned photos and return a finished video composite with audio added.
The video will contain annotated month names white annotate=True

When audio is added this script will produce a video with and without sound
"""

# Define path file constants ----------------------------------

# TODO currently need to move images into a special folder to make the movie from

# Pictures ------------------------
input_path = "pi_pics"
output_path = "enhanced_pics/all"


# Download files from camera --------------------
download_pictures.dl_pictures(server_info="server_info.csv", output_path="pi_pics")

# Run picture enhancements
# Can set annotations for the pictures
enhance.find_files_enhance(
    input_path=input_path, output_path=output_path, annotate=True
)
