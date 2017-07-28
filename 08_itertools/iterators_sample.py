"""
Several infinite iterators are addressed in this sample file: 
	count(), islice(), cycle(), repeat()
"""
from itertools import count
for i in count(10):  # count() also accepts a step parameter
	if i > 20:
		break
	else:
		print (i)
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

from itertools import islice
for i in islice(count(10), 5):  # starts iterating at 10 and ends after 5 iterations
	print (i)
# 10
# 11
# 12
# 13
# 14


from itertools import cycle
count = 0
for item in cycle('XYZ'):  # cycles through a series of values infinitely, 'XYZ' here
	if count > 7:
		break
	print (item)
	count += 1
# X
# Y
# Z
# X
# Y
# Z
# X
# Y


polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
print (next(iterator))
# triangle

print (next(iterator))
# square

print (next(iterator))  # we can call next(iterator) all day long and never run out of items
# pentagon


from itertools import repeat
repeat(5, 5)

iterator = repeat(5, 5)  # repeats the number 5 five times
print (next(iterator))
# 5

print (next(iterator))
# 5

print (next(iterator))
# 5

print (next(iterator))
# 5

print (next(iterator))
# 5

print (next(iterator))
# Traceback (most recent call last):
#   File "iterators_sample.py", line 80, in <module>
#     print (next(iterator))
# StopIteration
