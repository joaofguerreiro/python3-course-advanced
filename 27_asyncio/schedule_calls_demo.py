import asyncio
import functools


def event_handler(loop, stop=False):
	print ('event handler called')

	if stop:
		print ('stopping the loop')
		loop.stop()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		# call_soon() will call your callback or event handler as soon as it can
		loop.call_soon(functools.partial(event_handler, loop))  # works as FIFO
		print ('starting event loop')

		# if you set stop to True, it will stop the event loop
		# the first time we call it, we do not stop the loop
		loop.call_soon(functools.partial(event_handler, loop, stop=True))

		# The reason we want to stop the loop is that we’ve told it to run_forever, 
		# which will put the event loop into an infinite loop.

		# to delay a call to 1 second in the future, use this:
		# loop.call_later(1, event_handler, loop)

		# to delay a call to a specific time in the future, use this:
		# current_time = loop.time()
		# loop.call_at(current_time + 300, event_handler, loop)

		loop.run_forever()
	finally:
		print ('closing event loop')
		loop.close()
# starting event loop
# event handler called
# event handler called
# stopping the loop
# closing event loop
