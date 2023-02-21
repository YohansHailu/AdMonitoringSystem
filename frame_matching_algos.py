import cv2
import numpy as np

#Check if two frames match using knn and SIFT_create
def sift(frame_a, frame_b,  threshold = 0.4):
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

    num_matches = good_matches
    denom_matches = min(len(des1), len(des2))

    if denom_matches == 0:
        return False

    match_ratio = num_matches / denom_matches

    return match_ratio > threshold

# Check if two frames match using surf
def surf(frame_a, frame_b, threshold = 0.5):
    # Detect keypoints and compute descriptors for both images
    surf = cv2.xfeatures2d.SURF_create()
    kp1, des1 = surf.detectAndCompute(frame_a, None)
    kp2, des2 = surf.detectAndCompute(frame_b, None)

    # Create a BFMatcher object
    bf = cv2.BFMatcher()

    # Match descriptors between the two images
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test to filter out false matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    
    # Calculate a similarity score based on the number of good matches
    num_matches = len(good_matches)
    denom_matches = min(len(kp1), len(kp2))


    if denom_matches == 0:
        return False

    similarity = num_matches / denom_matches
    # Return a Boolean value indicating whether the two images are similar
    return similarity >= threshold 

# using orb
def orb(frame_a, frame_b, treshold = 0.5):
    # Convert the images to grayscale
    frame_a = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)

    # Create an ORB object
    orb = cv2.ORB_create()

    # Detect keypoints and compute descriptors for both images
    kp1, des1 = orb.detectAndCompute(frame_a, None)
    kp2, des2 = orb.detectAndCompute(frame_b, None)

    # Create a BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors between the two images
    matches = bf.match(des1, des2)

    # Sort the matches by distance
    matches = sorted(matches, key=lambda x:x.distance)

    # Calculate a similarity score based on the number of good matches

    num_matches = len(matches)
    denom_matches = min(len(kp1), len(kp2))


    if denom_matches == 0:
        return False

    similarity = num_matches / denom_matches

    # Return a Boolean value indicating whether the two images are similar
    return similarity >= treshold

# akaze algorithm
def akaze(frame_a, frame_b, threshold = 0.5):

    # Initialize the AKAZE detector and descriptor
    akaze = cv2.AKAZE_create()

    # Detect keypoints and compute descriptors for both images
    kp1, des1 = akaze.detectAndCompute(frame_a, None)
    kp2, des2 = akaze.detectAndCompute(frame_b, None)

    # Match the descriptors using a Brute-Force matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Calculate the distance threshold for the matches
    max_distance = 0
    for match in matches:
        distance = match.distance
        if distance > max_distance:
            max_distance = distance

    distance_threshold = threshold * max_distance

    # Count the number of matches that pass the distance threshold
    num_good_matches = 0
    for match in matches:
        if match.distance < distance_threshold:
            num_good_matches += 1

    # Determine if the images are similar based on the number of good matches
    return num_good_matches >= 10



# Check if two frames match using template matching
def template_matching(frame_a, frame_b, threshold = 0.8 ):
    height, width = frame_b.shape[:2]
    frame_a = cv2.resize(frame_a, (width, height))


    result = cv2.matchTemplate(frame_a, frame_b, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    if max_val > threshold:
        return True
    else:
        return False

# Check if two frames match using xor
def xor_matching(frame_a, frame_b, threshold = 0.8):
    equal_shape = frame_a.shape == frame_b.shape 
    if equal_shape and not np.bitwise_xor(frame_a, frame_b).any():
        return True

    return False

