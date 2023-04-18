import pygame

from .timer import Timer


delta_time = 0
_clock = pygame.Clock()

def tick():
    global delta_time
    delta_time = _clock.tick() / 1_000

def get_fps():
    global _clock
    return _clock.get_fps()
