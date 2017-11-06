"""
The multiprocessing module allows to spawn processes the same way the threading module allows to
spawn threads. The advantage on multiprocessing module is that we can avoid the 
GIL (Global Interpreter Lock) and use in a real way multiple processors on a machine.
"""
import os

from multiprocessing import Process, current_process


def doubler(number):
	"""
	A doubling function that can be used by a process
	"""
	result = number * 2

	# Using process id
	# proc = os.getpid()  # we get the current process id by using the python module os
	# print ('{} doubled to {} by process id: {}'.format(number, result, proc))

	# Using process name 
	proc_name = current_process().name  # grabs the name of the process calling the function
	print ('{} doubled to {} by process: {}'.format(number, result, proc_name))


if __name__ == '__main__':
	numbers = [5, 10, 15, 20, 25]
	procs = []

	for index, number in enumerate(numbers):

		# Using process id
		proc = Process(target=doubler, args=(number,))  # creates a process for each number in the list
		procs.append(proc)
		proc.start()

	# Assigning process name
	proc = Process(target=doubler, name='Test', args=(2,))
	procs.append(proc)
	proc.start()

	for proc in procs:
		proc.join()  # tells Python to wait for the process to terminate

# Using process id
# 5 doubled to 10 by process id: 9544
# 10 doubled to 20 by process id: 9545
# 15 doubled to 30 by process id: 9546
# 20 doubled to 40 by process id: 9547
# 25 doubled to 50 by process id: 9548

# Using process name
# 5 doubled to 10 by process: Process-1
# 10 doubled to 20 by process: Process-2
# 15 doubled to 30 by process: Process-3
# 20 doubled to 40 by process: Process-4
# 25 doubled to 50 by process: Process-5
# 2 doubled to 4 by process: Test
