from collections import namedtuple


Parts = namedtuple('Parts', 'id_num desc cost amount')  # Creates a new tuple class.
auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200.00, amount=10)
print (auto_parts.id_num)
# 1234

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}

# Creates a new tuple class and instantiates it right away.
parts = namedtuple('Parts', Parts.keys())(**Parts)  
print (parts)
# Parts(id_num='1234', desc='Ford Engine', cost=1200.0, amount=10)


# ======================== Using a regular tuple ============================
auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
print (auto_parts[2])
# 1200.0

id_num, desc, cost, amount = auto_parts
print (id_num)
# 1234
