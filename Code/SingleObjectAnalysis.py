"""
Blaire Robinson
Edwards Lab
Fall 2013

This program Draws the contour of only one object in the image and prints the objects
average color, number boundary points for that object, area, perimeter, etc. 
"""

import numpy as np
import cv2

im = cv2.imread('/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/Simple_Test/shapes.jpg')

#When testing on ARMS image, will need to resize 
#im = cv2.resize(im, (640, 800))

#convert to gray
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#Sets image threshold
tlow = 40
thigh = tlow * 4


#canny edge detection
canny = cv2.Canny(imgray, tlow, thigh)

#find contours
ret,thresh = cv2.threshold(canny,tlow,thigh,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#converts image back to color
cannyc = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

#prints the number of objects in the image
num_objects = len(contours)
print "There are ", num_objects, " objects in this image."

#Draws the indicated contour, default is set at 0
num = 0
cnt = contours[0]
print "Object ", num," has ", len(cnt)," boundary points."
single_contour = cannyc
cv2.drawContours(single_contour, contours, 0,(255,0,0), 1)
print "You are now working with Object ", num," of the image. The image displayed highlights object ", num

#cv2.imshow("0",single_contour)

#Finds the area of the image
area = cv2.contourArea(cnt)
print "The area of Object ", num," is ", area," pixels."

#Calculates the perimeter of the image
perimeter = cv2.arcLength(cnt,True)
print "The perimeter (or arc length) of Object ", num," is ", perimeter," pixels."

#Approximates the contours to reduce the number of points to the major corners of the object
#Adjusted accuracy parameter to 10% of original arc length.
#approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
