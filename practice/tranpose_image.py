# autor yohans hailu
import cv2
roadImg = cv2.imread("./road.jpg")

roadImg = roadImg.transpose((1,0,2))
cv2.imwrite("read_copy.jpg", roadImg)

# adaptive treshold
roadImg = cv2.adaptiveThreshold(roadImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
#roadImg = cv2.GaussianBlur(roadImg, (5,5),0)
#_, roadImg = cv2.threshold(roadImg, 155,255, cv2.THRESH_BINARY_INV)
cv2.imwrite("adaptive_read_copy.jpg", roadImg)
