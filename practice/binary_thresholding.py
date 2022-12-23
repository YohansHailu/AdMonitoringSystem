import cv2
import numpy as np
roadImg = cv2.imread("./mpy.jpeg")

roadImg = cv2.cvtColor(roadImg, cv2.COLOR_BGR2GRAY)
roadImg = cv2.GaussianBlur(roadImg, (5,5),0)
_, roadImg = cv2.threshold(roadImg, 155,255, cv2.THRESH_BINARY_INV)
cv2.imwrite("read_copy.jpg", roadImg)
