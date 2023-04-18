from engine.clock import Timer
from engine.components import FilledImageComponent
from engine.components import GlowComponent
from engine.events import EVENT_GLOW_EFFECT
from engine.events.event_handlers import EventHandler


class GlowEventHandler(EventHandler):
    @property
    def event_types(self) -> list[int]:
        return [EVENT_GLOW_EFFECT]

    def handles(self, event):
        return event.type in self.event_types

    def handle_event(self, event):
        image_component = event.entity.get_component(FilledImageComponent)
        glow_component = GlowComponent(image_component.image.get_size(), image_component.color)

        # ThisProgrammerG components stored in dictionary can only have 1 at a time. May have to use lists
        event.entity.add_component(glow_component)
        Timer(lambda: event.entity.remove_component(GlowComponent), 0.15)
