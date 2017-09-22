import mymath
import sys
import unittest


class TestAdd(unittest.TestCase):
	"""
	Tests the add function from the mymath library.
	"""

	def test_add_integers(self):
		"""
		Tests that the addition of two integers returns the correct total.
		"""
		result = mymath.add(1, 2)
		self.assertEqual(result, 3)

	def test_add_floats(self):
		"""
		Tests that the addition of two floats returns the correct result.
		"""
		result = mymath.add(10.5, 2)
		self.assertEqual(result, 12.5)

	@unittest.skip('Skip this test')  # Test is ignored because of the decorator
	def test_add_strings(self):
		"""
		Tests that the addition of two strings returns the two string as one concatenated string.
		"""
		result = mymath.add('abc', 'def')
		self.assertEqual(result, 'abcdef')

	@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows") # Test is ignored if platform is Windows	
	def test_adding_on_windows(self):
		result = mymath.add(1, 2)
		self.assertEqual(result, 3)

# $ python3 -m unittest test_mymath2.py -v
# test_add_floats (test_mymath2.TestAdd) ... ok
# test_add_integers (test_mymath2.TestAdd) ... ok
# test_add_strings (test_mymath2.TestAdd) ... skipped 'Skip this test'
# test_adding_on_windows (test_mymath2.TestAdd) ... skipped 'requires Windows'

# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK (skipped=2)
