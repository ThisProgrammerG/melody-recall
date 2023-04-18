class ToggleMixin:
    def __init__(self):
        self._enabled = True

    @property
    def enabled(self):
        return self._enabled

    def toggle(self):
        self._enabled = not self._enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False
