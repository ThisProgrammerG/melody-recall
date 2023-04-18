import pygame

from engine import settings
from engine.components import ClickComponent
from engine.components import FilledImageComponent
from engine.components import KeyboardComponent
from engine.components import PositionComponent
from engine.components import RectComponent
from engine.components import SoundComponent
from engine.entity import Entity
from engine.events import post_glow_effect
from engine.events import post_note_pressed


def create_grid(rows=3, columns=3):
    colors = iter(
            [
                    'gold', 'crimson', 'dodgerblue',
                    'fuchsia', 'silver', 'darkviolet',
                    'forestgreen', 'blue', 'chocolate',
            ]
    )
    note_values = iter(
            (
                    7, 8, 9,
                    4, 5, 6,
                    1, 2, 3,
            )
    )
    spacing = 20
    margin = 0
    size = 100
    half_size = size // 2
    cell_size = size + spacing
    centered_margin = margin + half_size

    cells = []
    for i, row in enumerate(range(rows)):
        for j, column in enumerate(range(columns)):
            x = column * cell_size + centered_margin + (settings.window_rect.width - (columns * cell_size)) / 2
            y = row * cell_size + centered_margin + (settings.window_rect.height - (rows * cell_size)) / 2
            note = next(note_values)
            color = pygame.Color(next(colors)).lerp((0, 0, 0), 0.5)

            entity = Entity(
                    FilledImageComponent((size, size), color),
                    PositionComponent((x, y)),
                    RectComponent(),
                    SoundComponent(f'SOUND_{note}'),
            )
            entity.add_component(
                    ClickComponent(
                            [pygame.BUTTON_LEFT],
                            callback=lambda obj=entity: play_note_on_click(obj),
                            callback_on_clicked=False
                    )
            )
            entity.add_component(
                    KeyboardComponent(
                            [getattr(pygame, f'K_KP_{note}')],
                            callback=lambda obj=entity: play_note_on_click(obj)
                    )
            )
            cells.append(entity)

    return cells

def play_note_on_click(entity):
    play_note(entity)
    post_note_pressed(entity)

def play_note(entity):
    entity.get_component(SoundComponent).play()
    post_glow_effect(entity, 2)
