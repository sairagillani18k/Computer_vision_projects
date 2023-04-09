import cv2
import numpy as np

image = cv2.imread("img2.png")

matrix = np.float32([[1,0,100],[0,1,100]])
#Apply translation cv2.wrapAffine(src,m,dsize)
translated = cv2.warpAffine(image,matrix,(image.shape[0]+100,image.shape[1]+100))

cv2.imshow("translated",translated)
cv2.waitKey(0)