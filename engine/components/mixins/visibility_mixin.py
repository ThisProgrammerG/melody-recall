class VisibilityMixin:
    def __init__(self):
        self._visible = True

    @property
    def visible(self):
        return self._visible

    def show(self):
        self._visible = True

    def hide(self):
        self._visible = False
