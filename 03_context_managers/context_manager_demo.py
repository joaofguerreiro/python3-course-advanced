from contextlib import contextmanager


@contextmanager  # This allows us to call file_open() using Python’s 'with' statement
def file_open(path):
	try:
		f_obj = open(path, 'w')
		yield f_obj  # When a yield statement is executed, the state of the generator is frozen
	except OSError:
		print ("We had an error!")
	finally: 
		print ("Closing file")
		f_obj.close()

if __name__ == '__main__':
	with file_open('test.txt') as fobj:
		fobj.write('Testing context managers')
		print ("Still open but about to close")
	print ("See? It's closed now")
	