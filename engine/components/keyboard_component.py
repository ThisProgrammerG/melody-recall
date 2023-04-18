from engine.components import Component
from engine.components.mixins import ToggleMixin


class KeyboardComponent(Component, ToggleMixin):
    def __init__(self, handled_keys, callback: callable):
        Component.__init__(self)
        ToggleMixin.__init__(self)
        self.handled_keys = handled_keys
        self.callback = callback

    def action(self):
        self.callback()
