from engine.events import post_scene_switch_event


def switch_to_settings_scene():
    from .settings_scene import SettingsScene

    post_scene_switch_event(SettingsScene)

def switch_to_game_scene():
    from .game_scene import GameScene

    post_scene_switch_event(GameScene)

def switch_to_main_menu_scene():
    from .main_menu_scene import MainMenuScene

    post_scene_switch_event(MainMenuScene)
