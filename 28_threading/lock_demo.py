import threading
"""
We may have a use case where more than one thread will need to access the same resource at the same time.

A lock is provided by Python’s threading module and can be held by either a single thread or no thread at all.
Should a thread try to acquire a lock on a resource that is already locked, 
that thread will basically pause until the lock is released.
"""

total = 0
lock = threading.Lock()  # acquire the lock before anything else

def update_total(amount):
	"""
	Updates the total by the given amount
	"""
	global total

	# Old way of doing things:
	# lock.acquire()
	# try:
	# 	total += amount
	# finally: 
	# 	lock.release()

	# New way of doing things, using a context manager:
	with lock:
		total += amount
	print (total)


if __name__ == '__main__':
	for i in range(10):
		my_thread = threading.Thread(target=update_total, args=(5,))
		my_thread.start()
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
