from typing import List

class Subscriber:
    def update(self, *args, **kwargs) -> None:
        raise NotImplementedError('Update method must be implemented!')
    

class Publisher:
    def __init__(self, *args, **kwargs):
        self.subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        if not subscriber in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def publish(self, *args, **kwargs) -> None:
        for subscriber in self.subscribers:
            subscriber.update(*args, **kwargs)
            

if __name__ == '__main__':
    class AmercianCompany(Subscriber):
        def update(self, *args, **kwargs) -> None:
            print(f'Hello from America: {args}\t{kwargs}')
            

    class EuropeanCompany(Subscriber):
        def update(self, *args, **kwargs) -> None:
            print(f'Hello from Europe: {args}\t{kwargs}')
            

    class News(Publisher):
        def __init__(self, name: str):
            super().__init__(name)
            self.name = name


    news = News('CNN')
    american = AmercianCompany()
    european = EuropeanCompany()

    news.subscribe(american)
    news.subscribe(european)

    news.publish('Be aware!', type='DANGER')

    news.unsubscribe(american)

    news.publish('Be happy!', type='NATURAL')
