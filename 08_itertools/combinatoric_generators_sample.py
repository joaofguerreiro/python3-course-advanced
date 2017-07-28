"""
Four iterators that can be used for creating combinations and permutations of data:
	combinations(), combinations_with_replacement(), product(), permutations()
"""
from itertools import combinations
print (list(combinations('WXYZ', 2)))  # combinations returns tuples
# [('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
for item in combinations('WXYZ', 2):
	print (''.join(item))  # little easier to see all the various combination
# WX
# WY
# WZ
# XY
# XZ
# YZ


from itertools import combinations_with_replacement  # will actually create combinations where elements do repeat
for item in combinations_with_replacement('WXYZ', 2):
	print (''.join(item))
# WW
# WX
# WY
# WZ
# XX
# XY
# XZ
# YY
# YZ
# ZZ


from itertools import product
arrays = [(-1,1), (-3,3), (-5,5)]
cp = list(product(*arrays))  # creates Cartesian products from a series of input iterables
print (cp)
# [(-1, -3, -5),
# (-1, -3, 5),
# (-1, 3, -5),
# (-1, 3, 5),
# (1, -3, -5),
# (1, -3, 5),
# (1, 3, -5),
# (1, 3, 5)]


from itertools import permutations
for item in permutations('WXYZ', 3):  # returns successive r length permutations of elements from the iterable 
	print (''.join(item))
# WXY
# WXZ
# WYX
# WYZ
# WZX
# WZY
# XWY
# XWZ
# XYW
# XYZ
# XZW
# XZY
# YWX
# YWZ
# YXW
# YXZ
# YZW
# YZX
# ZWX
# ZWY
# ZXW
# ZXY
# ZYW
# ZYX
