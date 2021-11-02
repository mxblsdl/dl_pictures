
import os
import re
import calendar
from PIL import Image, ImageDraw, ImageFont

'''
One time annotate of enhanced pics. This functionality has been built into the enhance.py script.
Preserving this for reference.
'''

input_path = "enhanced_pics/to june"

# find all pictures in the directory
pictures = [os.path.join(input_path, p) for p in os.listdir(input_path)]
pictures.sort()

# Loop over every picture and add the month name
for i in range(len(pictures)):

    # open image
    img = Image.open(pictures[i])

    # init a draw class on image
    draw = ImageDraw.Draw(img)

    # set the font, can be set more globally
    font = ImageFont.truetype("DejaVuSans.ttf", 175)

    # find the month of the photo
    s = re.sub(".*2021", "", pictures[i])
    month = s[:2]

    # Convert to name with calendar API
    month = calendar.month_name[int(month)]
    draw.text((25,25), month, fill=(255,255,255, 100), font=font, stroke_fill=(0,0, 0), stroke_width=5)

    img.save(pictures[i])