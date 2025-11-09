import cv2
import numpy as np

class MotionDetector:
    def __init__(self, min_area=500):
        self.prev_gray = None
        self.min_area = min_area

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return []

        diff = cv2.absdiff(self.prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_regions = []
        for c in contours:
            if cv2.contourArea(c) < self.min_area:
                continue
            x,y,w,h = cv2.boundingRect(c)
            motion_regions.append((x,y,w,h, cv2.contourArea(c)))

        self.prev_gray = gray
        return motion_regions

