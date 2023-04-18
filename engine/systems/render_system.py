from collections import deque

import pygame

from engine import settings
from engine.components import FilledImageComponent
from engine.components import GlowComponent
from engine.components import ImageComponent
from engine.components import PositionComponent
from engine.components import RectComponent
from engine.components import TextComponent
from engine.entity import Entity


def get_image_component(obj):
    return (
            obj.get_component(ImageComponent)
            or obj.get_component(TextComponent)
            or obj.get_component(FilledImageComponent)
    )

def get_placement_component(obj):
    return (
            obj.get_component(RectComponent)
            or obj.get_component(PositionComponent)
    )

def get_placement_value(obj):
    return (
            getattr(get_placement_component(obj), 'rect', None)
            or getattr(get_placement_component(obj), 'position', None)
    )

def is_renderable(obj):
    has_image = get_image_component(obj)
    has_placement = get_placement_component(obj)
    if has_image and has_placement:
        return True

class RenderSystem:
    def __init__(self):
        self.display = Entity(
                ImageComponent(pygame.display.get_surface()),
        )
        self.screen = Entity(
                ImageComponent(pygame.display.get_surface().copy()),
                RectComponent(position=settings.window_rect.center),
        )
        self.display_surface = get_image_component(self.display).image
        self.screen_surface = get_image_component(self.screen).image
        self.render_last = deque()

    def _get_renderable(self, objects):
        for obj in objects:
            if is_renderable(obj):
                yield obj

        while self.render_last:
            obj = self.render_last.popleft()
            if is_renderable(obj):
                yield obj

    def render_renderables(self, objects):
        for obj in self._get_renderable(objects):
            image_component = get_image_component(obj)
            glow_component = obj.get_component(GlowComponent)
            image = image_component.image
            blend_mode = image_component.blend_mode

            if not image_component.visible:
                continue

            if glow_component:
                image = image.copy()
                image.blit(glow_component.image, (0, 0), special_flags=glow_component.blend_mode)

            self.render_onto(
                    self.screen_surface,
                    image,
                    get_placement_value(obj),
                    blend_mode,
            )

    def render_onto(self, surface, image, placement: pygame.Vector2 | pygame.Rect, blend_mode=0):
        surface.blit(image, placement, special_flags=blend_mode)

    def update(self, objects):
        self.display_surface.fill('black')
        self.screen_surface.fill('black')

        self.render_renderables(objects)
        self.render_onto(
                self.display_surface,
                self.screen_surface,
                get_placement_value(self.screen),
                # pygame.BLEND_ADD
        )

        pygame.display.flip()
