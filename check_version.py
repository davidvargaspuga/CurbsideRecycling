import cv2

image = cv2.imread("updated_300.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# draw the contours on the image
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)