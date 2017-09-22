import doctest
import my_docs
import unittest


# The function name is required for Test Discovery to work
def load_tests(loader, tests, ignore):
	tests.addTests(doctest.DocTestSuite(my_docs))  # Adding a suite to the tests object
	# Each docstring is considered a single test
	return tests
# $ python3 -m unittest discover -v
# add (my_docs)
# Doctest: my_docs.add ... ok
# subtract (my_docs)
# Doctest: my_docs.subtract ... ok

# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s

# OK
