import imagehash
from PIL import Image
import cv2


def append_to_text_file(content,file_name: str):
    file_path = "/home/adadu/Thesis Project/GUI/hashes/"+file_name+".txt"
    try:
        with open(file_path, 'a') as file:
            file.write(str(content) + '\n')
        print(content)
    except Exception as e:
        print(f"An error occurred while appending to the file: {str(e)}")


def get_line_from_file(file_name):
    file_path = '/home/adadu/Thesis Project/GUI/hashes/'+file_name+'.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def ad_frame_hasher(video_path):
    video = cv2.VideoCapture(video_path)
    frame_number=int(video.get(cv2.CAP_PROP_FRAME_COUNT)) // 10
    if not video.isOpened():
        print("Error opening video file")
        return None
    j=0
    for i in range(0,10):
        video.set(cv2.CAP_PROP_POS_FRAMES, j)
        ret, frame = video.read()
        h1 = imagehash.average_hash(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        j+=frame_number
        append_to_text_file(str(h1),"ad_hashes")
    
    # Set the desired frame number
    video.release()

def get_frame_from_video(video_path, frame_number):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error opening video file")
        return None
    
    # Set the desired frame number
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = video.read()
    video.release()

    if not ret:
        print("Error reading frame")
        return None
        
    return frame





# path="/home/adadu/Thesis Project/Test video/Yap720.mkv"
# ad_frame_hasher(path)