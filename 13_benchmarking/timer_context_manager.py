import random 
import time


class MyTimer():
	"""
	A context manager that tracks running time.
	"""
	
	def __init__(self):
		self.start = time.time()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""
		Here we grab the end time, calculate the total run time and print it out.
		"""
		end = time.time()
		runtime = end - self.start
		msg = "The function took {time} seconds to complete"
		print (msg.format(time=runtime))


def long_runner():
	for x in range(5):
		sleep_time = random.choice(range(1, 5))
		time.sleep(sleep_time)


if __name__ == '__main__':
	with MyTimer():
		long_runner()
# The function took 15.012794017791748 seconds to complete
