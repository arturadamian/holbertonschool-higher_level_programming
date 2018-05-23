#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseMethods(unittest.TestCase):
    
    def check_id(self):
        
        self.assertEqual(None, 1)
        self.assertEqual(Base(12), 12)
        self.assertEqual(None(), 2)
        self.assertEqual(Base(-1), -1)
        
    def to_js_str(self):

        self.assertEqual(None, "[]")
        result = Base.to_json_string([dictionary])
        self.assertTrue(type(result), <class 'str'>)
        self.assertTrue(type(list_dictionaries), <class 'dict'>)
















    
if __name__ == '__main__':
    unittest.main()
