"""
Counter is a subclass of Python's dictionary.
A Counter object can be run against most iterables.

It counts the repetitions of each element in the iterable.

The method elements() will iterate over all the elements, 
in an arbitrary order. You can kind of think of this function
as a “scrambler” as the output in this case is a scrambled
version of the string.

The method most_common() returns the most common elements (a tuple with
the element and the times it occurred.
It receives a number that represents the top recurring "n" elements.

The method subtract() will remove the argument object out of the self object.
As in, it will decrement the repetition of elements in the argument from the self object.
"""
from collections import Counter

print (Counter('superfluous'))
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

counter = Counter('superfluous')
print (counter['u'])
# 3

print (list(counter.elements()))
# ['s', 's', 'u', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']

print (counter.most_common(2))
# [('u', 3), ('s', 2)]

counter_one = Counter('superfluous')
print (counter_one)
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

counter_two = Counter('super')
print (counter_one.subtract(counter_two))
#None

print (counter_one)
# Counter({'u': 2, 's': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 0, 'e': 0, 'r': 0})
