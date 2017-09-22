"""
The doctest module works by examining the docstrings in the module, 
from the module level to the function, class and method levels. 
It will not look at imported modules though.

We can't use doctest on an id or a dictionary as they are quite dynamic.
"""

def add(a, b):
    """
    Return the addition of the arguments: a + b

    >>> add(1, 2)
    3
    >>> add(-1, 10)
    9
    >>> add('a', 'b')
    'ab'
    >>> add(1, '2')
    Traceback (most recent call last):
      File "test.py", line 17, in <module>
        add(1, '2')
      File "test.py", line 14, in add
        return a + b
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


"""When running the module in a bash shell:
    $ python -m doctest -v test.py
    Trying:
        add(1, 2)
    Expecting:
        3
    ok
    Trying:
        add(-1, 10)
    Expecting:
        9
    ok
    Trying:
        add('a', 'b')
    Expecting:
        'ab'
    ok
    Trying:
        add(1, '2')
    Expecting:
        Traceback (most recent call last):
          File "test.py", line 17, in <module>
            add(1, '2')
          File "test.py", line 14, in add
            return a + b
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ok
    1 items had no tests:
        __main__
    1 items passed all tests:
       4 tests in __main__.add
    4 tests in 2 items.
    4 passed and 0 failed.
    Test passed.
"""
