#!/usr/bin/python3
"""testing Rectangle class code"""
from io import StringIO
import sys
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class TestBaseMethods(unittest.TestCase):
    """class with tests"""

    @classmethod
    def setUp(cls):
        """setting Up"""
        sys.stdout = StringIO()
        cls.r1 = Rectangle(1, 2, 3, 4, 5)
        cls.r2 = Rectangle(5, 4, 3, 2, 1)
        Base._Base__nb_objects = 0

    def tearDown(self):
        """reset"""
        sys.stdout = sys.__stdout__

    def test_raises(self):
        """checks raises"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("", 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, "")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 3, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 3, 4, -4)

    def test_init__(self):
        """checking the id"""
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 2, 3, 4, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.id, 2)

    def test_area(self):
        """check the area calculation"""

        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(3, 5).area(), 15)
        self.assertEqual(Rectangle(2, 2, 1, 1).area(), 4)

    def test_display(self):
        """testing display rectangle"""
        self.Rectangle(2, 2).display()
        self.assertEqual(mystdout.getvalue(), "##\n##")

    def test_str(self):
        """str output"""
        self.assertEqual(str(self.r1), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(str(self.r2), "[Rectangle] (1) 3/2 - 5/4")

        
    def test_doc(self):
        """testing docstring"""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_display(self):
        """checking output"""

    if __name__ == '__main__':
        unittest.main()
