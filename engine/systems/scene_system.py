from engine import clock
from engine.events.event_handlers import SceneEventHandler
from engine.systems import EventSystem
from engine.systems import RenderSystem
from engine.systems import TimerSystem


class SceneSystem:
    def __init__(self):
        self.timer_system = TimerSystem()
        self.render_system = RenderSystem()
        self.event_system = EventSystem()
        self.event_system.register_handler(SceneEventHandler(self))
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes.setdefault(scene, scene)

    def add_scenes(self, *scenes):
        for scene in scenes:
            self.add_scene(scene)

    def _exit_scene(self):
        if not self.current_scene:
            return
        self.current_scene.exit()

    def _enter_scene(self):
        if not self.current_scene:
            return
        self.current_scene.enter()

    def set_scene(self, scene_type):
        self._exit_scene()
        self.current_scene = self.scenes[scene_type](self.event_system, self.render_system)
        self._enter_scene()

    def update(self):
        while self.event_system.running:
            self.timer_system.update()
            self.current_scene.update()
            self.event_system.update()
            self.render_system.update(self.current_scene.objects)
            clock.tick()
