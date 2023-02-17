import cv2
import time

from video_file import VideoFile
import frame_matching_algos as fma
print("---------------------")
print("Sift_knn test")
print("---------------------")
# make VideoFile object
video_file = VideoFile("./data_files/test_video_ad_video.webm")

# get two random frames
frame1 = video_file.get_random_frame()
frame2 = video_file.get_random_frame()

# write frame1 and 2 ast test_frame1 and 2
cv2.imwrite("./data_files/test_frame1.jpg", frame1)
cv2.imwrite("./data_files/test_frame2.jpg", frame2)

# compare frame1 with itself
res = fma.sift_knn(frame1, frame1)
print("frame1 is equal to itself: ", res)

# compare frame1 with itself
res = fma.sift_knn(frame1, frame2)
print("frame2 is equal to frame1: ", res)

# change the brightness of frame2
bright_frame2 = cv2.convertScaleAbs(frame2, beta=150)

# compare frame2 with bright_frame2
res = fma.sift_knn(frame2, bright_frame2)
print("frame2 is equal to bright_frame2: ", res)


# crop both 
h, w, c = frame1.shape
crop_frame1_half_width = frame1[int(h/4):int(3*h/4), int(w/4):int(3*w/4)]
res = fma.sift_knn(frame1, crop_frame1_half_width)
print("frame1 is equal to crop_frame1_both_half: ", res)

# crop half_width
h, w, c = frame1.shape
crop_frame1_half_width = frame1[0:int(h), int(w/4):int(3*w/4)]
res = fma.sift_knn(frame1, crop_frame1_half_width)
print("frame1 is equal to crop_frame1_half_width: ", res)

# crop half_height 
h, w, c = frame1.shape
crop_frame1_half_heigth = frame1[int(h/4):int(3*h/4), 0:int(w)]
res = fma.sift_knn(frame1, crop_frame1_half_heigth)
print("frame1 is equal to crop_frame1_half_height: ", res)

# almost no crop 
h, w, c = frame1.shape
crop_frame1_3forth= frame1[int(h/6):int(5*h/6), int(w/10):int(5*w/6)]
res = fma.sift_knn(frame1, crop_frame1_3forth)
print("frame1 is equal to crop_frame1_3forth: ", res)

# almost no crop 
h, w, c = frame1.shape
crop_frame1_full = frame1[int(h/10):int(9*h/10), int(w/10):int(9*w/10)]
res = fma.sift_knn(frame1, crop_frame1_full)
print("frame1 is equal to crop_frame1_almost_no_crop: ", res)


# time it took to compare frame1 and frame2
start_time = time.time()
fma.sift_knn(frame1, frame2)
end_time = time.time()
print('time it took to compre frame1 and frame2: {:.3f} seconds'.format(end_time - start_time))