import os
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import re
import calendar

###
'''
Apply enhancements to the pictures 
'''
###
def enhance_images(img, output_path, annotate=False):
    print(output_path)
    im = Image.open(img)
    en = ImageEnhance.Contrast(im).enhance(1.4)
    en = ImageEnhance.Sharpness(en).enhance(1.5)
    en = ImageEnhance.Color(en).enhance(1.4)

    if annotate:
        # init a draw class on image
        draw = ImageDraw.Draw(en)

        # set the font, can be set more globally
        font = ImageFont.truetype("DejaVuSans.ttf", 175)

        # find the month of the photo
        s = re.sub(".*2021", "", img)
        month = s[:2]

        # Convert to name with calendar API
        month = calendar.month_name[int(month)]
        
        # Add text to each picture
        draw.text((25,25), month, fill=(255,255,255, 100), font=font, stroke_fill=(0,0, 0), stroke_width=5)

    en.save(output_path)

# Create path list
def find_files_enhance(input_path, output_path, annotate):
    
    # remove trailing slash if it exists
    output_path = output_path.rstrip("/")

    # Find all files and sort chronologically
    pictures = [os.path.join(input_path, p) for p in os.listdir(input_path)]
    pictures.sort()

    # Create list of names for final files
    pic_names = [ os.path.join(output_path, pic.replace(input_path + "/cl", "")) for pic in pictures]

    # Save images in new dir
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # open each image, apply enhancements, and save
    for i in range(len(pic_names)):
        # Check that the file exists before overwriting
        if not os.path.isfile(pic_names[i]):
            enhance_images(img = pictures[i], output_path = pic_names[i], annotate = annotate)
