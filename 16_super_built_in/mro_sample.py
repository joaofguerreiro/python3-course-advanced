"""
Method Resolution Order (MRO) is just a list of types that the class is derived from.
"""
class Base:
    var = 5
    def __init__(self):
        pass

class X(Base):
    def __init__(self):
        print('X')
        super().__init__()

class Y(Base):
    var = 10
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


"""
Class Z inherits from X and Y. So when we ask it what its var is, 
the MRO will look at X to see if it is defined. 
It’s not there, so it moves on to Y. Y has it, so that is what gets returned.
"""
z = Z()
print (Z.__mro__)
print (super(Z, z).var)  # Prints var from class Y because it comes first in the inheritance order.
# X
# Y
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Base'>, <class 'object'>)
# 10


class Base():
    def __init__(self):
        s = super()
        print(s.__thisclass__)
        print(s.__self_class__)
        s.__init__()

class SubClass(Base):
    pass

sub = SubClass()
# <class '__main__.Base'>
# <class '__main__.SubClass'>
