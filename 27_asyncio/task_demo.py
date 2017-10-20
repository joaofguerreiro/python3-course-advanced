import asyncio


async def my_task(seconds):
	"""
	This task is an asynchronous function that accepts the number of 
	seconds it will take for the function to run.
	"""
	print ('This task is taking {} seconds to complete'.format(seconds))
	asyncio.sleep(seconds)
	return 'task finished'


if __name__ == '__main__':
	my_event_loop = asyncio.get_event_loop()
	try:
		print ('task creation started')
		# create a task object by calling the event loop object’s create_task function
		task_obj = my_event_loop.create_task(my_task(seconds=2))
		# event loop will run until the task completes
		my_event_loop.run_until_complete(task_obj)
	finally:
		my_event_loop.close()

	print ("The task's result was: {}".format(task_obj.result()))
# task creation started
# This task is taking 2 seconds to complete
# The task's result was: task finished
