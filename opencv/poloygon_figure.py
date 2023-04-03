import cv2
import numpy as np

#making a empty canvas
canvas = np.zeros((300,300,3))

#required point we nee to join
pts = np.array([[250,5],[220,80],[280,80]])

# reshape(no._row in above if write -1, row_per_matrix, col_per_matrix ) simple tells make three matrix of 1x2

pts = pts.reshape((-1, 1, 2))

#Drawing the polygon
# Boolean True and False determine if the figure is closed or not
cv2.polylines(canvas, [pts], True, (0,255,0), 3)

cv2.imshow('sample', canvas)
cv2.waitKey(0)