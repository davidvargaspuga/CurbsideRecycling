import os
import cv2

# Read the video from the specified path
capture = cv2.VideoCapture("IMG_4212_Slomo.mp4")

try:
    # Creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
# If not created, then raise error
except OSError:
    print ('Error: Creating directory')

# Frame
currentframe = 0

while True:
    # Reading from frame
    ret, frame = capture.read()
    if ret:
        # If video is still creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)

        # Writing the extracted images
        cv2.imwrite(name, frame)

        # Increasing counter to show amount created
        currentframe += 1
    else:
        break

capture.release()
cv2.destroyAllWindows()