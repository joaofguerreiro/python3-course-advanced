"""
Benchmarking my code using the timeit module.
"""

def my_function():
	try:
		1 / 0
	except ZeroDivisionError:
		pass

if __name__ == "__main__":
	import timeit
	setup = "from __main__ import my_function"
	print (timeit.timeit("my_function()", setup))
# 0.8849668939947151
