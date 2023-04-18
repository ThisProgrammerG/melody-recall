import pygame

from engine.components import ClickComponent
from engine.components import RectComponent
from engine.events.event_handlers import EventHandler


def valid_clickable(obj):
    return obj.get_component(ClickComponent) and obj.get_component(RectComponent)

class ClickEventHandler(EventHandler):
    def __init__(self, objects):
        self.objects = []
        self.handled_buttons = set()

        self.add_objects(objects)

    def add_objects(self, objects):
        for obj in objects:
            if not valid_clickable(obj):
                continue
            self.objects.append(obj)

        self.set_handled_buttons()

    def set_handled_buttons(self):
        self.handled_buttons = set(
                button
                for obj in self.objects
                for button in obj.get_component(ClickComponent).buttons
        )

    @property
    def event_types(self) -> list[int]:
        return [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]

    def handles(self, event):
        return event.type in self.event_types

    def handle_event(self, event):
        for obj in self.objects:
            component = obj.get_component(ClickComponent)
            rect = obj.get_component(RectComponent).rect
            enabled = component.enabled

            if event.button not in component.buttons or not enabled:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    has_collided = rect.collidepoint(event.pos)

                    if not has_collided:
                        continue

                    component.click_initiated()

                    if not component.callback_on_click:
                        continue

                    component.callback_on_click()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    has_collided = rect.collidepoint(event.pos)
                    had_initiated_click = component.had_initiated_click

                    component.click_ended()

                    if (
                            not (has_collided and had_initiated_click)
                            or not component.callback_on_clicked
                    ):
                        continue

                    component.callback_on_clicked()
