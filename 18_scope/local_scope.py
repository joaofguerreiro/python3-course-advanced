def my_func(a, b):
    i = 2
    print(x)

if __name__ == '__main__':
	"""
	The variable, i, is only defined inside the function, 
	so when you run this code you will get a NameError.
    """
    x = 10
    my_func(1, 2)
    print(i)
# 10
# Traceback (most recent call last):
#   File "local_scope.py", line 8, in <module>
#     print(i)
# NameError: name 'i' is not defined
