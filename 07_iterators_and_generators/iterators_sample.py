"""
An iterator is an object that will allow you to iterate over a container. 
The iterator in Python is implemented via two distinct methods: __iter__ and __next__.
"""
# The list is an iterable, but not an iterator because it does not implement __next__.
lst = [1,2,3]

print (iter(lst))
# <list_iterator object at 0x109b36e80>
lst_iterator = iter(lst)
print (next(lst_iterator))
# 1
print (next(lst_iterator))
# 2
print (next(lst_iterator))
# 3
print (next(lst_iterator))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# Turning the list into an iterator:
for item in iter(lst):
	print (item)
# 1
# 2
# 3
