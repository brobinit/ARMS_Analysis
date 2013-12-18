import sys
import cv2
import numpy


#Supposedly fixes issue with being unable to close windows during active session
cv2.startWindowThread() 

#establishes the threshold to be used
tlow=100
thigh=0

if len(sys.argv) > 1:
    tlow = int(sys.argv[1])

if len(sys.argv) > 2:
    thigh=int(sys.argv[2])
else:
    thigh=tlow * 3


print "The low threshold is ", tlow, " and the high threshold is ", thigh


#importing the image to be used and giving it name im
imfile = '/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/Simple_Test/mm1.jpg'
im=cv2.imread(imfile)

#resize the image and make it grayscale
imsmall = cv2.resize(im, (640, 800))
gray=cv2.cvtColor(imsmall, cv2.COLOR_BGR2GRAY)


#Find the contours of the image using canny
canny=cv2.Canny(gray, tlow, thigh)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cannyc=cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

#Draws the contours using a randomly generated color
for i in range(len(contours)):
    c1=numpy.random.randint(255)
    c2=numpy.random.randint(255)
    c3=numpy.random.randint(255)
    cv2.drawContours(cannyc, contours, i, (c1,c2,c3), 1)


#Converts image from grayscale to color
#cannybgr=cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

#Shows both images in the same window
both = numpy.hstack([canny, cannyc])


cv2.imshow('regions', both)
print "Press any key ...."

#fixes infinite loading problem, but have to crash the terminal to get out of the image and add new code. Need to find better solution.
k = cv2.waitKey(0)
cv2.destroyAllWindows()
