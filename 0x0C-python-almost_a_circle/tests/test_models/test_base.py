#!/usr/bin/python3
"""testing Base class code"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """class with tests"""

    def check_id(self):
        """checking the id"""

        self.assertEqual(None, 1)
        self.assertEqual(Base(12), 12)
        self.assertEqual(None(), 2)
        self.assertEqual(Base(-1), -1)

    def to_js_str(self):
        """checking the dumps method"""

        self.assertEqual(None, "[]")
        result = Base.to_json_string([dictionary])
#        self.assertTrue(type(result), <class 'str'>)
#        self.assertTrue(type(list_dictionaries), <class 'dict'>)

    def test_doc(self):
        """testing docstring"""

        self.assertIsNotNone(Base.__doc__)

if __name__ == '__main__':
    unittest.main()
