import pygame

from engine.components import Component
from engine.components.mixins import VisibilityMixin


class GlowComponent(Component, VisibilityMixin):
    _cache = {}

    def __init__(self, size, color='grey', blend_mode=pygame.BLEND_ADD):
        Component.__init__(self)
        VisibilityMixin.__init__(self)
        self._set_image(size, color)
        self.blend_mode = blend_mode

    def _set_image(self, size, color):
        color = pygame.Color(color)[:4]
        if (size, color) in self._cache:
            self.image = self._cache[(size, color)]
        else:
            self.image = pygame.Surface(size, pygame.SRCALPHA)
            self.image.fill(color)
            self._cache[(size, color)] = self.image
