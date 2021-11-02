import cv2
import os


def make_movie(image_folder, video_name, fps):
    '''
    Find all images, sort, and stich into a movie
    '''
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, fps, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()