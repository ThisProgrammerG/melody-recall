from assets import paths
from engine.components import Component
from engine.events import post_audio_event


class SoundComponent(Component):
    def __init__(self, sound_name):
        super().__init__()
        self.sound_name = sound_name

    def play(self):
        post_audio_event(getattr(paths, f'{self.sound_name}'))
