import importlib.util

def check_module(module_name):
    """
    Checks if module can be imported without actually
    importing it
    """
    # When you pass in a module name that is not installed, 
    # the find_spec function will return None and our code will 
    # print out that the module was not found. 
    # If it was found, then we will return the module specification. 
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
        return None
    else:
        print('Module: {} can be imported!'.format(module_name))
        return module_spec

def import_module_from_spec(module_spec):
    """
    Import the module via the passed in module specification
    Returns the newly imported module
    """
    module = importlib.util.module_from_spec(module_spec) # returns the import module
    module_spec.loader.exec_module(module) # executes module, as recommended by Python docs
    return module


if __name__ == '__main__':
    module_spec = check_module('fake_module')
    module_spec = check_module('collections')
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))
# Module: fake_module not found
# Module: collections can be imported!
# ['AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable', 'ByteString', 
# 'Callable', 'ChainMap', 'Collection', 'Container', 'Coroutine', 'Counter', 'Generator', 
# 'Hashable', 'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'Mapping', 'MappingView', 
# 'MutableMapping', 'MutableSequence', 'MutableSet', 'OrderedDict', 'Reversible', 
# 'Sequence', 'Set', 'Sized', 'UserDict', 'UserList', 'UserString', 'ValuesView', '_Link', 
# '_OrderedDictItemsView', '_OrderedDictKeysView', '_OrderedDictValuesView', '__all__', 
# '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__path__', '__spec__', '_chain', '_class_template', '_collections_abc', 
# '_count_elements', '_eq', '_field_template', '_heapq', '_iskeyword', '_itemgetter', 
# '_proxy', '_recursive_repr', '_repeat', '_repr_template', '_starmap', '_sys', 
# 'defaultdict', 'deque', 'namedtuple']
