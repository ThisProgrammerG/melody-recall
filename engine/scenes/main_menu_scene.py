import pygame

from engine import settings
from engine.components import ClickComponent
from engine.components import KeyboardComponent
from engine.components import PositionComponent
from engine.components import RectComponent
from engine.components import TextComponent
from engine.events.event_handlers import KeyboardEventHandler
from engine.scenes import Scene
from engine.scenes import switch_to_game_scene
from engine.entity import Entity


class MainMenuScene(Scene):
    def __init__(self, event_system, render_system):
        super().__init__(event_system, render_system)
        self.objects.extend(
                [
                        Entity(
                                TextComponent('Play'),
                                PositionComponent((settings.window_rect.centerx, 400)),
                                RectComponent(),
                                ClickComponent([pygame.BUTTON_LEFT], switch_to_game_scene),
                                KeyboardComponent([pygame.K_RETURN, pygame.K_KP_ENTER], switch_to_game_scene)

                        ),
                        # UI(
                        #         TextComponent('Settings'),
                        #         PositionComponent((settings.window_rect.centerx, 450)),
                        #         ClickComponent(switch_to_settings_scene),
                        #         RectComponent(),
                        # )
                ]
        )
        self.handlers.append(KeyboardEventHandler(self.objects))
