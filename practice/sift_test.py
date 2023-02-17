import cv2
img = cv2.imread("walia bira ad.jpeg")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(img, keypoints, img)

cv2.imwrite("SIFT_keypoints.jpg", img)
cv2.waitKey()
cv2.destroyAllWindows()
