# import libraries
from vidgear.gears import CamGear
import cv2

stream = CamGear(source='/home/yohansh/Videos/video_files/30s_ed_sheeran_ad.mp4', stream_mode = True, logging=True).start()

while True:
    
    frame = stream.read()
    if frame is None:
        break
    cv2.imshow("Output Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()
