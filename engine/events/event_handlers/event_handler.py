from abc import ABC
from abc import abstractmethod


class EventHandler(ABC):
    @property
    @abstractmethod
    def event_types(self) -> list[int]:
        """"""

    @abstractmethod
    def handles(self, event):
        """"""

    @abstractmethod
    def handle_event(self, event):
        """"""
