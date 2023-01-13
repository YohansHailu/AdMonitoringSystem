import cv2
import os
import numpy as np
import random

def get_random_frame(video_file_name):
    cap = cv2.VideoCapture(video_file_name)
    if not cap.isOpened():
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
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

def matching_frame_in_video(video_name, frame):
    video = cv2.VideoCapture(video_name)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for i in range(total_frames):
        ret, cur_frame = video.read()
        if not ret:
            break
        equal_shape = cur_frame.shape == frame.shape 
        if equal_shape:
            equal_bits = not np.bitwise_xor(cur_frame, frame).any()
            if equal_bits: 
                return (True, i)

    video.release()
    return (False, -1)

def get_fps(video_file_name):
    video = cv2.VideoCapture(video_file_name)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def get_time_two_frames(video_file_name, frame_a, frame_b):
    res, index_a =  matching_frame_in_video(video_file_name, frame_a)
    res, index_b =  matching_frame_in_video(video_file_name, frame_b)
    
    num_frames_between = abs(index_a - index_b)
    fps = get_fps(video_file_name)    
    return num_frames_between//fps

video_file_name = "./sample_video.mp4"
video_file_name2 = "./sample2.mp4"
#last_frame = get_the_last_frame(video_file_name)
#cv2.imwrite("last_frame.jpg", last_frame)

random_frame = get_random_frame(video_file_name)
random_frame2 = get_random_frame(video_file_name)
print(get_time_two_frames(video_file_name,random_frame, random_frame2), "s")
