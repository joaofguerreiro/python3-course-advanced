"""
A descriptor is invoked automatically when you access an attribute. 
A typical example would be my_obj.attribute_name.

The magic behind this lies in the magic method known as __getattribute__,
which will turn my_obj.a into this: type(my_obj).__dict__['a'].__get__(a, type(a)).

A descriptor can be created in one of the following ways:
- __get__(self, obj, type=None), returns value
- __set__(self, obj, value), returns None
- __delete__(self, obj), returns None
"""

class MyDescriptor():
    """
    A simple demo descriptor
    """
    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value

class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='desc')
    normal = 10

if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)
# Getting desc
# Mike
# 10
# Setting desc to 100
# Getting desc
# 100
