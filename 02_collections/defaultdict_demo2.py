# ======================== Old school attempt ============================
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acct_num, value in my_list:
	if acct_num in reg_dict:
		reg_dict[acct_num].append(value)
	else:
		reg_dict[acct_num] = [value]

print (reg_dict)
# {
# 	1234: [100.23, 75.0, 35.67], 
# 	345: [10.45, 222.66], 678: [300.25]
# }


# ======================== defaultdict attempt ============================
from collections import defaultdict


my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
	d[acct_num].append(value)

print (d)
# defaultdict(<class 'list'>, {
# 	1234: [100.23, 75.0, 35.67], 
# 	345: [10.45, 222.66], 678: [300.25]
# })
