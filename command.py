from typing import T

class Stack:
    def __init__(self):
        self.list: List[T] = []

    @property
    def is_empty(self):
        return len(self.list) == 0

    def push(self, item: T) -> None:
        self.list.append(item)

    def pop(self) -> T:
        if not self.is_empty:
            return self.list.pop()

class Command:
    def __init__(self, *args, **kwargs):
        self.device = None
        
    def execute(self) -> None:
        raise ValueError('Method "execute" must be implemented!')

    def undo(self) -> None:
        raise ValueError('Method "undo" must be implemented!')

    def set_device(self, device) -> None:
        self.device = device

class VolumeUpCommand(Command):
    def __init__(self, volume: int):
        super().__init__()
        self.volume = volume

    def execute(self):
        if self.device:
            self.device.volume_up(self.volume)

    def undo(self):
        if self.device:
            self.device.volume_down(self.volume)

class TVDevice:
    def __init__(self):
        self.command_history = Stack()
        self.volume = 50
        self.is_on = False

    def __repr__(self):
        return f'TVDevice(volume={self.volume}, is_on={self.is_on})'

    def on(self) -> None:
        self.is_on = True

    def off(self) -> None:
        self.is_on = False

    def volume_up(self, value: int) -> None:
        self.volume += value

    def volume_down(self, value: int) -> None:
        self.volume -= value

    def execute_command(self, command: Command) -> None:
        command.set_device(self)
        command.execute()
        self.command_history.push(command)

    def ctr_z(self) -> None:
        command: Command = self.command_history.pop()
        command.undo()

if __name__ == '__main__':
    tv = TVDevice()
    print(tv)
    
    tv.execute_command(VolumeUpCommand(10))
    print(tv)
    
    tv.ctr_z()
    print(tv)

    up_30_command = VolumeUpCommand(30)
    tv.execute_command(up_30_command)
    print(tv)
    up_30_command.undo()
    print(tv)
