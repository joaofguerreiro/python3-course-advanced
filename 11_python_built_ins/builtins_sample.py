"""
any() returns True if any element in the iterable is True.
"""
print (any([0,0,0,1]))
# True


"""
enumerate() returns the position of each item in the iterable as well as the value.
"""
my_string = 'abcdefg'
for pos, letter in enumerate(my_string):
	print (pos, letter)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g


"""
eval() accepts strings and basically runs them. This is a controversial builtin so caution is required.
"""
var = 10
source = 'var * 2'
print (eval(source))
# 20


"""
filter() takes a function and an iterable, returning an iterator for
the iterable's elements for which the function returns True.
"""
def less_than_ten(x):
	return x < 10

my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
	print (item)
# 1
# 2
# 3



"""
map() takes a function and an iterable and return an iterator that applies the function to each item in the iterable.
"""
def doubler(x):
	return x * 2

my_list = [1, 2, 3, 4, 5]
print (list(map(doubler, my_list)))
# [2, 4, 6, 8, 10]
for item in map(doubler, my_list):
	print (item)
# 2
# 4
# 6
# 8
# 10


"""
zip() takes a series of iterables and aggregates the elements from each of them.
"""
keys = ['x', 'y', 'z']
values = [5, 6, 7]
print (zip(keys, values))
# <zip object at 0x10940a8c8>
print (list(zip(keys, values)))
# [('x', 5), ('y', 6), ('z', 7)]
keys = ['x', 'y', 'z']
values = [5, 6, 7]
my_dict = dict(zip(keys, values))
print (my_dict)
# {'x': 5, 'y': 6, 'z': 7}



