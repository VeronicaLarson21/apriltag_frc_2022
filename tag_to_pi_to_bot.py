from cscore import CameraServer
from pupil_apriltags import Detector
import cv2
import time
from networktables import NetworkTables
# setup and the main loop
detector = Detector(families='tag36h11')
cam = CameraServer.getVideo()
Networktables.intialize('10.41.22.2')
time.sleep(0.5)
looping = True
while looping:
    image = cam.read()
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# look for tags
    detections = detector.detect(grayimg)
    #make this better than jamming my screen with nothings, gonna put nothing in there maybe that will work? nah i want a way to tell no matter how annoying
    if not detections:
        pass
    else:
        #loops over detections lets me get at the other results beyond pure number of detections
        for r in detections:
            (ptA, ptB, ptC, ptD) = r.corners
            print(r.corners)
            #print(r.center)
            #set the values we need here(including pose if i get to that, then send those vals over network tables)
        #looping = False


#breaks the window and ends the program
cv2.destroyAllWindows()

