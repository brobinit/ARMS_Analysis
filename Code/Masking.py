import sys
import cv2
import numpy

#Supposedly fixes issue with being unable to close windows during active session
cv2.startWindowThread() 
#cvStartWindowThread()

#establishes the threshold to be used
tlow=100
thigh=300

if len(sys.argv) > 1:
    tlow = int(sys.argv[1])
    
if len(sys.argv) > 2:
    thigh=int(sys.argv[2])
else:
    thigh=tlow * 3
    
print "The low threshold is ", tlow, " and the high threshold is ", thigh

 
 #importing the image to be used and giving it name img
imfile = '/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/DSC_0265.JPG'
img = cv2.imread(imfile)

#resize the image
imsmall = cv2.resize(img, (640, 800))

#make the image grayscale
gray = cv2.cvtColor(imsmall, cv2.COLOR_BGR2GRAY)

#Find the contours of the image
canny = cv2.Canny(gray, tlow, thigh)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cannyc = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)



#draws one color on all the contours and names it cannyc
"""for i in range(len(contours)):
    c1 = 0
    c = 255
    c3 = 0
    cannyc = cv2.drawContours(cannyc, contours, i,(c1,c,c3), 1)
    c = c-1"""


#Draws the contours using a randomly generated color
for i in range(len(contours)):
    c1=numpy.random.randint(255)
    c2=numpy.random.randint(255)
    c3=numpy.random.randint(255)
    cv2.drawContours(cannyc, contours, i, (c1,c2,c3), 1)
    


#converts image from gray to color
cannybgr = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

#Shows both images in the same window
both = numpy.hstack([cannybgr, cannyc])



#Name the Window
cv2.namedWindow('DSC_0265', cv2.WINDOW_AUTOSIZE)


#Opens the image window
cv2.imshow('DSC_0265', both)



#Fixes infinite loading problem, but have to crash the terminal to get out of the image 
#and add new code. Need to find better solution.
print "Press 'esc' to exit image or press 'S' to save image and exit"
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('MaskingBoth.png', both)
	cv2.destroyAllWindows()

