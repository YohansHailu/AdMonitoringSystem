import streamlit as st
import tempfile 
import validators
import os

from time import sleep
import streamlit as st
from stqdm import stqdm
import logic as match
import frame_handler as imhs

import matcher


def get_video_path(uploaded_video):
    temp_file = tempfile.NamedTemporaryFile(delete=False) 

    # save video file again as temp file
    temp_file.write(uploaded_video.read()) 
    return temp_file.name

def ad_input_section():
    # upload you file here

    ad_video = st.file_uploader("Upload your Ad please")

    if ad_video:
        ad_path = get_video_path(ad_video)
        st.header("your Advertizment video")
        #_, container, _ = st.columns([0, 3, 0])
        #container.video(ad_video)
        imhs.ad_frame_hasher(ad_path)
        st.video(ad_video)

def live_stream_input_section():

    # video uploading
    live_stream_path = st.text_input("Put link to the live stream")

    is_valid_input = os.path.isfile(live_stream_path) or  validators.url(live_stream_path)



        # Create a button with the custom CSS class
    button_clicked = st.button("Submit and Start Monitoring")




    if button_clicked:
        if is_valid_input:
            st.text("here is the live stream video")
            matcher.video_to_image(live_stream_path)
            st.video(live_stream_path)
        else:
            st.text("Error path: please enter the correct live stream link or path")



def monitoring_section():
    # start moinitoring big botton
    # progress bar
    
    
    for _ in stqdm(range(4), st_container=st):
        sleep(0.5)
    
    # The Ad was showed 
    st.write(f'<p>The ad was showing: <b style="font-size:40px">{3}</b> times</p>', unsafe_allow_html=True)

    expander1 = st.expander("Time stamps of each Advertizment")
    expander1.write("hello")
    expander1.image("https://static.streamlit.io/examples/dice.jpg")


    expander2 = st.expander("Display quality of each Advertizemnt")
    expander2.write("hello")
    expander2.image("https://static.streamlit.io/examples/dice.jpg")


    expander3 = st.expander("Sound Quality of Each Advertizment")
    expander3.write("hello")
    expander3.image("https://static.streamlit.io/examples/dice.jpg")

    st.button("Save result as Text") 


style = """
    .css-x78sv8 e16nr0p3{
        border-color: rgb(255, 75, 75);
    }
    
    div[data-testid*="stHorizontalBlock"] > .css-x78sv8  p {
        font-size:50px;
    }

"""




st.write("<h1>Hello and Welcome to our Project</h1>", unsafe_allow_html=True)
st.sidebar.header("We might need a side bar")

ad_input_section()
live_stream_input_section()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
monitoring_section()

