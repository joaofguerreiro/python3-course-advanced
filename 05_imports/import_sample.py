"""
Several ways of importing modules and submodules.
"""
import sys as system
print (system.platform)
# darwin

import urllib.error  # imports submodule error from module urllib

from functools import lru_cache  # imports submodule lru_cache from module functools
from os import *  # imports all submodules from module os
from os import path, walk, unlink  # imports explicit submodules from module os
from os import (
	path,
	walk,
	unlink,
)

from os import path, walk, \
			unlink  # line continuation

from . import subpackage1  # relative import
from . subpackage1 import module_x  # 2nd level relative import


# conditional imports
try:
	# for Python 3
	from http.client import responses
except ImportError:  
	# for Python 2.7
	try:
		from httplib import responses
	except ImportError:
		# for Python 2.4
		from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH


def square_root(a):
	"""This import is into the square_root functions local scope 
	and can only be accessed by this function.
	"""
	import math
	return math.sqrt(a)

# ================= Circular Imports ================= 
# These will happen if we create two modules that import each other.

# ================= Shadowed Imports ================= 
# Happens when we create a module with the same name as a Python module.

