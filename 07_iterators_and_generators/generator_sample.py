"""
A generator works by “saving” where it last left off (or yielding) and giving 
the calling function a value. So instead of returning the execution to the caller, 
it just gives temporary control back. 

One of the biggest benefits to a generator is that it canterate over large
data sets and return them one piece at a time.

A generator is great for memory efficient data processing.
"""
def doubler_generator():
	number = 2
	while True:
		yield number
		number *= number

# the generator is also defining the __next__ method that we looked at in our 
# previous section, which is why the next keyword we just used worked.
doubler = doubler_generator()
print (next(doubler))
# 2

print (next(doubler))
# 4

print (next(doubler))
# 16

print (type(doubler))
# <class 'generator'>


def silly_generator():
	yield "Python"
	yield "Rocks"
	yield "So do you!"
gen = silly_generator()

print (next(gen))
# Python

print (next(gen))
# Rocks

print (next(gen))
# So do you!

print (next(gen))
# Traceback (most recent call last):
#   File "generator_sample.py", line 43, in <module>
#     print (next(gen))
# StopIteration
