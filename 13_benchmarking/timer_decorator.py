import random
import time


def timerfunc(func):
	"""
	A timer decorator
	"""
	def function_timer(*args, **kwargs):
		"""
		A nested function for timing other functions
		"""
		start = time.time()
		value = func(*args, **kwargs)
		end = time.time()
		runtime = end - start
		msg = "The runtime for {func} took {time} seconds to complete"
		print (msg.format(func=func.__name__, time=runtime))
		return value
	return function_timer
# The nested function will grab the time before calling the passed in function. 
# Then it waits for the function to return and grabs the end time.

@timerfunc
def long_runner():
	for x in range(5):
		sleep_time = random.choice(range(1, 5))
		time.sleep(sleep_time)


if __name__ == '__main__':
	long_runner()
# The runtime for long_runner took 15.013960838317871 seconds to complete
