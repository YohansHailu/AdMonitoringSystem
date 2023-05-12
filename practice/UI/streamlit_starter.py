import streamlit as st

st.set_page_config(page_title="Tweet", page_icon="🤖")

st.markdown("---")
st.header("image uploading using link")
st.spinner("Please wait while your Tweet is being generated...")

default_image_address = "https://dailypost.ng/wp-content/uploads/2018/01/Ugochi-Ihezue.jpg"
topic = st.text_input(label="put you image link to display", placeholder="link .. ")
if not topic:
    topic = default_image_address
st.image(topic)

st.markdown("-----------")
st.header("take image from camera")
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

st.markdown("----")
st.header("local image uploading")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    image = uploaded_file.getvalue()
    st.image(image)

st.markdown("-----------")
st.header("video uploading")
uploaded_file = st.file_uploader("Choose a video file file")
if uploaded_file:
    video = uploaded_file.getvalue()

    _, container,_ = st.columns([10, 10, 30])
    container.video(video)

st.markdown("-----------")
st.header("from link")
video_link = st.text_input(label="input video link adress of the live stream", placeholder="link ..")
if video_link == "":
    video_link = "https://www.youtube.com/watch?v=PsfVYQ8zd4M&list=RDMMcw3zMU6upes&index=19&ab_channel=AbbyLakew" 

_, container,_ = st.columns([10, 10, 30])
container.video(video_link)



