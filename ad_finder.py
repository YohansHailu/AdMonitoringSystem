import cv2
import streamlit as st
import imagehash
from PIL import Image
from frame_handler import get_n_hashs

def ad_finder(video_path, ad_hashs, threshold = 12, frame_jump=10):

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error opening video file")
        return None
    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # handle st.progress here

    print("dubug: totale frames ", total_frames) 

    cur_frame_index = 0
    num_detected_frames = 0
    num_detected_ads = 0

    one_group_hashs = set(ad_hashs)
    fps = video.get(cv2.CAP_PROP_FPS)
    while True:

        if cur_frame_index % 100 == 0: 
            print(cur_frame_index)

        video.set(cv2.CAP_PROP_POS_FRAMES, cur_frame_index)
        _, stream_frame = video.read()

        h1 = imagehash.average_hash(Image.fromarray(stream_frame))
        if  hash_exist(h1, one_group_hashs, threshold):
            num_detected_frames += 1
            print("frame detected, len of one_group_hash", len(one_group_hashs))

        cur_frame_index += frame_jump

        # time cur_frame_index/fps
        # one ad has been detedect
        if num_detected_frames > len(ad_hashs)//2:
            num_detected_ads += 1
            num_detected_frames  = 0
            one_group_hashs = set(ad_hashs)
            
            time_second = cur_frame_index//fps
            time_minute = cur_frame_index//fps

            print("Time of the ads roughly ", time_minute //60,"m", time_second % 60 , "s")

            cur_frame_index += 100*frame_jump
            print("full ads has been detected", len(one_group_hashs), "must be", len(ad_hashs), "numer of ads detected", num_detected_ads)








        if cur_frame_index >= total_frames:
            break

def hash_exist(hash, hashs, threshold = 12):
    for h in hashs:
        if (hash - h) < threshold: 
            hashs.remove(h)
            return True
    return False



# testing
if __name__ == "__main__":
    live_path = "/home/yohansh/Videos/video_files/2m_short_movie_with_10s_mr_been_ad.mp4"
    ad_path = "/home/yohansh/Videos/video_files/10s_mr_been_ad.mp4"
    
    live_path = "/home/yohansh/Videos/video_files/10m_short_movie_with_4_30s_ed_sheeran_ads.mp4"
    ad_path = "/home/yohansh/Videos/video_files/30s_ed_sheeran_ad.mp4"


    live_path = "/home/yohansh/Videos/video_files/5m_short_movie_with_2_ads.mp4" 
    ad_path = "/home/yohansh/Videos/video_files/20s_coca_cola_ad.mp4"

    hashs = get_n_hashs(ad_path)

    ad_finder(live_path, hashs)



