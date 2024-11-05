import unittest
## Test DRIVEN DEVELOPMENT
from development import *

class TestExercises(unittest.TestCase):

    # 1. Write a test that fails
    def test_is_item_in_list(self):
        self.assertTrue( is_item_in_list(3, [1, 2, 3]))
        self.assertFalse( is_item_in_list(3, [1, 2 ]))

    # 1. Write a test that fails
    def test_is_palindrom(self):
        self.assertTrue(is_palindrome("kayak"))
        self.assertFalse(is_palindrome("pen"))
        self.assertFalse(is_palindrome("&&&"))
        self.assertFalse(is_palindrome("t"))

if __name__ == "__main__":
    unittest.main()