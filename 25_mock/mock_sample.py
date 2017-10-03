"""
A mock object is used for simulating system resources that aren’t available in your test environment.
"""
from unittest.mock import Mock, create_autospec, patch
import urllib.request


# my_mock = Mock()
# my_mock.__str__ = Mock(return_value='Mocking')
# print (str(my_mock))
# # Mocking

# class TestClass:
# 	pass

# cls = TestClass()
# cls.method = Mock(return_value='mocking is fun')
# print (cls.method(1, 2, 3))
# # mocking is fun

# cls.method.assert_called_once_with(1, 2, 3)
# print (cls.method(1, 2, 3))
# # mocking is fun

# cls.method.assert_called_once_with(1, 2, 3)
# # Traceback (most recent call last):
# #   File "mock_sample.py", line 23, in <module>
# #     cls.method.assert_called_once_with(1, 2, 3)
# #   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/unittest/mock.py", line 824, in assert_called_once_with
# #     raise AssertionError(msg)
# # AssertionError: Expected 'mock' to be called once. Called 2 times.

# cls.other_method = Mock(return_value='Something else')
# cls.other_method.assert_not_called()


# """
# A side effect is something that happens when you run your function.
# """
# def my_side_effect():
# 	print ('Updating database!')


# def main():
# 	mock = Mock(side_effect=my_side_effect)
# 	mock()


# if __name__ == '__main__':
# 	main()
# Updating database!


# """
# The autospec allows you to create mock objects that contain the same attributes and methods 
# of the objects that you are replacing with your mock.
# """
# def add(a, b):
# 	return a + b

# mocked_func = create_autospec(add, return_value=10)
# print (mocked_func(1, 2))
# # 10

# mocked_func(1, 2, 3)
# Traceback (most recent call last):
#   File "mock_sample.py", line 64, in <module>
#     mocked_func(1, 2, 3)
#   File "<string>", line 2, in add
#   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/unittest/mock.py", line 171, in checksig
#     sig.bind(*args, **kwargs)
#   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/inspect.py", line 2933, in bind
#     return args[0]._bind(args[1:], kwargs)
#   File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/inspect.py", line 2854, in _bind
#     raise TypeError('too many positional arguments') from None
# TypeError: too many positional arguments


"""
Patch will allow you to easily create mock classes or objects in a module that 
you want to test as it will be replaced by a mock.
"""
def read_webpage(url):
	response = urllib.request.urlopen(url)
	return response.read()


@patch('urllib.request.urlopen')
def dummy_reader(mock_obj):
	result = read_webpage('https://www.google.com/')
	mock_obj.assert_called_with('https://www.google.com/')
	print (result)

if __name__ == '__main__':
	dummy_reader()
# <MagicMock name='urlopen().read()' id='4318947816'>
