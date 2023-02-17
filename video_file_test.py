import cv2
# test the class
from video_file import VideoFile
ad_video = VideoFile("./data_files/test_video_ad_video.webm")

print("total frames:", ad_video.total_frames)
print("fps:", ad_video.fps)
# get random frame and write it as random_frame.jpg from ad_video and also show it
cv2.imwrite("./data_files/random_frame.jpg", ad_video.get_random_frame())
