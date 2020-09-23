import numpy as np
import cv2 as cv
print(cv.__version__)

# load original and gray img
imgoriginal = cv.imread('simon.png')
imggrey = cv.imread('simon.png',0) # 0 - gray, 1 - original, -1 - including alpha channel

# show img with adjustable window
cv.namedWindow('imagegrey',cv.WINDOW_NORMAL) # can adjust window size
cv.imshow('imagegrey',imggrey) # (windown name, object read)

cv.namedWindow('imageoriginal',cv.WINDOW_NORMAL) # can adjust window size
cv.imshow('imageoriginal',imgoriginal) # (windown name, object read)
cv.waitKey(0) # only parameter is just how long should it wait for a user input. Zero means to wait forever until keyboard event.
cv.destroyAllWindows() # if a sepcified window need to be close, use cv.destroyWindow()