#!/usr/bin/python3
"""testing Base class code"""
import os
import sys
import json
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """class with tests"""

    def test_check_id(self):
        """checking the id"""
        r1 = Base()
        self.assertEqual(r1.id, 1)
        r2 = Base(12)
        self.assertEqual(r2.id, 12)
        r3 = Base()
        self.assertEqual(r3.id, 2)
        r4 = Base(-1)
        self.assertEqual(r4.id, -1)

    def test_to_js_str(self):
        """checking the dumps method"""

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
#        result = Base.to_json_string([dictionary])
#        self.assertTrue(type(result), <class 'str'>)
#        self.assertTrue(type(list_dictionaries), <class 'dict'>)

    def test_doc(self):
        """testing docstring"""

        self.assertIsNotNone(Base.__doc__)

if __name__ == '__main__':
    unittest.main()
