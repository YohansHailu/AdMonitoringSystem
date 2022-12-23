import cv2
import numpy as np
roadImg = cv2.imread("./mpy.jpeg")

roadImg = cv2.cvtColor(roadImg, cv2.COLOR_BGR2GRAY)
#roadImg = cv2.adaptiveThreshold(roadImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
#roadImg = cv2.Laplacian(roadImg, cv2.CV_64F)
#roadImg = np.uint8(np.absolute(roadImg))
roadImg = cv2.Canny(roadImg, 30, 150)
#_, roadImg = cv2.threshold(roadImg, 155,255, cv2.THRESH_BINARY_INV)
cv2.imwrite("read_copy.jpg", roadImg)
