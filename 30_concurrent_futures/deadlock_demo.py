from concurrent.futures import ThreadPoolExecutor


def wait_forever():
	"""
	This function will wait forever if there's only one thread assigned to the pool
	"""
	my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
	
	# Creates a deadlock
	# result = my_future.result()
	# print (result)

	# Works
	return my_future  # returns the inner future from this


if __name__ == '__main__':

	# Creates a deadlock
	# executor = ThreadPoolExecutor(max_workers=1)  # won't work because there is only one worker at max
	# # We’ve just created a deadlock! The reason is that we are having one Future wait for another Future to finish.
	# executor.submit(wait_forever)

	# Works
	executor = ThreadPoolExecutor(max_workers=3)
	fut = executor.submit(wait_forever)

	result = fut.result()
	print (list(result.result()))
# [(1, 4), (2, 5), (3, 6)]
