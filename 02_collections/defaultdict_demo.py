"""
The defaultdict is a subclass of Python’s dict that accepts a default_factory
as its primary argument. The default_factory is usually a Python type, 
such as int or list, but you can also use a function or a lambda too.
"""

# ======================== Old school attempt ============================
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
	if word in reg_dict:
		reg_dict[word] += 1
	else:
		reg_dict[word] = 1

print (reg_dict)
# {
# 	'The': 1, 
# 	'red': 1, 
# 	'for': 2, 
# 	'jumped': 1, 
# 	'over': 1, 
# 	'the': 2, 
# 	'fence': 1, 
# 	'and': 1, 
# 	'ran': 1, 
# 	'to': 1, 
# 	'zoo': 1, 
# 	'food': 1
# }


# ======================== defaultdict attempt ============================
from collections import defaultdict


sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
	d[word] += 1

print (d)
# defaultdict(<class 'int'>, {
# 	'The': 1, 
# 	'red': 1, 
# 	'for': 2, 
# 	'jumped': 1, 
# 	'over': 1, 
# 	'the': 2, 
# 	'fence': 1, 
# 	'and': 1, 
# 	'ran': 1, 
# 	'to': 1, 
# 	'zoo': 1, 
# 	'food': 1
# })
