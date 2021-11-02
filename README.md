
# Pi Camera and Time Lapse Movie

Use a raspberry pi zero to take a picture every day and create a time lapse movie with sound and month name annotations.

This repo is intended to act as an example of how to setup a similar project, not as a fully reproducible project.

## Hardware setup

I am using a [raspberry pi zero](https://www.raspberrypi.com/products/raspberry-pi-zero/) with the [Camera module 2](https://www.raspberrypi.com/products/camera-module-v2/) inside a simple black case. I originally attached the camera to my window frame with
a [tripod stand](https://www.ebay.com/itm/292971440283), but found this to be too flimsy. If things ever got bumped the camera angle would shift slightly and this was very bad for a time lapse series. I ended up using the 'phone holder' to hold the picam with a more sturdy [C-Clamp](https://www.amazon.com/MOSHUSO-Heavy-Clamp-Camera-Articulating/dp/B08SKXS5N3?ref_=ast_sto_dp&th=1&psc=1) I purchased. I am very happy with the Moshuso clamp and would go that route again. 

You can see from this picture that I needed to add a wood spacer since the picam was smaller than any phone the holder was designed for. This setup is nice because it can be attached from any angle. I have attached it to the top of my window frame for a better view of the yard. ![camera](img/cam.png)

## Software scripts (PI)

The pi itself runs a simple script, `takepic.py`, that interacts with the camera module and names the file accordingly. The script is included in this repo even though it is loaded separately on the raspberry pi.

### Scheduling the camera

The `takepic.py` script is scheduled with crontab and [sunwait](https://risacher.org/sunwait/). To get the lighting close to similar everyday I take the photo right after sunrise. Since this time is different every day I use the sunwait application to help schedule.

```
0 5 * * * /usr/local/bin/sunwait sun up +0:30:00 45.5051N 122.6750W ; python3 takepic.py
```

At 5am this cronjob is triggered but then waits until 30 minutes after sun rise for the specified latitude and longitude.

## Download Pictures

With the files on the raspberry pi I can periodically run the `1_download_pictures.py` file to download every new file to a directory. The download is performed through SSH and relies on a config file called `server_info.csv` which contains log-in information for the rpi.

The pictures are then saved to a different directory with the `2_clean_metadata.py` which removes metadata associated with the picture. This step is not essential and may be removed in the future as it duplicates the file, albeit without metadata.

After images have been clean there is a manual process of reviewing the images and deleting images that are too dark, too sunny, etc. I have not been able to automate this process but hope to reduce this as the sunwait is refined. 

## Create movie

Once a set of pictures has been finalized they can be stitched together with the `main.py` script. 

Some constants are defined in the script including the audio file to include and whether to annotate the video. This script also runs some image enhancements to increase brightness, saturation, and image 'pop'. 