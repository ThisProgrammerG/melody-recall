import pygame

from engine.components import Component
from engine.components.mixins import VisibilityMixin


class FilledImageComponent(Component, VisibilityMixin):
    def __init__(self, size, color='grey', alpha=255, blend_mode=0):
        Component.__init__(self)
        VisibilityMixin.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(color)
        self.color = pygame.Color(color)
        self.color.a = alpha
        self.blend_mode = blend_mode
