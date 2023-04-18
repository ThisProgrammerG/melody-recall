from engine.components import Component
from engine.components.mixins import VisibilityMixin
from engine.settings import font


class TextComponent(Component, VisibilityMixin):
    def __init__(self, text, color='white', blend_mode=0):
        Component.__init__(self)
        VisibilityMixin.__init__(self)
        self.image = font.render(text, True, color)
        self.blend_mode = blend_mode
