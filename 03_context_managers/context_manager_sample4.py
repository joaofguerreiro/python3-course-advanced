"""
Sample on opening files that do not exist.
"""

with open('fauxfile.txt') as fobj:
	for line in fobj:
		print (line)
# Traceback (most recent call last):
#   File "context_manager_sample4.py", line 1, in <module>
#     with open('fauxfile.txt') as fobj:
# FileNotFoundError: [Errno 2] No such file or directory: 'fauxfile.txt'


# ===================== with a suppress context manager =====================
from contextlib import suppress
# nothing happens as the file does not exist, but an error is also not raised
with suppress(FileNotFoundError):
	with open('fauxfile.txt') as fobj:
		for line in fobj:
			print (line)
