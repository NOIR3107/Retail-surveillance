import cv2
from detector import PersonDetector
from tracker import SimpleTracker

video_path = "data/videos/sample.mp4"

cap = cv2.VideoCapture(video_path)
detector = PersonDetector()
tracker = SimpleTracker()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)
    tracked = tracker.update(detections)

    for x1, y1, x2, y2, conf, track_id in tracked:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(
            frame,
            f"ID {track_id}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2,
        )

    cv2.imshow("Person Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
