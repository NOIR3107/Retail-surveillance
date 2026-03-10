import cv2
from detector import PersonDetector

video_path = "data/videos/sample.mp4"

cap = cv2.VideoCapture(video_path)
detector = PersonDetector()

if not cap.isOpened():
    print("Error opening video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)

    for x1, y1, x2, y2, conf in detections:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"Person {conf:.2f}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Person Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
