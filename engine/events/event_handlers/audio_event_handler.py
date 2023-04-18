import pygame

from engine.cache import AudioCache
from engine.events import EVENT_PLAY_AUDIO
from engine.events.event_handlers import EventHandler


class AudioEventHandler(EventHandler):
    def __init__(self):
        self.audio_cache = AudioCache()
        pygame.mixer.set_num_channels(50)

    @property
    def event_types(self) -> list[int]:
        return [EVENT_PLAY_AUDIO]

    def handles(self, event):
        return event.type == EVENT_PLAY_AUDIO

    def play_sound(self, audio_name, volume, loops):
        sound = self.audio_cache.get_sound(audio_name)
        sound.set_volume(volume)
        channel = pygame.mixer.find_channel()
        channel.play(sound, loops=loops)

    def handle_event(self, event):
        self.play_sound(event.audio_name, event.volume, event.loops)
