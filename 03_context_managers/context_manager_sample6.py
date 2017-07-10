"""
By using the lower level context manager ExitStack, all opened files 
will automatically be closed at the end of
the with statement, even if attempts to open files later
in the list raise an exception.

It provides a suitable foundation for higher level context
managers that manipulate the exit stack in application specific ways.
"""
from contextlib import ExitStack
with ExitStack() as stack:
	file_objects = [stack.enter_context(open(filename) for filename in filenames]
