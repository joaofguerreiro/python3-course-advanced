"""
Type hints aren’t a replacement for good documentation, 
but they do enhance our ability to understand our code in the future.
"""
from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a: int, b: int) -> int:
    print("First argument is of type ", type(a))
    print(a + b)
    return a + b


@add.register(str)
def _(a: str, b: str) -> str:
    print("First argument is of type ", type(a))
    print(a + b)
    return a + b


@add.register(list)
def _(a: list, b: list) -> list:
    print("First argument is of type ", type(a))
    print(a + b)
    return a + b
