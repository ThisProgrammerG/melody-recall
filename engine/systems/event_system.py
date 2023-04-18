import pygame

from engine.events.event_handlers import EventDispatcher


class EventSystem:
    def __init__(self):
        self.events = []
        self.event_dispatcher = EventDispatcher()

        self.running = True

    def register_handler(self, handler):
        self.event_dispatcher.register_handler(handler)

    def unregister_handler(self, handler):
        self.event_dispatcher.unregister_handler(handler)

    def update(self):
        if pygame.event.peek(pygame.QUIT):
            self.running = False
        self.event_dispatcher.add_events(pygame.event.get())
        self.event_dispatcher.dispatch_events()
