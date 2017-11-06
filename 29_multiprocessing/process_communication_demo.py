from multiprocessing import Process, Queue


sentinel = -1


def creator(data, q):
	"""
	Creates data to be consumed and waits for the consumer to finish processing
	"""
	print ('Creating data and putting it on the queue')
	for item in data:
		q.put(item)  # puts the data into the queue


def my_consumer(q):
	"""
	Consumes some data and works on it

	In this case, all it does is double the input
	"""
	while True:
		data = q.get()  # gets the data that was put into the queue
		print ('data found to be processed: {}'.format(data))
		processed = data * 2
		print (processed)

		if data is sentinel:
			break


if __name__ == '__main__':
	q = Queue()  # the same queue is provided to creator and consumer functions
	data = [5, 10, 13, -1]
	process_one = Process(target=creator, args=(data, q))  # creates data
	process_two = Process(target=my_consumer, args=(q,))  # consumes the data
	process_one.start()
	process_two.start()

	q.close()  # closes because there will be no more data inserted into this queue
	q.join_thread()  # joins the background thread. can only be called after close()

	process_one.join()  # blocks process until all data in the queue is completely flushed
	process_two.join()  # blocks process until all data in the queue is completely flushed
# Creating data and putting it on the queue
# data found to be processed: 5
# 10
# data found to be processed: 10
# 20
# data found to be processed: 13
# 26
# data found to be processed: -1
# -2
