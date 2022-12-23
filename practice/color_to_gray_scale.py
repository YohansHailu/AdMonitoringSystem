import cv2
import numpy as np
roadImg = cv2.imread("./mpy.jpeg")

grayScale = np.zeros(roadImg.shape[:2])
for i in range(len(roadImg)):
    for j in range(len(roadImg)):
        grayScale[i][j] = sum(roadImg[i][j])//3

cv2.imwrite("read_copy.jpg", grayScale)
