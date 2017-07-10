"""
Context managers are handy constructs that allow you to set 
something up and tear something down automatically.

Examples below.
"""

# after Python 2.5
with open(path, 'w') as f_obj:
	f_obj.write(some_data)

# before Python 2.4
f_obj = open(path, 'w')
f_obj.write(some_data)
f_obj.close()
