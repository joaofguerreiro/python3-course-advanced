import doctest

doctest.testfile('add.txt')

"""
$ python3 testfile.py -v
	Trying:
	    from doctest_sample import add
	Expecting nothing
	ok
	Trying:
	    add(1, 2)
	Expecting:
	    3
	ok
	1 items passed all tests:
	   2 tests in add.txt
	2 tests in 1 items.
	2 passed and 0 failed.
Test passed.
"""
