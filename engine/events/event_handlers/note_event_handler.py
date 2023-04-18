import typing

from engine.events import EVENT_NOTE_PRESSED
from engine.events.event_handlers import EventHandler


if typing.TYPE_CHECKING:
    from engine.scenes import GameScene

class NoteEventHandler(EventHandler):
    def __init__(self, game_scene: 'GameScene'):
        self.game_scene = game_scene

    @property
    def event_types(self) -> list[int]:
        return [EVENT_NOTE_PRESSED]

    def handles(self, event):
        return event.type in self.event_types

    def handle_event(self, event):
        self.game_scene.played_notes.append(event.entity)
