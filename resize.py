import moviepy.editor as mp


clip = mp.VideoFileClip("videos/june.mp4")
clip_resized = clip.resize(width=600) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized.write_videofile("videos/resized.mp4")