from typing import TYPE_CHECKING

from engine.events import EVENT_SWITCH_SCENE
from engine.events.event_handlers import EventHandler


if TYPE_CHECKING:
    from engine.systems.scene_system import SceneSystem

class SceneEventHandler(EventHandler):
    def __init__(self, scene_system: 'SceneSystem'):
        self.scene_system = scene_system

    @property
    def event_types(self) -> list[int]:
        return [EVENT_SWITCH_SCENE]

    def handles(self, event):
        return event.type == EVENT_SWITCH_SCENE

    def handle_event(self, event):
        self.scene_system.set_scene(event.scene_type)
