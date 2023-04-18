from engine.scenes import GameScene
from engine.scenes import MainMenuScene
from engine.scenes import SettingsScene
from engine.systems.scene_system import SceneSystem


class Application:
    def __init__(self):
        self.scene_system = SceneSystem()
        self.scene_system.add_scenes(MainMenuScene, GameScene, SettingsScene)
        self.scene_system.set_scene(MainMenuScene)

    def run(self):
        self.scene_system.update()
