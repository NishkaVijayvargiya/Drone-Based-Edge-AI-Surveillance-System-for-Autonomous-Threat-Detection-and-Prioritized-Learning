# Simple heuristic: larger area => likely vehicle => higher base priority
# faster pixel displacement => priority boost

def compute_centroid(box):
    x,y,w,h = box
    return (x + w/2, y + h/2)

class PriorityEngine:
    def __init__(self, area_vehicle_threshold=4000):
        self.area_vehicle_threshold = area_vehicle_threshold
        self.prev_centroids = {}  # id -> (x,y)

    def estimate_speed(self, id, centroid):
        prev = self.prev_centroids.get(id)
        if prev is None:
            self.prev_centroids[id] = centroid
            return 0.0
        dx = centroid[0] - prev[0]
        dy = centroid[1] - prev[1]
        speed = (dx*dx + dy*dy)**0.5
        self.prev_centroids[id] = centroid
        return speed

    def assign_priority(self, area, speed):
        # base by area
        if area >= self.area_vehicle_threshold:
            base = 3   # vehicle-like
        else:
            base = 2   # person-like / small object
        # speed boost
        if speed > 15:
            base += 2
        elif speed > 7:
            base += 1
        return min(base, 5)  # scale 0-5
