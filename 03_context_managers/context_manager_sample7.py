"""
Most context managers that you create will be written such 
that they can only be used once using a with statement.
The second time we try running it, a RuntimeError is raised.

Examples below.
"""
from contextlib import contextmanager
@contextmanager
def single():
	print ('Yielding')
	yield
	print ('Exiting context manager')

context = single()
with context:
	pass
# Yielding
# Exiting context manager

with context:
	pass
# Traceback (most recent call last):
#   File "context_manager_sample7.py", line 14, in <module>
#     with context:
#   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/
# Versions/3.6/lib/python3.6/contextlib.py", line 84, in __enter__
#     raise RuntimeError("generator sdidn't yield") from None
# RuntimeError: generator didn't yield


# ========== using the redirect_stdout, a "reentrant" context manager ==========
from contextlib import redirect_stdout
from io import StringIO
stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
	print ('Write something to the stream')
	with write_to_stream:
		print ('Write something else to stream')

print (stream.getvalue())
# Write something to the stream
# Write something else to stream
