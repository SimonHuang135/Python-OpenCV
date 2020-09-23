import numpy as np
import cv2 as cv

img = cv.imread('hey.png', 0) # read the image in grey
cv.imshow('image', img) # show img with window named image

k = cv.waitKey(0) & 0xFF # set wait for keyboard event forever (64 bit must & 0xFF)
if k == 27: # 27 in ASCII is Esc
    cv.destroyAllWindows()
elif k == ord('s'): # if keyboard event is 's'
    cv.imwrite('grey_hey.png', img)
    cv.destroyAllWindows()