"""
According to the Python documentation, deques “are a generalization of stacks and queues”. 
They are pronounced “deck” which is short for "double-ended queue". They are a replacement 
container for the Python list. Deques are thread-safe and support memory efficient appends
and pops from either side of the deque.

A deque accepts a maxlen argument which sets the bounds for the deque. 
Otherwise the deque will grow to an arbitrary size.

When a bounded deque is full, any new items added will cause the same number of 
items to be popped off the other end.

To actually create an instance of a deque, we need to pass it an iterable.
"""
from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
	print (letter)
# a
# b
# c
# d
# e
# f
# g
# h
# i
# j
# k
# l
# m
# n
# o
# p
# q
# r
# s
# t
# u
# v
# w
# x
# y
# z

d.append('bork')  # appends a value to the end of the deque
print (d)
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
# 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.appendleft('test')  # appends a value to the start of the deque
print (d)
# deque(['test', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
# 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.rotate(1)  # Rotates to the right. If n is negative, rotates to the left.
print (d)
# deque(['bork', 'test', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
# 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


d = deque(string.ascii_lowercase, 5)  # 5 is the bound of this deque object.
for letter in d:
	print (letter)
# v
# w
# x
# y
# z
