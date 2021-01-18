from PIL import Image
import os

# set 
root_dir = "../pi_pics/"

# find all files
existing_files = os.listdir(root_dir)

# remove any file that does not end with .jpg
ef = [x for x in existing_files if x.endswith(".jpg")]

# Open and resave each file
# This scrubs the metadata from each image
for e in ef:
    img = Image.open(root_dir + e)
    img.save(root_dir + "clean/cl" + ef)


