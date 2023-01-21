import cv2
import os
import numpy as np
import random
import itertools
import math

def get_random_frame(video_file_name, portion = 1):
    cap = cv2.VideoCapture(video_file_name)
    if not cap.isOpened():
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames *= portion
    frame_num = round(total_frames * random.random())
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    cap.release()
    if ret:
        return frame
    return None

def get_the_last_frame(video_file_name):
    cap = cv2.VideoCapture(video_file_name)
    if not cap.isOpened():
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_num = total_frames - 1
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    cap.release()
    if ret:
        return frame
    return None

# matching using exact bits xor
def are_matching_xor(frame_a, frame_b):
    equal_shape = frame_a.shape == frame_b.shape 
    if equal_shape and not np.bitwise_xor(frame_a, frame_b).any():
        return True

    return False

def matching_frame_in_video(video_name, frame):

    video = cv2.VideoCapture(video_name)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in range(total_frames):
        ret, cur_frame = video.read()
        if not ret:
            break
        #frames_matched = are_matching_xor(cur_frame, frame)
        #frames_matched = are_matching_sift_knn(cur_frame, frame)
        frames_matched = are_matching_template_matching(cur_frame, frame)
        if frames_matched:
            return (True, i)

    video.release()
    return (False, -1)

def get_fps(video_file_name):
    video = cv2.VideoCapture(video_file_name)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def get_time_two_frames(video_file_name, frame_a, frame_b):
    _, index_a =  matching_frame_in_video(video_file_name, frame_a)
    _, index_b =  matching_frame_in_video(video_file_name, frame_b)
    
    num_frames_between = abs(index_a - index_b)
    fps = get_fps(video_file_name)    
    return num_frames_between//fps


# matching using exact bits xor
def are_matching_xor(frame_a, frame_b):
    equal_shape = frame_a.shape == frame_b.shape 
    if equal_shape and not np.bitwise_xor(frame_a, frame_b).any():
        return True

    return False

# matching SIFT and KNN
# n**2 time comlexity too slow
def are_matching_sift_knn(frame_a, frame_b):
    sift = cv2.xfeatures2d.SIFT_create()
    _, des1 = sift.detectAndCompute(frame_a, None)
    _, des2 = sift.detectAndCompute(frame_b, None)

    if des1 is None or  des2 is None:
        return False

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good_matches = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
          good_matches += 1

    match_ratio = good_matches / min(len(des1), len(des2))

    return match_ratio > 0.4

def are_matching_template_matching(frame_a, frame_b):
    height, width = frame_b.shape[:2]
    frame_a = cv2.resize(frame_a, (width, height))


    result = cv2.matchTemplate(frame_a, frame_b, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8
    if max_val > threshold:
        return True
    else:
        return False

#img1 = cv2.imread("walia bira ad.jpeg")
#img2 = cv2.imread("walia bira ad_copy.jpeg")
#img3 = cv2.imread("walia bira_2.jpg")
#print(are_matching_sift_knn(img1, img3))

#walia_beer_frame = cv2.imread("walia bira_2.jpg")
#walia_ad_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#random_walia_frame = get_random_frame(walia_ad_file_name)
#cv2.imwrite("random walie frame.jpg", random_walia_frame)
#print(are_matching_sift_knn(random_walia_frame, walia_beer_frame))

#walia_beer_frame = cv2.imread("walia bira_2.jpg")
#walia_ad_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#res = matching_frame_in_video(walia_ad_file_name, walia_beer_frame)


frame_a = cv2.imread("./sample_rand_frame.jpg")
walia_ad_file_name  = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
res = matching_frame_in_video(walia_ad_file_name, frame_a)
print(res)


#video_file_name = "./WALIA BEER TVC (Directors' Cut) [DPJBDupSiwA].webm"
#random_frame = get_random_frame(video_file_name, 0.2)
#random_frame2 = get_random_frame(video_file_name, 0.2)
#cv2.imwrite("rand_img.jpg",random_frame)
#cv2.imwrite("rand_imge2.jpg",random_frame2)
#
#_, index_a =  matching_frame_in_video(video_file_name, random_frame2)
#_, index_b =  matching_frame_in_video(video_file_name, random_frame)
#print(index_a)
#print(index_b)
#print(get_time_two_frames(video_file_name,random_frame, random_frame2), "s")



#img1 = cv2.imread("walia bira ad.jpeg")
#img2 = cv2.imread("walia bira ad_copy.jpeg")
#img3 = cv2.imread("walia bira_2.jpg")
#print(are_matching_template_matching(img1, img2))


