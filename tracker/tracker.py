from FPS import FPS
from FPS import ScreenCaptureStream
import cv2
from ultralytics import YOLO
import threading



class YOLOTracker:
    def __init__(self, model):
        self.model = model
        self.latest_frame = None
        self.latest_results = None
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.detect_and_track, daemon=True)
    
    def start(self):
        self.thread.start()
    
    def update_frame(self, frame):
        with self.lock:
            self.latest_frame = frame.copy()
    
    def get_results(self):
        with self.lock:
            return self.latest_results
    
    def detect_and_track(self):
        while True:
            if self.latest_frame is not None:
                with self.lock:
                    frame = self.latest_frame.copy()
                results = self.model.track(frame, conf=0.6, save=False)
                with self.lock:
                    self.latest_results = results

