import cv2
from apriltag import apriltag


# setup and the main loop
detector = apriltag("tag36h11")
cam = cv2.VideoCapture(0)

looping = True

while looping:
    result, image = cam.read()
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# look for tags
    detections = detector.detect(grayimg)
    if not detections:
        print("Nothing")
    else:
        print("Tag found!")
        looping = False
    cv2.imshow('Result', image)
	

# loop over; clean up and dump the last updated frame for convenience of debugging
cv2.destroyAllWindows()


# let the system event loop do its thing
     # key = cv2.waitKey(100)
	# terminate the loop if the 'Return' skey his hit
    # if key == 13:
        # looping = False
