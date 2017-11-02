import logging
import threading


class MyThread(threading.Thread):

	def __init__(self, number, logger):
		threading.Thread.__init__(self)
		self.number = number
		self.logger = logger

	def run(self):
		"""
		Run the thread
		"""
		logger.debug('Calling doubler')
		doubler(self.number, self.logger)


def get_logger():
	logger = logging.getLogger("threading_example")
	logger.setLevel(logging.DEBUG)


	fh = logging.FileHandler("threading_class.log")
	fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
	formatter = logging.Formatter(fmt)
	fh.setFormatter(formatter)

	logger.addHandler(fh)
	return logger


def doubler(number, logger):  # we pass the logger to the function so we have only one logging object during runtime
    """
    A function that can be used by a thread
    """
    logger.debug('doubler function executing')  # instead of printing, we log the statements
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(result))


if __name__ == '__main__':
	logger = get_logger()
	thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
	for i in range(5):
		thread = MyThread(i, logger)
		thread.setName(thread_names[i])
		thread.start()  # this will run the thread by calling the run method, which calls the doubler function

