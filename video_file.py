import cv2
import random

class VideoFile:
    def __init__(self, vidoe_file_name) -> None:
        print("loging: VideoFile created", vidoe_file_name)
        self.video_file_name = vidoe_file_name
        self.video = cv2.VideoCapture(vidoe_file_name)
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
    

    def get_last_frame(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.total_frames - 1)
        ret, frame = self.video.read()
        self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if ret:
            return frame
        return None

    # get a random frame of the video
    def get_random_frame(self, portion = 1):
        total_frames = self.total_frames * portion
        frame_num = round(total_frames * random.random())
        self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = self.video.read()
        if ret:
            return frame
        return None

    # when the object is deleted, release the video
    def __del__(self):
        print("loging: VideoFile object is deleted")
        self.video.release()
