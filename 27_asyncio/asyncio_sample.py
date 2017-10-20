"""
Asyncio provides infrastructure for writing single-threaded concurrent code using coroutines,
multiplexing I/O access over sockets and other resources, running network clients and servers, 
and other related primitives.

The module resolves around the event loop. 
An event loop basically says "when event A happens, react with function B".

See this example of event loop:
When a user loads the web page, the server will check for and call one or more event handlers.
Once those event handlers are done, they need to give control back to the event loop. 
To do this in Python, asyncio uses coroutines.

A coroutine is a special function that can give up control to its caller without losing its state.
They don't use too much memory unlike threads.

When you run a coroutine, it doesn't execute. Instead, it returns a coroutine object that you can
pass to the event loop to have it executed either immediately or later on.

A future object represents the result of work that hasn't completed.
The event loop can watch future objects and wait for them to finish. When a future finishes, it is set to done.

A Task is a wrapper for a coroutine and a subclass of Future. You can schedule a Task using the event loop.
"""

import asyncio


# Python 3.4 coroutine example
@asyncio.coroutine  # this decorator still works in Python 3.5
def my_coro():
	yield from func()



# Python 3.5 coroutine example
async def my_coro():
	# async / await keywords can be considered an API to be used for asynchronous programming
	await func()
