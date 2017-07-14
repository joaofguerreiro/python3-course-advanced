"""
It calls the appropriate function based on the first argument’s type. 
If the type isn’t handled, then we raise a NotImplementedError.
"""
from functools import singledispatch


@singledispatch
def add(a, b):
	raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
	print ("First argument is of type ", type(a))
	print (a + b)


@add.register(str)
def _(a, b):
	print ("First argument is of type ", type(a))
	print (a + b)


@add.register(list)
def _(a, b):
	print ("First argument is of type ", type(a))
	print (a + b)


if __name__ == '__main__':
	add(1, 2)
	add('Python', 'Programming')
	add([1, 2, 3], [5, 6, 7])
	add({'teste': 'teste'}, {'teste2': 'teste2'})
# First argument is of type  <class 'int'>
# 3
# First argument is of type  <class 'str'>
# PythonProgramming
# First argument is of type  <class 'list'>
# [1, 2, 3, 5, 6, 7]
# Traceback (most recent call last):
#   File "simpledispatch_demo.py", line 34, in <module>
#     add({'teste': 'teste'}, {'teste2': 'teste2'})
#   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/functools.py", line 803, in wrapper
#     return dispatch(args[0].__class__)(*args, **kw)
#   File "simpledispatch_demo.py", line 9, in add
#     raise NotImplementedError('Unsupported type')
# NotImplementedError: Unsupported type

print (add.registry.keys())
# dict_keys([<class 'object'>, <class 'int'>, <class 'str'>, <class 'list'>])
