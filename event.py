from collections import defaultdict
from enum import Enum
from typing import Callable, T, List

EventCallbackFunction = Callable[[dict], None]

class EventType(Enum):
    ClickEvent = 'ClickEvent'
    PressEvent = 'PressEvent'

class Event:
    def __init__(self, event_type: EventType, event_data: dict = {}):
        self.type = event_type
        self.data = event_data

class Dispatcher:
    def __init__(self, object: T = None):
        self.object = object
        self.event_listeners = defaultdict(list)

    def on(self, event: Event, callback: EventCallbackFunction) -> None:
        self.event_listeners[event].append(callback)

    def dispatch(self, event: Event) -> None:
        for callback in self.event_listeners.get(event.type, []):
            callback(event.data)


if __name__ == '__main__':
    dispatcher = Dispatcher()

    def click_callback(event_data: dict) -> None:
        print(f'User has clicked at x:{event_data["x"]}, y:{event_data["y"]}')

    def press_callback(event_data: dict) -> None:
        print(f'User pressed key with code: {event_data["key_code"]}')

    dispatcher.on(EventType.ClickEvent, click_callback)
    dispatcher.on(EventType.PressEvent, press_callback)

    my_click_event = Event(EventType.ClickEvent, {'x': 10, 'y': 20})
    my_press_event = Event(EventType.PressEvent, {'key_code': 101})

    from time import sleep
    dispatcher.dispatch(my_click_event)
    sleep(2)
    dispatcher.dispatch(my_press_event)

    

    
