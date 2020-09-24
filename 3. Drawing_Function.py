import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, pt1 = (0,0), pt2 = (511,511), color = (255,0,0), thickness = 5)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv.circle(img,(447,63), 63, (0,0,255), -1)

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

# cv.namedWindow('image',cv.WINDOW_NORMAL) # can adjust window size
cv.imshow('image',img) # (windown name, object read)
cv.waitKey(0) # only parameter is just how long should it wait for a user input. Zero means to wait forever until keyboard event.
cv.destroyAllWindows() # if a sepcified window need to be close, use cv.destroyWindow()
