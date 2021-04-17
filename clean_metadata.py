from PIL import Image
import os

# set 
# dir = os.path.dirname(__file__)
# os.chdir(dir)

root_dir = "pi_pics/"

# # find all files
new_files = os.listdir(root_dir)

# remove any file that does not end with .jpg
nf = [x for x in new_files if x.endswith(".jpg")]

# remove existing files that have already been cleaned
existing_files = os.listdir(root_dir + "clean/")
ef = [x.strip("cl") for x in existing_files]

nf = list(set(nf) - set(ef))

# Open and resave each file
# This scrubs the metadata from each image
for n in nf:
    img = Image.open(root_dir + n)
    img.save(root_dir + "clean/cl" + n)
