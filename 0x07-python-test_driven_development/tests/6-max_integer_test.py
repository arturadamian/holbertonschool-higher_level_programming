#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a unittest to find the max_int in a list
    Raises:
        TypeError: raises a error if there are....
    """
    def test_max_int(self):
        """
        Cheks if the integer is max integer
        """
        result = max_integer([6, 7, 5, 4])
        self.assertEqual(result, 7)
        result = max_integer([13, 2, 1, 5])
        self.assertEqual(result, 13)

    def test_isint(self):
        """
        Checks the variable against an integer
        """
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 7
        self.assertTrue(max_integer([1, x]) == x)

    def test_same_entry(self):
        """
        Checks to see if max int is same
        """
        a = 88
        self.assertEqual(max_integer([a, a, a, a]), a)

    def test_float_int(self):
        """
        Checks to see if float is the max integer
        """
        self.assertEqual(max_integer([7.0, 6, 5]), 7.0)

    def test_one_entry(self):
        """
        Checks if there is only one entry
        """
        self.assertEqual(max_integer([13]), 13)

    def test_negative_int(self):
        """
        Checks only negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_no_argument(self):
        """
        Checks that None is returned if there is no argument
        """
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """
        Checks if list is empty
        """
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
