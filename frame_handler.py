import cv2
import imagehash
from PIL import Image

def get_n_hashs(video_path, n = 10):
    video = cv2.VideoCapture(video_path)
    jumping_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) // n
    if not video.isOpened():
        print("Error opening video file")
        return None
    
    hashes = [] 
    frame_index = 0
    for _  in range(0,n):
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        _, frame = video.read()
        h1 = imagehash.average_hash(Image.fromarray(frame))
        #print(type(h1))
        frame_index += jumping_number
        hashes.append(h1)

    return hashes

# testing
if __name__ == "__main__":
    path = "/home/yohansh/Videos/video_files/2m_short_movie_with_10s_mr_been_ad.mp4"
    res = get_n_hashs(path)
    print(*res, end = "\n")
