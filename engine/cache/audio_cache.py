import pygame

from assets import get_path


def load(audio_type, audio_name):
    path = get_path(**{audio_type: audio_name})
    audio = pygame.mixer.Sound(path)
    return audio

class AudioCache:
    def __init__(self):
        self.cache = {}

    def get_sound(self, sound_name):
        if self.cache.get(sound_name):
            return self.cache[sound_name]

        audio = load('sounds', sound_name)
        self.cache[sound_name] = audio
        return audio
