from enum import Enum
from enum import auto


class GameState(Enum):
    PLAYING = auto()
    LISTENING = auto()
    INTERIM = auto()
    PAUSED = auto()
