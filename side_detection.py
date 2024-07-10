import cv2
import numpy as np

image = cv2.imread(r"")
image = cv2.blur(image,(5,5))
thresholded_image = cv2.inRange(image, (110,110,110), (125,125,125))
thresholded_image = 255 - thresholded_image
edges = cv2.Canny(thresholded_image, 10, 200)
edge_points = np.transpose(np.nonzero(edges))
for point in edge_points:
    x, y = point
    print(f"Координаты точки: ({x}, {y})")
cv2.imshow('Thresholded Image', edges)
cv2.imshow('Thresholded2 Image', thresholded_image)
cv2.waitKey(0)