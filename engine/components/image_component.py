import pygame

from engine.components import Component
from engine.components.mixins import VisibilityMixin


class ImageComponent(Component, VisibilityMixin):
    def __init__(self, image: pygame.Surface, blend_mode=0):
        Component.__init__(self)
        VisibilityMixin.__init__(self)
        self.image = image
        self.blend_mode = blend_mode
