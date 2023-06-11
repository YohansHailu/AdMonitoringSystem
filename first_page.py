import streamlit as st
import tempfile 
import validators
import os

from time import sleep
import streamlit as st
from stqdm import stqdm
from frame_handler import get_n_hashs
from ad_finder import ad_finder, dumb_progress

st.sidebar.header("Here we put on what the project is")
st.sidebar.header("And also how to use the project")

file_submited = [False]
hashed_ad_frames = [] 

def get_video_path(uploaded_video):
    temp_file = tempfile.NamedTemporaryFile(delete=False) 

    # save video file again as temp file
    temp_file.write(uploaded_video.read()) 
    return temp_file.name



st.write("<h1>Hello and Welcome to our Project</h1>", unsafe_allow_html=True)
ad_video = st.file_uploader("Upload the your Ad please")

if ad_video:
    ad_path = get_video_path(ad_video)
    st.header("your Advertizment video")
    st.video(ad_video)

    ad_path = get_video_path(ad_video)
    hashed_ad_frames =  get_n_hashs(ad_path)





live_stream_path = st.text_input("Put link to the live stream")
is_valid_input = os.path.isfile(live_stream_path) or  validators.url(live_stream_path)


view_live_button_clicked = False 
start_scanning_button  = False

view_live_button_clicked = st.button("View the live stream") or view_live_button_clicked 

if view_live_button_clicked:
    if is_valid_input:
        st.text("here is the live stream video")
        st.video(live_stream_path)
        
        print("view button ", view_live_button_clicked)
        print("view button inside start_scaning", view_live_button_clicked)

        
        

        # start scaning
        #dumb_progress()
        ad_finder(live_stream_path, hashed_ad_frames )
        st.markdown("----")
        st.button("Save result as Text") 



    else:
        st.text("red color: please inter the live stream")
