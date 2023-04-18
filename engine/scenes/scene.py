from engine.events.event_handlers import AudioEventHandler
from engine.events.event_handlers import ClickEventHandler


class Scene:
    def __init__(self, event_system, render_system):
        self.event_system = event_system
        self.render_system = render_system
        self.objects = []

        self.click_handler = ClickEventHandler(self.objects)
        self.audio_handler = AudioEventHandler()

        self.handlers = [self.click_handler, self.audio_handler]

    def enter(self):
        self.click_handler.add_objects(self.objects)
        for handler in self.handlers:
            self.event_system.register_handler(handler)

    def exit(self):
        for handler in self.handlers:
            self.event_system.unregister_handler(handler)

    def update(self):
        pass
