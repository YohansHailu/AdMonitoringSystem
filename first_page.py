import streamlit as st
import tempfile 
import validators
import os

from time import sleep
import streamlit as st
from stqdm import stqdm
from frame_handler import get_n_hashs

file_submited = [False]

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

start_button_clicked = st.button("Submit and Start Monitoring")
if start_button_clicked:
    if is_valid_input:
        st.text("here is the live stream video")
        st.video(live_stream_path)
    else:
        st.text("red color: please inter the live stream")



progress_bar = st.container()
st.write(f'<p>The ad was showing: <b style="font-size:40px">{3}</b> times so far</p>', unsafe_allow_html=True)
st.write("show the results below: ")

expander1 = st.expander("Time stamps of each Advertizment")
expander1.write("ad 1 at 6:00 oclock")
expander1.write("ad 2 at 6:14")
expander1.write("ad 3 at 6:15")


expander2 = st.expander("Display quality of each Advertizemnt")
expander2.write("diplay qulaity of ad 1")
expander2.write("diplay qulaity of ad 2")
expander2.write("diplay qulaity of ad 3")


expander3 = st.expander("Sound Quality of Each Advertizment")
expander3.write("sound qulaity of ad 1")
expander3.write("sound qulaity of ad 2")
expander3.write("sound qulaity of ad 3")

if file_submited[0]:
    for _ in stqdm(range(4), st_container=progress_bar):
        sleep(5)

# The Ad was showed 

st.button("Save result as Text") 



st.sidebar.header("Here we put on what the project is")
st.sidebar.header("And also how to use the project")
