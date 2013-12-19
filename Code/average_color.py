import cv2
import numpy


#importing the image and name it 'im'
imfile = '/Users/blairerobinson/Documents/SDSU_Undergrad/Edwards_Lab/ARMS/ARMS_Images/Simple_Test/mm1.jpg'
im = cv2.imread(imfile)

#resize image and make it grayscale
imsmall = cv2.resize(im, (640, 800))
gray = cv2.cvtColor(imsmall, cv2.COLOR_BGR2GRAY)




#Shows both images in the same window
both = numpy.hstack([IMGAGE 1, IMAGE 2])

cv2.imshow('regions', both)
print "Press any key ...."

k = cv2.waitKey(0)
