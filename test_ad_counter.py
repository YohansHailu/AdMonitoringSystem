import ad_counter
import cv2
from video_file import VideoFile

def test_mostly_back_or_white(video_file_name):
    cap = cv2.VideoCapture(video_file_name)
    # get number of frames
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    count = 0
    for i in range(n):
        ret, frame = cap.read()
        res = (ad_counter.mostly_back_or_white(frame))
        count += res
        if res and i < 2000:
            # write the frame
            print("writing")
            cv2.imwrite("./data_files/frame_{}.jpg".format(i), frame)



def test_spaced_frames(video_file_name):
    live_stream_vidoe = VideoFile(video_file_name)
    frames = ad_counter.get_spaced_frames(10, live_stream_vidoe)
    for i, frame in enumerate(frames):
        cv2.imwrite("./data_files/frame_{}.jpg".format(i), frame)


def test_count_ads_in_stream(live_stream_name, ad_name):
    res = ad_counter.count_ads_in_stream(live_stream_name, ad_name)
    print(res)



#test_mostly_back_or_white("./data_files/live_stream_video_test.mkv")
#test_spaced_frames("./data_files/live_stream_video_test.mkv")
test_count_ads_in_stream("./data_files/live_stream_video_test.mkv", "./data_files/live_stream_video_test.mkv")
