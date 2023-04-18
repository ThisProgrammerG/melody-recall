from typing import Sequence

import pygame

from engine.components import KeyboardComponent
from engine.events.event_handlers import EventHandler


def has_keypress_component(obj):
    return obj.get_component(KeyboardComponent)

class KeyboardEventHandler(EventHandler):
    def __init__(self, objects: Sequence):
        super().__init__()
        self.objects = []
        self.keys_handled = set()

        self.add_objects(objects)

    def add_objects(self, objects):
        for obj in objects:
            if not has_keypress_component(obj):
                continue
            self.objects.append(obj)

        self.set_handled_keys()

    def set_handled_keys(self):
        self.keys_handled = set(
                key
                for obj in self.objects
                for key in obj.get_component(KeyboardComponent).handled_keys
        )

    @property
    def event_types(self) -> list[int]:
        return [pygame.KEYDOWN, pygame.KEYUP]

    def handles(self, event):
        return event.type in self.event_types and event.key in self.keys_handled

    def handle_event(self, event):
        for obj in self.objects:
            component = obj.get_component(KeyboardComponent)
            handled_keys = component.handled_keys

            if not component.enabled or event.key not in handled_keys:
                continue

            if event.type == pygame.KEYDOWN:
                component.action()
            elif event.type == pygame.KEYUP:
                pass
