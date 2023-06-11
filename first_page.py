import streamlit as st
import tempfile 
import validators
import os

from time import sleep
import streamlit as st
from stqdm import stqdm
from frame_handler import get_n_hashs
from ad_finder import ad_finder, dumb_progress

st.sidebar.write("<h1 style='font-size:50px'>📺   AdMonitor</h1>", unsafe_allow_html=True)
st.sidebar.header("How to Use?")

st.sidebar.write("<li>first add your advertisement video in the browser filei </h1>", unsafe_allow_html=True)
st.sidebar.write("<li>Then put the link for the live stream and clik on start monitoring button</li>", unsafe_allow_html=True)
st.sidebar.write("<li>then you will be able to see results at the bootom", unsafe_allow_html=True)



st.sidebar.write("<h1 style='font-size:30px; padding-top:60px'>👷 Engineers</h1>", unsafe_allow_html=True)
st.sidebar.write("<li>Yohans Hailu</li>", unsafe_allow_html=True)
st.sidebar.write("<li>Yohannis solomon</li>", unsafe_allow_html=True)
st.sidebar.write("<li>Yohanes fiseha</li>", unsafe_allow_html=True)

st.sidebar.write("<h1 style='font-size:30px; padding-top:60px'>📚 Advisor</h1>", unsafe_allow_html=True)
st.sidebar.write("<b><li>Rediet Million</li></b>", unsafe_allow_html=True)





file_submited = [False]
hashed_ad_frames = [] 

def get_video_path(uploaded_video):
    temp_file = tempfile.NamedTemporaryFile(delete=False) 

    # save video file again as temp file
    temp_file.write(uploaded_video.read()) 
    return temp_file.name



st.write("<h1>Welcome to our Project 👋</h1>", unsafe_allow_html=True)
#st.write('**Upload your advertisement video here:**')
ad_video = st.file_uploader('')

if ad_video:
    ad_path = get_video_path(ad_video)
    st.write('<b style="font-size:25px">Your advertisement video:</b>', unsafe_allow_html=True)
    st.video(ad_video)

    ad_path = get_video_path(ad_video)
    hashed_ad_frames =  get_n_hashs(ad_path)





live_stream_path = st.text_input("**Put the link of stream**")
is_valid_input = os.path.isfile(live_stream_path) or  validators.url(live_stream_path)



view_live_button_clicked = False 
start_scanning_button  = False

view_live_button_clicked = st.button("Display and Start Monitoring") or view_live_button_clicked 

if view_live_button_clicked:
    if is_valid_input:
        st.write("<u><b style='25px'>Here is the live stream video</b></u>", unsafe_allow_html=True)
        st.video(live_stream_path)
        

        # start scaning
        #dumb_progress()
        ad_finder(live_stream_path, hashed_ad_frames )
        st.markdown("----")
        st.button("Save result as Text") 



    else:
        st.warning('Please Enter valid link', icon="⚠️")
