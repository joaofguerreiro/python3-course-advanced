"""
super() allows to access inherited methods that have been overridden in a class.
"""
class SubClass(MyParentClass):
	"""
	In Python 2, super() would be called this way.
	"""
    def __init__(self):
        super(SubClass, self).__init__()


class SubClass(MyParentClass):
	"""
	In Python 3, super() is called this way. Much better.
	"""
    def __init__(self, x, y):
        super().__init__(x, y)
