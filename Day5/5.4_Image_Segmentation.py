"""Image Segmentation using Computer Vision (CO3)

Color-based segmentation using K-Means (OpenCV).
"""

import numpy as np
import cv2

img = np.zeros((200, 300, 3), dtype=np.uint8)
img[:, :100] = (255, 0, 0)
img[:, 100:200] = (0, 255, 0)
img[:, 200:] = (0, 0, 255)
noise = np.random.randint(0, 40, img.shape, dtype=np.uint8)
img = cv2.add(img, noise)

Z = img.reshape((-1, 3)).astype(np.float32)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
seg = centers[labels.flatten()].reshape(img.shape)
cv2.imwrite("segmented.png", seg)
print("Segmented image saved to segmented.png")
print("Cluster centers:\n", centers)
