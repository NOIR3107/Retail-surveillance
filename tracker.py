import math

class SimpleTracker:
    def __init__(self, max_distance=50):
        self.next_id = 1
        self.objects = {}
        self.max_distance = max_distance

    def _center(self, box):
        x1, y1, x2, y2 = box
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def update(self, detections):
        tracked_objects = []

        for det in detections:
            x1, y1, x2, y2, conf = det
            cx, cy = self._center((x1, y1, x2, y2))

            assigned_id = None
            min_dist = float("inf")

            for obj_id, (px, py) in self.objects.items():
                dist = math.hypot(cx - px, cy - py)
                if dist < min_dist and dist < self.max_distance:
                    min_dist = dist
                    assigned_id = obj_id

            if assigned_id is None:
                assigned_id = self.next_id
                self.next_id += 1

            self.objects[assigned_id] = (cx, cy)
            tracked_objects.append((x1, y1, x2, y2, conf, assigned_id))

        return tracked_objects
