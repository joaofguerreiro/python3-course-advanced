"""
We import wraps from the functools module and use it as a decorator 
for the nested wrapper function inside of another_function.
"""
from functools import wraps


def another_function(func):
	"""
	A function that accepts another function
	"""

	@wraps(func)
	def wrapper():
		"""
        A wrapping function
        """
		val = "The result of %s is %s" % (func(), eval(func()))
		return val
	return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)
# a_function
# A pretty useless function
