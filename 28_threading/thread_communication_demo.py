import threading
from queue import Queue


def creator(data, q):
	"""
	Creates data to be consumed and waits for the consumer to finish processing
	"""
	print ('Creating data and putting it on the queue')
	for item in data:
		evt = threading.Event()

		# The queue will have the first thread feed data to the second
		q.put((item, evt))  # puts the data into the queue and passes in an event

		print ('Waiting for data to be doubled')
		evt.wait()  # waits for the event to finish
		print ('first thread is done')
		# this thread ends when it runs out of items to put into the Queue


def my_consumer(q):
	"""
	Consumes some data and works on it

	In this case, all it does is double the input
	"""
	while True:
		print ('second thread in action')
		data, evt = q.get()  # consumer will check for data that was put into the queue
		print ('data found to be processed: {}'.format(data))
		processed = data * 2
		print (processed)
		evt.set()  # tells the first thread that the second is done processing and it can continue
		q.task_done()


if __name__ == '__main__':
	q = Queue()
	data = [5, 10, 13, -1]  # list of values we want to double, aka data

	# The secret is to provide the same queue to both threads
	thread_one = threading.Thread(target=creator, args=(data, q))  # creator thread
	thread_two = threading.Thread(target=my_consumer, args=(q,))  # consumer thread
	thread_one.start()
	thread_two.start()
	"""
	What happens is:
	- first thread starts
	- first thread puts data and an event into the queue
	- first thread waits there
	- second thread starts, gets the data and processes it
	- second thread announces to first thread that it can resume its work
	- second thread stops
	- first thread stops
	"""
	q.join()  # tells the Queue to wait for both threads to finish

# Creating data and putting it on the queue
# Waiting for data to be doubled
# second thread in action
# data found to be processed: 5
# 10
# second thread in action
# first thread is done
# Waiting for data to be doubled
# data found to be processed: 10
# 20
# second thread in action
# first thread is done
# Waiting for data to be doubled
# data found to be processed: 13
# 26
# second thread in action
# first thread is done
# Waiting for data to be doubled
# data found to be processed: -1
# -2
# second thread in action
# first thread is done
