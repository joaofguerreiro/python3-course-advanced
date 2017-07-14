"""
You can use partial to “freeze” a portion of your function’s arguments 
and/or keywords which results in a new object. Another way to put it 
is that partial creates a new function with some defaults. 
"""
from functools import partial
def add(x, y):
		return x + y

p_add = partial(add, 2) 
# We are basically defaulting the x parameter of our add function to the number 2.
print(p_add(4))
# 6