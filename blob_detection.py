import cv2
import numpy as np

# Read in an image in grayscale
img = cv2.imread('updated_300.png', cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()

# Detects the blobs in the image
keypoints = detector.detect(img)

# Draw detected keypoints as red circles
imgKeyPoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display found keypoints
cv2.imshow("Keypoints", imgKeyPoints)
cv2.waitKey(0)

cv2.destroyAllWindows()

