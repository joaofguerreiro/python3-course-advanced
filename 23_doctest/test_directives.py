"""
>>> print(list(range(100))) # doctest: +ELLIPSIS
[0, 1, ..., 98, 99]

>>> class Dog: pass

>>> Dog() #doctest: +ELLIPSIS
<__main__.Dog object at 0x...>
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
The ELLIPSIS flag allows us to cut out part of the output and still pass the test.
"""

"""
$ python3 test_directives.py -v
	Trying:
	    print(list(range(100))) # doctest: +ELLIPSIS
	Expecting:
	    [0, 1, ..., 98, 99]
	ok
	Trying:
	    class Dog: pass
	Expecting nothing
	ok
	Trying:
	    Dog() #doctest: +ELLIPSIS
	Expecting:
	    <__main__.Dog object at 0x...>
	ok
	1 items passed all tests:
	   3 tests in __main__
	3 tests in 1 items.
	3 passed and 0 failed.
	Test passed.
"""
