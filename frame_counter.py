# function that will count number of similar frames in a video 
import frame_matching_algos as fma
import cv2
def count_frames(vidoe_file, frame, threshold = 0.7,matching_algo_func = fma.orb):
    print("---------------")
    print("counting frames")
    print("---------------")

    video = vidoe_file.video
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, image = video.read()
    count = 0
    while success:
        success, image = video.read()
        if success:
            if matching_algo_func(image, frame, threshold):
                count += 1
                video.set(cv2.CAP_PROP_POS_FRAMES, video.get(cv2.CAP_PROP_POS_FRAMES) + 25)
    return count
