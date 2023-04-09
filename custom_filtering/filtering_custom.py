# import required libraries
import numpy as np 
import cv2

# appling filter cv2.filter(src, ddepth, kernel, anchor, borkder_type)
# ddepth= no of bits in per pixel, anchor= where we place vaule after filtering

#import image
img = cv2.imread("download.jpeg")

# filters
#identity kernel
kernel_1 = np.array([[0,0,0],[0,1,0],[0,0,0]])

kernel_2 = np.ones((3,3), dtype=np.float32)/9

kernel_3 = np.ones((11,11), dtype=np.float32)/(11*11)

#applying the filters for bluering
img_kernel_1 = cv2.filter2D(img, -1, kernel_1)
img_kernel_2 = cv2.filter2D(img, -1, kernel_2)
img_kernel_3 = cv2.filter2D(img, -1, kernel_3)

#motion bulering in particuler direction (replace center row by one for horizontel)
kernel_blur = np.zeros((15,15))
kernel_blur[7 , :] = np.ones(15)
kernel_blur = kernel_blur/15
motion_kernel_blur = cv2.filter2D(img, -1, kernel_blur)




#Show the filtered image

cv2.imshow("img", img)
cv2.imshow("filterd kernel 1 img", img_kernel_1)
cv2.imshow("filterd kernel 2 img", img_kernel_2)
cv2.imshow("filterd kernel 3 img", img_kernel_3)
cv2.imshow("motion blure img",motion_kernel_blur)
cv2.waitKey(0)