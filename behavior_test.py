import cv2
import time
from detector import PersonDetector
from tracker import SimpleTracker
from behavior import BehaviorAnalyzer
from event_logger import EventLogger
from zones import ZONES

video_path = "data/videos/sample.mp4"

cap = cv2.VideoCapture(video_path)

detector = PersonDetector()
tracker = SimpleTracker()
behavior = BehaviorAnalyzer()
logger = EventLogger()

frame_count = 0
fps_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ---------- FPS OPTIMIZATION ----------
    frame = cv2.resize(frame, (640, 480))
    frame_count += 1

    detections = detector.detect(frame)
    tracked = tracker.update(detections)

    # Run heavy logic every 2 frames
    alerts = []
    if frame_count % 2 == 0:
        alerts = behavior.analyze(tracked)

    # ---------- Draw zones ----------
    for name, z in ZONES.items():
        cv2.rectangle(frame, (z[0], z[1]), (z[2], z[3]), (0, 255, 255), 2)
        cv2.putText(frame, name, (z[0] + 5, z[1] + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # ---------- Draw people ----------
    for x1, y1, x2, y2, conf, tid in tracked:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
        cv2.putText(frame, f"ID {tid}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)

    # ---------- Alerts + logging ----------
    y = frame.shape[0] - 20
    for tid, msg in alerts:
        logger.log(tid, msg, (0, 0))
        cv2.rectangle(frame, (10, y - 25), (450, y), (0, 0, 255), -1)
        cv2.putText(frame, f"ID {tid}: {msg}",
                    (15, y - 7),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        y -= 30

    # ---------- FPS counter ----------
    fps = frame_count / (time.time() - fps_time)
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Retail Theft Detection – Advanced", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
