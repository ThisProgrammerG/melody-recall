from collections import deque

from engine import clock


class Timer:
    timers = deque()

    def __init__(self, callback: callable = None, seconds=0, loops=1):
        self.callback = callback
        self.seconds = seconds
        self.time_remaining = self.seconds
        self.loops = loops

        self.timers.append(self)

    @property
    def ready(self):
        return self.time_remaining <= 0

    def reset(self):
        self.time_remaining = self.seconds

    def update(self):
        self.time_remaining -= clock.delta_time

        if not (self.callback and self.ready):
            return

        self.callback()
        self.loops -= 1

        if not self.loops > 1:
            return

        self.reset()
