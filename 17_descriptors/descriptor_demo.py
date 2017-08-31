"""
WeakKeyDictionary, which is a neat class that creates a dictionary that maps keys weakly. 
What this means is that when there are no strong references to a key in the dictionary, 
that key and its value will be discarded.
"""
from weakref import WeakKeyDictionary


class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance_obj, objtype):
        return self.age.get(instance_obj, self.req_age)

    def __set__(self, instance, new_age):
        if new_age < 21:
            msg = '{name} is too young to legally imbibe'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print('{name} can legally drink in the USA'.format(
            name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age
"""
If we were to try to print out the drinker_age, Python would execute Person.drinker_age.__get__. 
Since drinker_age is a descriptor, its __get__ is what actually gets called.

Since we want to set the drinker_age, Python calls Person.drinker_age.__set__ and since that method 
is also implemented in our descriptor, then the descriptor method is the one that gets called.
"""

p = Person('Miguel', 30)
p = Person('Niki', 13)
# Miguel can legally drink in the USA
# Traceback (most recent call last):
#   File "descriptor_demo.py", line 33, in <module>
#     p = Person('Niki', 13)
#   File "descriptor_demo.py", line 29, in __init__
#     self.drinker_age = age
#   File "descriptor_demo.py", line 15, in __set__
#     raise Exception(msg.format(name=instance.name))
# Exception: Niki is too young to legally imbibe
