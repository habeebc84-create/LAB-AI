"""Object Detection using a Pre-trained Model (CO3)

Object detection with pre-trained Faster R-CNN.
"""

import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights
from torchvision.transforms import functional as F
from PIL import Image
import numpy as np

arr = np.random.randint(0, 255, (300, 400, 3), dtype=np.uint8)
arr[80:220, 120:280] = 255
img = Image.fromarray(arr)

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn(weights=weights)
model.eval()

tensor = F.to_tensor(img)
with torch.no_grad():
    outputs = model([tensor])

boxes = outputs[0]["boxes"]
labels = outputs[0]["labels"]
scores = outputs[0]["scores"]
print(f"Detected {len(boxes)} objects")
for b, l, s in zip(boxes, labels, scores):
    if s > 0.5:
        print(f"  label={l.item()} score={s:.3f} box={b.tolist()}")
