from engine.components import Component
from engine.components.mixins import ToggleMixin


class ClickComponent(Component, ToggleMixin):
    def __init__(self, buttons: list[int], callback: callable, callback_on_clicked=True):
        Component.__init__(self)
        ToggleMixin.__init__(self)
        self.buttons = buttons
        self.callback = callback
        self.had_initiated_click = False
        self.callback_on_click = None
        self.callback_on_clicked = None

        setattr(self, ('callback_on_click', 'callback_on_clicked')[callback_on_clicked], callback)

    def click_initiated(self):
        self.had_initiated_click = True

    def click_ended(self):
        self.had_initiated_click = False
