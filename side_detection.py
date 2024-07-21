import cv2
import numpy as np
import os

image_name = '_20240721_184957_fix.png'
current_folder = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_folder, 'image' , image_name)
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#image = cv2.blur(image,(5,5))
thresholded_image = cv2.inRange(image, 110, 125)
thresholded_image = 255 - thresholded_image
cv2.imwrite("thr.png", thresholded_image)
edges = cv2.Canny(thresholded_image, 10, 200)
edge_points = np.transpose(np.nonzero(edges))

cv2.imshow('Thresholded Image', edges)
cv2.imshow('Thresholded2 Image', thresholded_image)
cv2.waitKey(0)