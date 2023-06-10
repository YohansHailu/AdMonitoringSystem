import cv2
import streamlit as st
import imagehash
import frame_handler as frm_hndlr
import matching_algorithms as algo
import time
from PIL import Image


def get_total_frames(video_path):
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()
    return total_frames


def video_to_image(video_path):
    lines = frm_hndlr.get_line_from_file("ad_hashes")
    i=0
    counter=0
    total_frames = get_total_frames(video_path)
    progress_bar = st.progress(0)
    while True:

        stream_frame=frm_hndlr.get_frame_from_video(video_path,i)
        h1 = imagehash.average_hash(Image.fromarray(cv2.cvtColor(stream_frame, cv2.COLOR_BGR2RGB)))
        for line in lines:
            h2 = imagehash.hex_to_hash(line)
            if abs(h1-h2)<12:
                print(abs(h1-h2),i)
                counter+=1
        i+=10
        # Update the progress bar
        progress = i / total_frames
        progress_bar.progress(progress)

        # Break the loop if all frames have been processed
        if i >= total_frames:
            break        
    print("Number of times frames were matched",counter)


# video_path="/home/adadu/Thesis Project/video_files/5m_short_movie_with_2_ads.mp4"
# video_to_image(video_path)

# ad_hash=frm_hndlr.read_from_text_file("ad_hashes")
# for i in range():
# print(ad_hash)
