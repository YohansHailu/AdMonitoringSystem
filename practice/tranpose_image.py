# autor yohans hailu
import cv2
roadImg = cv2.imread("./road.jpg")

roadImg = roadImg.transpose((1,0,2))
cv2.imwrite("read_copy.jpg", roadImg)
