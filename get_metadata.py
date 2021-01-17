
from PIL import Image, ExifTags
import os

# set 
root_dir = "../pi_pics/"

existing_files = os.listdir(root_dir)

# define function to get metadata from each picture
def get_metadata(filepath):

    # TODO fix root_dir here, files should have relative path included
    img = Image.open(root_dir + filepath)

    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return(exif)


o = map(get_metadata, existing_files)

