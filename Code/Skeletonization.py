"""
Blaire Robinson
Fall 2013

Skeletonization. 

(Adapted from http://opencvpython.blogspot.com/2012/05/skeletonization-using-opencv-python.html)

This is a way of identifying how many different objects OpenCV identifies in the original 
image as a means of understanding the contours issue. Creates a small skeleton about a 
pixel wide in the center of each object of the image.
"""

import cv2
import numpy as np

#Simple image of M&Ms
#im = cv2.imread('/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/Simple_Test/mm1.jpg')

#image from ARMS database
im = cv2.imread('/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/DSC_0265.JPG')


#convert image to grayscale and resizes image 
imsmall = cv2.resize(im, (640, 800))
gray=cv2.cvtColor(imsmall, cv2.COLOR_BGR2GRAY)

size = np.size(gray)
skel = np.zeros(gray.shape,np.uint8)

ret,gray = cv2.threshold(gray,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False

while (not done):
	eroded = cv2.erode(gray,element)
	temp = cv2.dilate(eroded,element)
	temp = cv2.subtract(gray,temp)
	skel = cv2.bitwise_or(skel,temp)
	gray = eroded.copy()
	
	zeros = size - cv2.countNonZero(gray)
	if zeros==size:
		done = True
		
cv2.imshow("skel",skel)
cv2.waitKey(0)
cv2.destroeAllWindows()
