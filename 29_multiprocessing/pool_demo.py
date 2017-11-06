from multiprocessing import Pool


def doubler(number):
	return number * 2


if __name__ == '__main__':
	numbers = [5, 10, 20]
	pool = Pool(processes=3)  # used to represent a pool of 3 worker processes
	print (pool.map(doubler, numbers))  # map a function and an iterable to each process
# [10, 20, 40]

	result = pool.apply_async(doubler, (25,))  # ask for the result of the process
	print (result.get(timeout=1))  # timeout set just in case something happened to the function
# 50
