import pygame

from engine.components import Component


class RectComponent(Component):
    def __init__(self, position=(0, 0), size=(0, 0), anchor='center'):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 0, 0)
        self._original_position = pygame.Vector2(position)  # Bug when setting position before size
        self.anchor = anchor

        self.update(self._original_position, size)
        # print('=====')
        # print(self.rect)

    def set_size(self, size):
        self.rect.width, self.rect.height = size
        self.set_position(self._original_position)

    def set_position(self, position: pygame.Vector2):
        setattr(self.rect, self.anchor, round(position))

    def update(self, position: pygame.Vector2, size):
        self.set_size(size)  # Size first before position due to bug
        self.set_position(position)
