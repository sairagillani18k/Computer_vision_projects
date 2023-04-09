import cv2
import numpy as np 

#Reading the image 
img = cv2.imread("download.jpeg")

# Gaussian blur
gaussian_blur = cv2.GaussianBlur(img, (7,7), 2)

#Sharpning the image using addweighted function
sharpned1 = cv2.addWeighted(img, 1.5, gaussian_blur, -.5, 0)
sharpned2 = cv2.addWeighted(img, 5.5, gaussian_blur, -4.5, 0)
sharpned3 = cv2.addWeighted(img, 11.0, gaussian_blur,-10.0, 0)

#write the image
cv2.imwrite("sharpned.jpg", sharpned2)

cv2.imshow("img", img)
cv2.imshow("sharpned1", sharpned1)
cv2.imshow("sharpned2", sharpned2)
cv2.imshow("sharpned3", sharpned3)
cv2.waitKey(0)