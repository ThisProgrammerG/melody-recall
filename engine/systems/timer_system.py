from engine.clock import Timer


class TimerSystem:
    def __init__(self):
        pass
        # self.timers = deque()

    def expired_timers(self):
        for timer in Timer.timers.copy():
            if timer.loops == 0:
                yield timer

    def update(self):
        for timer in Timer.timers.copy():
            timer.update()

        for timer in self.expired_timers():
            Timer.timers.remove(timer)
