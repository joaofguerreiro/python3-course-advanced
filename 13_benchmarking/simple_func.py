def my_function():
	try:
		1 / 0
	except ZeroDivisionError:
		pass
"""
To get this simple function benchmarked, we use a module named 'timeit' which has a command line interface.

Our python code needs to be written inside doublequotes.

To benchmark Python importing our simple_func.py script:
[terminal command]$ python -m timeit -s "import simple_func"
100000000 loops, best of 3: 0.0128 usec per loop

To benchmark Python importing our simple_func.py script and running its my_function():
[terminal command]$ python3 -m timeit -s "import simple_func; simple_func.my_function()"
100000000 loops, best of 3: 0.0128 usec per loop
"""