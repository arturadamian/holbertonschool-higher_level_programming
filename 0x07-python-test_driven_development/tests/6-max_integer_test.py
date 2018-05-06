#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """a unittest to find the max_int in a list
    """
    def output_test(self):
        """Test for outputs
        """
        self.assertEqual(max_integer([5, 6, 7]), 7)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3, 6, 4]), 6)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1.9, -2, -3]), -1.9)
        self.assertEqual(max_integer([[1], [2], [3]]), [3])
        self.assertEqual(max_integer({}), None)
