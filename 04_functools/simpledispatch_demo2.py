"""
One of the add function overloads can handle float 
and decimal.Decimal types as the first argument.
"""
from functools import singledispatch
from decimal import Decimal


@singledispatch
def add(a, b):
	raise NotImplementedError('Unsupported type')


@add.register(float)
@add.register(Decimal)
def _(a, b):
	print ("First argument is of type ", type(a))
	print (a + b)


if __name__ == '__main__':
	add(1.23, 5.5)
	add(Decimal(100.5), Decimal(10.789))
	print (add.registry.keys())
# First argument is of type  <class 'float'>
# 6.73
# First argument is of type  <class 'decimal.Decimal'>
# 111.2889999999999997015720510
# dict_keys([<class 'object'>, <class 'decimal.Decimal'>, <class 'float'>])
