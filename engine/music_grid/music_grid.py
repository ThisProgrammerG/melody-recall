import random
from collections import deque

import pygame

from engine import settings
from engine.clock import Timer
from engine.components import ClickComponent
from engine.components import GlowComponent
from engine.components import ImageComponent
from engine.components import KeyboardComponent
from engine.components import RectComponent
from engine.entity import Entity
from engine.music_grid import create_grid
from engine.music_grid import play_note
from engine.systems.render_system import get_image_component


class MusicGrid:
    def __init__(self):
        self.grid: list[Entity] = create_grid()
        self.queued_notes = deque()
        self.note_timers = []
        self.wrong_note_index = None

        self.delay = 0.5
        self._enabled = True

    @property
    def finished_playing(self):
        if all(timer.ready for timer in self.note_timers):
            self.note_timers.clear()
            return True
        return False

    def enable(self):
        for cell in self.grid:
            cell.get_component(ClickComponent).enable()
            cell.get_component(KeyboardComponent).enable()
        self._enabled = True

    def disable(self):
        for cell in self.grid:
            cell.get_component(ClickComponent).disable()
            cell.get_component(KeyboardComponent).disable()
        self._enabled = False

    def toggle(self):
        if self._enabled:
            self.disable()
        else:
            self.enable()

    def pick_note(self):
        entity = random.choice(self.grid)
        self.queued_notes.append(entity)

    def clear_queued_notes(self):
        self.wrong_note_index = None
        self.queued_notes.clear()

    def check_valid(self, played_notes):
        for i, (played_note, queued_note) in enumerate(zip(played_notes, self.queued_notes)):
            if played_note != queued_note:
                self.wrong_note_index = i
                return False
        return True

    def copy_queued_notes(self):
        # Refactor into class or dict.
        copied_notes = []
        width, height = get_image_component(self.grid[0]).image.get_size()
        quarter_width, quarter_height = width / 4, height / 4
        margin = 5
        spacing = 5
        max_width = settings.window_rect.width - (margin * 2)

        for i, note in enumerate(self.queued_notes):
            image: pygame.Surface = get_image_component(note).image
            quarter_image = pygame.transform.scale_by(image, 1 / 4)
            x = (i * (quarter_width + spacing) + quarter_width / 2 + margin)
            y = quarter_width / 2

            row = x // max_width
            y = y * row + row * (quarter_width / 2 + spacing) + y
            x = x % max_width

            note_copy = Entity(
                    ImageComponent(quarter_image),
                    RectComponent(position=(x, y), size=(quarter_width, quarter_height)),
                    GlowComponent((quarter_width, quarter_height), image.get_at((0, 0))),
            )
            if i >= self.wrong_note_index:
                note_copy.remove_component(GlowComponent)
            copied_notes.append(note_copy)
        return copied_notes

    def play_notes(self):
        self.note_timers = []
        for i, entity in enumerate(self.queued_notes):
            self.note_timers.append(Timer(lambda obj=entity: play_note(obj), (i + 1) * self.delay))
