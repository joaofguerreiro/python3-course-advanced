"""
Python includes the global statement. It is a keyword of Python.
The global statement declares a variable as being available for the code block following the statement.
"""


def my_func(a, b):
	# By declaring x to be a global, we tell Python to use the 
	# first declaration of x for our first print statement in the function. 
    global x
    print(x)
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    # Since x is now global when we reach the last print statement at the end of the code, x is still 5.
    print(x)
# 10
# 5
# 5


def my_func(a, b):
	"""
	Mixing globals and locals
	"""
    global c
    # swap a and b
    b, a = a, b
    d = 'Mike'
    print(a, b, c, d)

a, b, c, d = 1, 2, 'c is global', 4
my_func(1, 2)
print(a, b, c, d)
# 2 1 c is global Mike
# 1 2 c is global 4
