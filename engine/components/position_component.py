import pygame

from engine.components import Component


class PositionComponent(Component):
    def __init__(self, position):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.center_position = None

    def set_center_position(self, size):
        width, height = size
        self.center_position = (
                self.position.x - width / 2,
                self.position.y - height / 2
        )
