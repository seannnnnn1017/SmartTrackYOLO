import datetime

class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def update(self):
        self._numFrames += 1

    def elapsed(self):
        if self._end is None:
            return (datetime.datetime.now() - self._start).total_seconds()
        return (self._end - self._start).total_seconds()

    def fps(self):
        elapsed_time = self.elapsed()
        if elapsed_time == 0:
            return 1  # 或者可以选擇返回 0 或其他适当值
        return int(self._numFrames / elapsed_time)
