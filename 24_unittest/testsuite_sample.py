import unittest
from test_mymath2 import TestAdd


def my_suite():
	suite = unittest.TestSuite()
	result = unittest.TestResult()
	suite.addTest(unittest.makeSuite(TestAdd))  # turns our TestCase class into a suite
	runner = unittest.TextTestRunner()
	print (runner.run(suite))

my_suite()
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s

# OK
# <unittest.runner.TextTestResult run=3 errors=0 failures=0>
