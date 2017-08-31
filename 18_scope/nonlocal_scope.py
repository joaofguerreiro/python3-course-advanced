"""
The nonlocal keyword adds a scope override to the inner scope.

Basically nonlocal will allow you to assign variables in an outer scope, 
but not a global scope. So we can’t use nonlocal in our counter function 
because then it would try to assign to a global scope.
"""
def counter():
	"""
	This type of function is known as a closure. 
	A closure is basically a block of code that “closes” nonlocal variables. 
	The idea behind a closure is that you can reference variables that are 
	defined outside of your function.
    """
    num = 0
    def incrementer():
    	# You must use nonlocal in a nested function.
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()

print (c)
#<function counter.<locals>.incrementer at 0x7f78918f3378>

print (c())
#1

print (c())
#2

print (c())
#3
