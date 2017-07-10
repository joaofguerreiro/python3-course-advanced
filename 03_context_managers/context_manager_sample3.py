"""
The class closing would look like something of this kind:

from contextlib import contextmanager

@contextmanager
def closing(db):
	try:
		yield db.conn()
	finally:
		db.close()
"""
from contextlib import closing
from urllib.request import urlopen

# we open a url page but wrap it with our closing class. 
# This will cause the handle to the web page to be closed 
# once we fall out of the with statement’s code block.
with closing(urlopen('http://www.google.com')) as webpage:
	for line in webpage:
		pass
