import torch

model = torch.hub.load("ultralytics/yolov5", "custom", path="weights/last.pt", force_reload=True)
