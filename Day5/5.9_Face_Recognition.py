"""Face Recognition using a Pre-trained Model (CO5)

Face detection using OpenCV Haar cascade.
"""

import cv2
import numpy as np
import os

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

img_path = "face.jpg"
if os.path.exists(img_path):
    img = cv2.imread(img_path)
else:
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    cv2.putText(img, "No face.jpg found", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(f"Detected {len(faces)} face(s)")
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imwrite("faces_detected.png", img)
print("Output saved to faces_detected.png")
