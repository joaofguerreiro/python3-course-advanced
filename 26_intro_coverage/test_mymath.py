import mymath
import unittest
"""
Coverage.py is a 3rd party tool for Python that is used for measuring your code coverage.

The term “coverage” in programming circles is typically used to describe the 
effectiveness of your tests and how much of your code is actually covered by tests.
"""

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


class TestSubtract(unittest.TestCase):
    """
    Tests the subtract function frmo the mymath library
    """

    def test_subtract_integers(self):
        """
        Tests the subtracting integers returns the correct result
        """
        result = mymath.subtract(10, 8)
        self.assertEqual(result, 2)


class TestMultiply(unittest.TestCase):
    """
    Tests the multiply function from the mymath library
    """

    def test_subtract_integers(self):
        """
        Test that multiplying integers returns the correct result
        """
        result = mymath.multiply(5, 50)
        self.assertEqual(result, 250)


class TestDivide(unittest.TestCase):
    """
    Test the divide the function from the mymath library
    """

    def test_divide_by_zero(self):
        """
        Tests that multiplying integers returns the correct result
        """
        with self.assertRaises(ZeroDivisionError):
            result = mymath.divide(8, 0)


if __name__ == '__main__':
    unittest.main()
# $ coverage report -m
#     Name             Stmts   Miss  Cover   Missing
#     ----------------------------------------------
#     mymath.py            8      3    62%   11, 14, 17
#     test_mymath.py      14      0   100%
#     ----------------------------------------------
#     TOTAL               22      3    86%
