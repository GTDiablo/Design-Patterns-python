from typing import Union

class Websocket:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Websocket({self.name})'

class MyWebsocket:
    def __init__(self):
        self.instance: Union[Websocket, None] = None

    def get_instance(self):
        if not self.instance:
            self.instance = Websocket('Egyedi')
        return self.instance

if __name__ == '__main__':
    my_ws = MyWebsocket()
    
    w1 = my_ws.get_instance()
    print(w1, hash(w1))
    
    w2 = my_ws.get_instance()
    print(w2, hash(w2))
    
