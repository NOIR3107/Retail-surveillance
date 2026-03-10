import json
import csv
import time
import os

class EventLogger:
    def __init__(self, output_dir="output"):
        os.makedirs(output_dir, exist_ok=True)
        self.json_path = os.path.join(output_dir, "events.json")
        self.csv_path = os.path.join(output_dir, "events.csv")

        if not os.path.exists(self.csv_path):
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "track_id", "event", "x", "y"])

    def log(self, track_id, event, position):
        record = {
            "timestamp": time.time(),
            "track_id": track_id,
            "event": event,
            "x": position[0],
            "y": position[1],
        }

        # JSON
        data = []
        if os.path.exists(self.json_path):
            with open(self.json_path, "r") as f:
                try:
                    data = json.load(f)
                except:
                    pass
        data.append(record)
        with open(self.json_path, "w") as f:
            json.dump(data, f, indent=2)

        # CSV
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [record["timestamp"], track_id, event, position[0], position[1]]
            )
