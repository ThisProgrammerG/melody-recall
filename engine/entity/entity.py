from engine.components import Component
from engine.components import FilledImageComponent
from engine.components import ImageComponent
from engine.components import PositionComponent
from engine.components import RectComponent
from engine.components import TextComponent


class Entity:
    def __init__(self, *args):
        self.components = {}

        for arg in args:
            if isinstance(arg, Component):
                self.add_component(arg)

        self._set_rect()

    def _set_rect(self):
        # ThisProgrammerG Refactor later
        rect_component = self.get_component(RectComponent)
        image_component = (
                self.get_component(ImageComponent)
                or self.get_component(TextComponent)
                or self.get_component(FilledImageComponent)
        )
        position_component = self.get_component(PositionComponent)

        if rect_component and image_component and position_component:
            rect_component.update(position_component.position, image_component.image.get_size())
        elif rect_component and image_component:
            rect_component.set_size(image_component.image.get_size())
        elif rect_component and position_component:
            rect_component.set_position(position_component.position)

    def add_component(self, component):
        self.components[type(component)] = component

    def remove_component(self, component_type):
        if component_type not in self.components:
            return
        del self.components[component_type]

    def get_component(self, component_type):
        return self.components.get(component_type)
