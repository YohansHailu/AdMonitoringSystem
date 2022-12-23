import cv2
import numpy as np
roadImg = cv2.imread("./mpy.jpeg")

roadImg = cv2.cvtColor(roadImg, cv2.COLOR_BGR2GRAY)
roadImg = cv2.Canny(roadImg, 30, 150)
cv2.imwrite("read_copy.jpg", roadImg)
