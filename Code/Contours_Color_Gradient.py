"""
Blaire Robinson
Fall 2013

Contours 2
(Adapted from http://opencvpython.blogspot.com/2012/06/hi-this-article-is-tutorial-which-try.html)

An approach to finding the contours of the image that does not use Canny Image detection.

"""

import numpy as np
import cv2

im = cv2.imread('/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/Simple_Test/mm1.jpg')

#When testing on ARMS image, will need to resize 
#imsmall = cv2.resize(img, (640, 800))

#convert to gray
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
tlow = 50
thigh = tlow * 3


#canny edge detection
canny = cv2.Canny(imgray, tlow, thigh)

#find contours
ret,thresh = cv2.threshold(canny,tlow,thigh,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



cannyc = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
#draws a gradient of one color on all the contours and names it cannyc
c1 = 255
c2 = 0
c3 = 0
for i in range(len(contours)):
    c2 = c2 + 1
    if c2 >= 255:
    	c2 = 0
    else:
    	c2 = c2
    cv2.drawContours(cannyc, contours, i,(c1,c2,c3), 1)




"""
#display both images in same window
both = np.hstack([contours,cannyc])
cv2.imshow('contours2',both)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""


