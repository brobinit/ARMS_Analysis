"""
Blaire Robinson
Fall 2013

Various methods for image analysis developed over the semester.
Designed using a simpler image of M&Ms, but intended for more complex images of growth 
plates from Autonomous Reef Monitoring Systems.

"""


import numpy as np
import cv2
import sys


#Finds the contours of an image using Canny Edge detection. Determines the threshold high
#from the inputted low threshold.
def FindContours(image, low_thresh):
	im = cv2.imread(image)
	imsmall = cv2.resize(img, (640,800))
	imgray = cv2.cvtColor(imsmall,cv2.COLOR_BGR2GRAY)
	tlow = low_thresh
	thigh = tlow * 3
	canny = cv2.Canny(imgray, tlow, thigh)
	contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow("canny",canny)
	
	
def DrawContoursGradient(image, low_thresh):
	contours = FindContours(image, low_thresh)
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
    	cv2.imshow("cannyc",cannyc)
	
	
#Draws contours on the image using random generated colors
def DrawContoursRandom(contours):
	for i in range (len(contours)):
		c1=numpy.random.randint(255)
    	c2=numpy.random.randint(255)
    	c3=numpy.random.randint(255)
    	cv2.drawContours(cannyc, contours, i, (c1,c2,c3), 1)
    	cv2.imshow("cannyc",cannyc)


#Establishes the threshold to be used
def FindThreshold():
	tlow = 100
	thigh = 0
	if len(sys.argv) > 1:
		tlow = int(sys.argv[1])
	if len(sys.argv) > 2:
		thigh = int(sys.argv[2])
	else:
		thigh = tlow * 3
	print "The low threshold is ", tlow, " and the high threshold is ", thigh
	
def Skeletonization(image):
	im = cv2.imread(image)
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
	


