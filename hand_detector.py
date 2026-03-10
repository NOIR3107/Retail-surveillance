import cv2
from mediapipe.python.solutions import hands as mp_hands

class HandDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def detect(self, frame):
        """
        Returns list of hand centers [(x, y), ...]
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        hand_centers = []

        if results.multi_hand_landmarks:
            h, w, _ = frame.shape
            for hand_landmarks in results.multi_hand_landmarks:
                xs = [int(lm.x * w) for lm in hand_landmarks.landmark]
                ys = [int(lm.y * h) for lm in hand_landmarks.landmark]
                hand_centers.append(
                    (sum(xs) // len(xs), sum(ys) // len(ys))
                )

        return hand_centers
