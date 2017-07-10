"""
Here we create a defaultdict that will assign ‘Monkey’ as the default value to any key.
"""
from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print (animal['Nick'])
# Monkey

print (animal)
# defaultdict(<function <lambda> at 0x10afe7f28>, {'Sam': 'Tiger', 'Nick': 'Monkey'})


# Forcing a KeyError by setting the default_factory to None
x = defaultdict(None)
x['Mike']
# Traceback (most recent call last):
#   File "defaultdict_demo3.py", line 16, in <module>
#     x['Mike']
# KeyError: 'Mike'
