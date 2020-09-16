from typing import Callable

FunctionReturnsInt = Callable[[int, int], int]

def minus_one_decorator(func: FunctionReturnsInt, /):
    def inner(a: int, b: int):
        result: int = func(a, b)
        return result -1
    return inner

@minus_one_decorator
def add_int(a: int, b: int, /) -> int:
    if not all([isinstance(a, int), isinstance(b, int)]):
        raise ValueError('This function only can add 2 integers together!')
    return a + b


if __name__ == '__main__':
    a, b = 5, 2
    print(f'Result of the add_int({a},{b}) function is: {add_int(a,b)}')
    
    # add_int = minus_one_decorator(add_int)
    print(f'Result of the new add_int({a},{b}) function is: {add_int(a,b)}')
    
