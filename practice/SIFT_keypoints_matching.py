import cv2

# Load the images
img1 = cv2.imread("walia bira ad.jpeg")
img2 = cv2.imread("walia bira ad_copy.jpeg")
img2 = cv2.imread("walia bira_2.jpg")

# Create SIFT object
sift = cv2.xfeatures2d.SIFT_create()

# Detect keypoints and extract descriptors
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Create BFMatcher object
bf = cv2.BFMatcher()

# Match the descriptors
matches = bf.knnMatch(des1, des2, k=2)
print(matches[0])
for m,n in matches:
    print(m.distance, n.distance)

# Sort the matches by distance
#matches = sorted(matches, key = lambda x:x.distance)

# Draw the top matches
#img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)

# Show the image
#cv2.imwrite("Matches.jpg", img3)
