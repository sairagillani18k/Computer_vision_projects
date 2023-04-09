import cv2
import numpy as np 

#Reaading the image
image = cv2.imread("img2.png")

height, width = image.shape[:2]

# Rotation matrix: cv2.getRotationMatrix2D(center, angle, scale)
matrix = cv2.getRotationMatrix2D((width//2,height//2), 10, .5)

#Applying the matrix
rotated = cv2.warpAffine(image, matrix, (width,height))

#show the image
cv2.imshow("rotated",rotated)
cv2.waitKey(0)