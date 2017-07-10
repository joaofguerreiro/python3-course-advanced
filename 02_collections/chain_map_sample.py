"""
A ChainMap is a class that provides the ability to link multiple 
mappings together such that they end up being a single unit.

The ChainMap will go through each map in order to see if that key 
exists and has a value. If it does, then the ChainMap will return
 the first value it finds that matches that key.

Put into personal words: it is another way of updating a dictionary
but we get to keep the original smaller dictionaries that are aglutinated.
"""
from collections import ChainMap
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print (car_pricing['hood'])
# 500