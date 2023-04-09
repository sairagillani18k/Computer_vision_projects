import numpy as np 
import cv2

#reading image
# img = cv2.imread("download.jpeg")
img = cv2.imread("noise.jpg")

# boxfilter and blur function
img_blur = cv2.blur(img, (5,5))
img_box = cv2.boxFilter(img, -1, (3,3), normalize = False)

# weight is value that is mulitplied with pixel values
#gaussian blur
img_gaussian = cv2.GaussianBlur(img, (5,5), 0) # 0 is standerdeviation about x axis

# median Blur (used for noise reduction)
img_median = cv2.medianBlur(img, 5)

# Bilateral filtering (Reduction of noise + preserving of edges)
# Bilateral function makes sure that only those pixels 
# having intensity almost same as target pixel are considered
img_bilateral = cv2.bilateralFilter(img, 5, 6, 6)

#Write the image
cv2.imwrite("blur.jpg", img_gaussian)
cv2.imwrite("denoise.jpg", img_median)

#show the image
cv2.imshow("img", img)
cv2.imshow("img blur", img_blur)
cv2.imshow("img box", img_box)
cv2.imshow("img gaussian", img_gaussian)
cv2.imshow("img median", img_median)
cv2.imshow("img bilateral", img_bilateral)
cv2.waitKey(0)