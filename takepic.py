import pytz
from picamera import PiCamera
from datetime import datetime

now = datetime.now(pytz.timezone("US/Pacific"))

dtime_str = now.strftime("%Y%m%d_%H:%M")

filename = "pictures/" + dtime_str + ".jpg"

camera = PiCamera()

camera.rotation = 90
camera.iso = 80

# set camera resolution to maximum
camera.resolution = {3280, 2464}

camera.capture(filename)
