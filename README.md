
# Pi Camera and Time Lapse Movie

Use a raspberry pi zero to take a picture every day and create a time lapse movie with sound and month name annotations.

## Hardware setup

I am using a [raspberry pi zero](https://www.raspberrypi.com/products/raspberry-pi-zero/) with the [Camera module 2](https://www.raspberrypi.com/products/camera-module-v2/) inside a simple black case. I originally attached the camera to my window frame with
a [tripod stand](https://www.ebay.com/itm/292971440283), but found this to be too flimsy. If things ever got bumped the camera angle would shift slightly and this was very bad for a time lapse series. I ended up using the 'phone holder' to hold the picam with a more sturdy [C-Clamp](https://www.amazon.com/MOSHUSO-Heavy-Clamp-Camera-Articulating/dp/B08SKXS5N3?ref_=ast_sto_dp&th=1&psc=1) I purchased. I am very happy with the Moshuso clamp and would go that route again. 

You can see from this picture that I needed to add a wood spacer since the picam was smaller than any phone the holder was designed for. This setup is nice because it can be attached from any angle. I have attached it to the top of my window frame for a better view of the yard. ![camera](img/cam.png)

## Software scripts (PI)

The pi itself runs a simple script, `takepic.py` 

## Download Pictures

- Connect to Raspberry zero with camera over ssh
- Download all new pictures onto local machine

## Create movie