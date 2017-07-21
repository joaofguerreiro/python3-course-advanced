import importlib
import foo


def dynamic_import(module):
	"""
	Calls importlib’s import_module function with the module 
	string that we passed in and returns the result of that call. 
	"""
	return importlib.import_module(module)


if __name__ == '__main__':
	module = dynamic_import('foo')
	module.main()

	module_two = dynamic_import('bar')
	module_two.main()
# foo
# bar
