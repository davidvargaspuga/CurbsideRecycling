import cv2
import numpy as np

# Read image
frame = cv2.imread("updated_300.png")

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define range of green color in HSV
lower_green = np.array([30, 100, 20], np.uint8)
upper_green = np.array([70, 255, 255], np.uint8)

# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask)

# Resize windows then show updated image
frame_resize = cv2.resize(frame, (450, 800))
cv2.imshow('frame', frame_resize)
mask_resize = cv2.resize(mask, (450, 800))
cv2.imshow('mask', mask_resize)
res_resize = cv2.resize(res, (450, 800))
cv2.imshow('res', res_resize)
cv2.imwrite('res_300.png', res)
cv2.waitKey(0)
cv2.destroyAllWindows()