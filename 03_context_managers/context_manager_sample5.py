# before Python 3.4 and Python 3.5 
import sys

path = 'text.txt'
with open(path, 'w') as fobj:
	sys.stdout = fobj  # old way of redirecting stdout elsewhere
	help(sum)


# after Python 3.4 and Python 3.5 using a contextlib module
from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
	with redirect_stdout(fobj):  # new way of redirecting stdout elsewhere
		help(redirect_stdout)
