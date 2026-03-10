from ultralytics import YOLO

class PersonDetector:
    def __init__(self):
        # Lightweight model (fast, good for CCTV)
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame, conf=0.4, classes=[0])  # class 0 = person
        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                detections.append((x1, y1, x2, y2, confidence))

        return detections
