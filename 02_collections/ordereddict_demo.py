"""
As the name implies, OrderedDict keeps track of the order of the keys as they are added.

popitem() will return and remove a (key, item) pair.

move_to_end() will move an existing key to either end of the OrderedDict, 
right if the last argument of the OrderedDict is True, left if False.
"""

# ======================== Using a regular dictionary ============================
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)
# {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

keys = d.keys()
print (keys)
# dict_keys(['banana', 'apple', 'pear', 'orange'])

keys = sorted(keys)
print (keys)
# ['apple', 'banana', 'orange', 'pear']

for key in keys:
	print (key, d[key])
# apple 4
# banana 3
# orange 2
# pear 1


# ======================== Using OrderedDict ============================
from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
new_d['mango'] = 1  # last item in the OrderedDict because it was the last item added
print (new_d)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1), ('mango', 1)])

for key in reversed(new_d):
	print (key, new_d[key])
# mango 1
# pear 1
# orange 2
# banana 3
# apple 4

new_d.popitem() # pass an argument 'last' equal to False to pop the first item instead
print (new_d)
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
