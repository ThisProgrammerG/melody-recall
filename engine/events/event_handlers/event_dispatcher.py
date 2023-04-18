from collections import defaultdict
from collections import deque


class EventDispatcher:
    def __init__(self):
        self.handlers = defaultdict(list)
        self.events = deque()

    def add_event(self, event):
        self.events.append(event)

    def add_events(self, events):
        self.events.extend(events)

    def register_handler(self, handler):
        for event_type in handler.event_types:
            if handler not in self.handlers[event_type]:
                self.handlers[event_type].append(handler)

    def unregister_handler(self, handler):
        for event_type in handler.event_types:
            self.handlers[event_type].remove(handler)

    def dispatch_events(self):
        while self.events:
            event = self.events.popleft()
            handlers = self.handlers.get(event.type, [])
            for handler in handlers:
                handler.handle_event(event)
