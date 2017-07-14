"""
lru_cache is a decorator that adds caching to the function it decorates.
"""
import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
	"""
	Gets the specified Python module web page.
	We decorate our get_webpage function with lru_cache and set its max size to 24 calls.
	"""
	webpage = "https://docs.python.org/3/library/{}.html".format(module)
	try:
		with urllib.request.urlopen(webpage) as request:
			return request.read()
	except urllib.error.HTTPError:
		return None

if __name__ == '__main__':
	modules = ['functool', 'collections', 'os', 'sys']
	for module in modules:
		page = get_webpage(module)
	if page:
		print ("{} module page found".format(module))
		# sys module page found
