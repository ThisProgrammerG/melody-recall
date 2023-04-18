import pygame

from engine import settings
from engine.components import ClickComponent
from engine.components import KeyboardComponent
from engine.components import RectComponent
from engine.components import TextComponent
from engine.events.event_handlers import GlowEventHandler
from engine.events.event_handlers import KeyboardEventHandler
from engine.events.event_handlers import NoteEventHandler
from engine.music_grid.music_grid import MusicGrid
from engine.scenes import Scene
from engine.states import GameState
from engine.entity import Entity


class GameScene(Scene):
    def __init__(self, event_system, render_system):
        super().__init__(event_system, render_system)
        self.music_grid = MusicGrid()
        self.played_notes = []
        self.display_notes = []
        self.game_state = GameState.LISTENING
        self.press_continue = Entity(
                TextComponent('Round ended. [Continue?]', 'grey'),
                RectComponent(
                        (
                                settings.window_rect.centerx,
                                self.music_grid.grid[-1].get_component(RectComponent).rect.bottom + 50
                        )
                ),
                KeyboardComponent([pygame.K_RETURN, pygame.K_KP_ENTER], self.switch_to_listening),
                ClickComponent([pygame.BUTTON_LEFT], self.switch_to_listening),
        )
        self.objects.extend(self.music_grid.grid + [self.press_continue])
        self.handlers.append(GlowEventHandler())
        self.handlers.append(NoteEventHandler(self))
        self.handlers.append(KeyboardEventHandler(self.objects))

        self.switch_to_listening()

    def switch_state_to(self, state):
        self.game_state = state

    def switch_to_listening(self):
        self.switch_state_to(GameState.LISTENING)
        self.press_continue.get_component(KeyboardComponent).disable()
        self.press_continue.get_component(ClickComponent).disable()
        self.press_continue.get_component(TextComponent).hide()
        self.objects = [obj for obj in self.objects if obj not in self.display_notes]
        self.played_notes.clear()
        self.display_notes.clear()
        self.music_grid.disable()
        self.music_grid.pick_note()
        self.music_grid.play_notes()

    def switch_to_playing(self):
        self.switch_state_to(GameState.PLAYING)
        self.music_grid.enable()

    def switch_to_interim(self):
        self.switch_state_to(GameState.INTERIM)
        self.press_continue.get_component(KeyboardComponent).enable()
        self.press_continue.get_component(ClickComponent).enable()
        self.press_continue.get_component(TextComponent).show()
        self.display_notes = self.music_grid.copy_queued_notes()
        self.objects.extend(self.display_notes)
        self.music_grid.clear_queued_notes()
        self.music_grid.disable()

    def update(self):
        super().update()
        if self.game_state == GameState.PLAYING:
            correct_order = self.music_grid.check_valid(self.played_notes)
            if not correct_order:
                self.switch_to_interim()
            elif len(self.played_notes) >= len(self.music_grid.queued_notes):
                self.switch_to_listening()
        elif self.game_state == GameState.LISTENING and self.music_grid.finished_playing:
            self.switch_to_playing()
