import cv2
import numpy as np

#Check if two frames match using knn and SIFT_create
def sift_knn(frame_a, frame_b):
    sift = cv2.xfeatures2d.SIFT_create()
    _, des1 = sift.detectAndCompute(frame_a, None)
    _, des2 = sift.detectAndCompute(frame_b, None)

    if des1 is None or  des2 is None:
        return False

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good_matches = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
          good_matches += 1

    match_ratio = good_matches / min(len(des1), len(des2))

    return match_ratio > 0.4

# Check if two frames match using template matching
def template_matching(frame_a, frame_b):
    height, width = frame_b.shape[:2]
    frame_a = cv2.resize(frame_a, (width, height))


    result = cv2.matchTemplate(frame_a, frame_b, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    threshold = 0.8
    if max_val > threshold:
        return True
    else:
        return False

# Check if two frames match using xor
def are_matching_xor(frame_a, frame_b):
    equal_shape = frame_a.shape == frame_b.shape 
    if equal_shape and not np.bitwise_xor(frame_a, frame_b).any():
        return True

    return False
