from multiprocessing import Process, Lock


def printer(item, lock):
	"""
	Prints out the item that was passed in
	"""
	
	# Old way
	# lock.acquire()
	# try:
	# 	print (item)
	# finally:
	# 	lock.release()

	# New way
	with lock:
		print (item)


if __name__ == '__main__':
	lock = Lock()
	items = ['tango', 'foxtrot', 10]
	for item in items:
		p = Process(target=printer, args=(item, lock))
		# Because we’re using locks, the next process in line will wait for the lock to release before it can continue.
		p.start() 
# tango
# foxtrot
# 10
