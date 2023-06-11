# import libraries
from vidgear.gears import CamGear
import cv2
import streamlit as st

#url = "https://youtu.be/KEPf48yztts"
#url = "https://youtu.be/ZBbMk-Ej0Xk"
url = st.text_input("Put link to the live stream")
start_button = st.button("start scaning")
if start_button:
    stream = CamGear(source=url, stream_mode = True, logging=True).start()

    num_frames = int(stream.stream.get(cv2.CAP_PROP_FRAME_COUNT))
    print(num_frames)
    i = 0 

    cur_frame_index = 0
    index = 0
    while True:
        
        #stream.stream.set(cv2.CAP_PROP_POS_FRAMES, cur_frame_index)
        
        frame = stream.read()
        if i < cur_frame_index:
            i += 1
            continue

        print(i)
        cur_frame_index += 10
        if cur_frame_index >= 1000:
            break
        index += 1
    cv2.destroyAllWindows()
    stream.stop()
    st.write("done scaning")
