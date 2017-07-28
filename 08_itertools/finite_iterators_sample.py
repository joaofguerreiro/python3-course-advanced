"""
Several finite iterators and iterating tools are addressed in this sample file:
	accumulate(), chain(), compress(), dropwhile(), filterfalse(), groupby(), 
	islice(), startmap(), takewhile(), tee(), zip_longest()
"""
from itertools import accumulate
print (list(accumulate(range(10))))  # return accumulated sums or the accumulated results
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]


import operator
print (list(accumulate(range(1, 10), operator.mul)))  # returns accumulated multiplications
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


from itertools import chain
my_list = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
# take a series of iterables and basically flatten them down into one long iterable
my_list = list(chain(['foo', 'bar'], cmd, numbers))
# this would have worked too: my_list += cmd + numbers
print (my_list)
# ['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]


print (list(chain.from_iterable([cmd, numbers])))
# ['ls', '/some/dir', 0, 1, 2, 3, 4]


from itertools import compress
letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print (list(compress(letters, bools)))  # checks the first against the second, keeps the first if match is True
# ['A', 'C', 'D']


from itertools import dropwhile
print (list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # drops elements as long as the filter criteria is True
# [6, 4, 1]


def great_than_five(x):
	return x > 5
# Once we hit a value that is less than 5, then ALL the values after and including that value will be kept
print (list(dropwhile(great_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
# [1, 2, 3, 10]


from itertools import filterfalse
# filterfalse will only return those values that evaluated to False
print (list(filterfalse(great_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
# [1, 2, 3]


from itertools import groupby
vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]
sorted_vehicles = sorted(vehicles)  # very important to sort the list when using groupby() iterator
# loop over the iterator returned by groupby which gives us the key and the group
for key, group in groupby(sorted_vehicles, lambda make: make[0]):
	# loop over the group and print out what’s in it
	for make, model in group:
		print ('{model} is made by {make}'.format(model=model, make=make))

	print ("*** END OF GROUP ***\n")
# Cobalt is made by Chevrolet
# *** END OF GROUP ***

# Charger is made by Dodge
# Durango is made by Dodge
# *** END OF GROUP ***

# F150 is made by Ford
# GT is made by Ford
# Taurus is made by Ford
# *** END OF GROUP ***


from itertools import islice, count
for i in islice(count(), 3, 15):  # starts at the number 3 and stops when we reach 15
	print (i)
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14


from itertools import starmap
def add(a,b):
	return a+b
# starmap() passes each tuple element into the function and returns an iterator of the results
for item in starmap(add, [(2,3), (4,5)]):
	print (item)
# 5
# 9


from itertools import takewhile  # basically the opposite of the dropwhile iterator 
print (list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
# [1, 4]


from itertools import tee
data = 'ABCDE'
iter1, iter2 = tee(data) # will create n iterators from a single iterable
for item in iter1: 
	print (item)
# A
# B
# C
# D
# E
for item in iter2:
	print (item)
# A
# B
# C
# D
# E


from itertools import zip_longest
for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):  # zips two iterables together
	# The first two tuples are combinations of the first and second letters from each string respectively. 
	# The last two has our fill value inserted
	print (item)
# ('A', 'x')
# ('B', 'y')
# ('C', 'BLANK')
# ('D', 'BLANK')
