from frame_counter import count_frames
from video_file import VideoFile
import frame_matching_algos as fma
import cv2

# test test_frame_counter.count_frames
video_file = VideoFile("./data_files/test_video_ad_video.webm")
frame = video_file.get_random_frame()
#write the frame
cv2.imwrite("./data_files/frame_to_count.png", frame)
count = count_frames(video_file, frame, 0.9, fma.xor_matching)
print(count)
