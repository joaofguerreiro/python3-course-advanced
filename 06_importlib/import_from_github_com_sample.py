"""
import_from_github_com uses pip to install the package if it’s not installed and then 
it uses Python’s __import__() function to actually import the newly installed module.
"""

# Run:
# pip3 install import_from_github_com

# Inside a python3 console:
from github_com.zzzeek import sqlalchemy
# Collecting git+https://github.com/zzzeek/sqlalchemy
#   Cloning https://github.com/zzzeek/sqlalchemy to /private/var/folders/jb/kfvwn4j91bs2r7hdnvpl495r0000gn/T/pip-q4s7_ly1-build
# Installing collected packages: SQLAlchemy
#   Running setup.py install for SQLAlchemy ... done
# Successfully installed SQLAlchemy-1.2.0b2.dev0

print (locals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, 
# '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, 
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
# 'sqlalchemy': <module 'sqlalchemy' from '/usr/local/lib/python3.6/site-packages/sqlalchemy/__init__.py'>}

# Run:
# pip3 uninstall sqlalchemy
