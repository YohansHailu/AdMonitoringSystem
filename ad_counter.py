import cv2
from frame_matching_algos import orb as orb_matching
from video_file import VideoFile


def mostly_back_or_white(frame):
    mean_color = cv2.mean(frame)
    mean_color = sum(mean_color[:3]) / 3
    return mean_color > 200 or mean_color < 50 


def get_spaced_frames(n, video_file):
    video = video_file.video 
    frames = []
    
    separation = video_file.total_frames // n
    for i in range(n):
        video.set(cv2.CAP_PROP_POS_FRAMES, i * separation)
        
        ret, frame = video.read()

        # while frame is blank, keep reading
        while not ret and not mostly_back_or_white(frame):
            ret, frame = video.read()

        frames.append(frame) 

    return frames

def count_ads_in_stream(live_stream_name, ad_name):
    stream = VideoFile(live_stream_name)
    ad_video = VideoFile(ad_name)
    
    ad_frames = get_spaced_frames(50, ad_video)
    frame_pointer = 0
    
    counter = 0
    for i in range(stream.total_frames):
        _, frame = stream.video.read()
        if orb_matching(frame, ad_frames[frame_pointer], 0.9):
            frame_pointer += 1 

        if frame_pointer == len(ad_frames):
            counter += 1
            frame_pointer = 0

    return counter


