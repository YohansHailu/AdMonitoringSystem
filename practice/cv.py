import cv2
import numpy as np

img2 = cv2.imread('Screenshot from 2022-12-22 15-07-48.png')
img_gr=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img3=cv2.imread('Screenshot from 2022-12-22 15-07-59.png',0)
w,h= img3.shape[::-1]

match=cv2.matchTemplate(img_gr, img3, cv2.TM_CCOEFF_NORMED)

threshold =0.8
loc = np.where(match >= threshold)

for pt in zip(*loc[::-1]):
	print(loc)
	cv2.rectangle(img2,pt, (pt[0]+w,pt[1]+h), (0,255,255), 2)

cv2.imshow('Result',img2)
cv2.waitKey(0)
