import cv2
import streamlit as st
import imagehash
from PIL import Image
from frame_handler import get_n_hashs
import datetime
from order_handler import number_to_ordinal
from audio_data_handler import get_audio, calculate_sound_quality

def dumb_progress():
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i)

def ad_finder(video_path, ad_hashs, threshold = 12, frame_jump=10):

    progress_bar = st.progress(0)
    video = cv2.VideoCapture(video_path)
    sound, sr = get_audio(video_path)

    if not video.isOpened():
        print("Error opening video file")
        return None
    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # handle st.progress here

    print("dubug: totale frames ", total_frames) 

    cur_frame_index = 0
    num_detected_frames = 0
    num_detected_ads = 0

    number_ads_text = f'<p>The ad was showing: <b style="font-size:40px">{num_detected_ads}</b> times so far</p>'
    #text_number_ads = st.write(text, unsafe_allow_html=True)
    number_ads_componenet  = st.empty()

    time_staps_expander= st.expander("Time stamps of each Advertizment")
    time_staps_expander.write("here are the time stamps: ", unsafe_allow_html=True)

    display_quality_expander= st.expander("display quality of each advertizment")
    display_quality_expander.write("here are each display qualities: ", unsafe_allow_html=True)

    sound_quality_expander= st.expander("sound quality of each advertizment")
    sound_quality_expander.write("here are each sound qualities: ", unsafe_allow_html=True)


    number_ads_componenet.write(number_ads_text,unsafe_allow_html=True )


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
            
            total_second = cur_frame_index//fps 

            cur_frame_index += 100*frame_jump
            print("full ads has been detected", len(one_group_hashs), "must be", len(ad_hashs), "numer of ads detected", num_detected_ads)

            time_stap_text = str(datetime.timedelta(seconds=total_second))
            time_staps_expander.write("The "+number_to_ordinal(num_detected_ads)+ " Ad is Detected at:  " + time_stap_text, unsafe_allow_html=True)

            display_quality_text = "Video Resolution of the " + number_to_ordinal(num_detected_ads) + " Ad is "+ str(Image.fromarray(stream_frame).size)
            display_quality_expander.write(display_quality_text)



            # totatal sound_part
            start = max(int(total_second) - 5, 0)
            end  = int(total_second)
            sound_part = sound[start*sr:end*sr]
            sound_quality = calculate_sound_quality(sound_part)

            
            sound_quality_str = "{:.2f}".format(sound_quality)
            sound_quality_text = "Sound daynamic range of the " + number_to_ordinal(num_detected_ads) + " Ad is "+ sound_quality_str
            sound_quality_expander.write(sound_quality_text)


        if cur_frame_index >= total_frames:
            break

        progress_bar.progress(cur_frame_index/total_frames)
        number_ads_text = f'<p>The ad was showing : <b style="font-size:40px">{num_detected_ads}</b> times so far</p>'
        number_ads_componenet.write(number_ads_text, unsafe_allow_html=True)
        

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



