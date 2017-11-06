import logging
import multiprocessing

from multiprocessing import Process, Lock


def printer(item, lock):
	"""
	Prints out the item that was passed in
	"""
	with lock:
		print (item)


if __name__ == '__main__':
	lock = Lock()
	items = ['tango', 'foxtrot', 10]
	multiprocessing.log_to_stderr()  # simplest way to log is to send it all to stderr
	logger = multiprocessing.get_logger()
	logger.setLevel(logging.INFO)  # set its logging level to INFO
	for item in items:
		p = Process(target=printer, args=(item, lock))
		p.start()
# [INFO/Process-1] child process calling self.run()
# tango
# [INFO/Process-1] process shutting down
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# [INFO/MainProcess] calling join() for process Process-3
# [INFO/Process-2] child process calling self.run()
# foxtrot
# [INFO/Process-2] process shutting down
# [INFO/Process-2] process exiting with exitcode 0
# [INFO/Process-3] child process calling self.run()
# 10
# [INFO/Process-3] process shutting down
# [INFO/Process-3] process exiting with exitcode 0
# [INFO/MainProcess] calling join() for process Process-1
# [INFO/MainProcess] calling join() for process Process-2
