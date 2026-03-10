import cv2
import numpy
from ultralytics import YOLO

print("OpenCV:", cv2.__version__)
print("NumPy:", numpy.__version__)

model = YOLO("yolov8n.pt")
print("YOLO model loaded successfully")
