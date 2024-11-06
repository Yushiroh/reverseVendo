import torch

# Model
model = torch.hub.load("ultralytics/yolov8", "custom", path="petbottlesv8_v1.pt", device='cpu', force_reload=True)

# Image
im = "IMG_8112.JPG"

# Inference
results = model(im)

results.pandas().xyxy[0]
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie