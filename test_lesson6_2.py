#!/usr/bin/env python3

import unittest
from lesson6_2 import *


class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("DOGMAIAMGOD"))
        self.assertTrue(is_palindrome("43211234"))
        self.assertFalse(is_palindrome("12345321"))
        self.assertTrue(is_palindrome("1"))
        self.assertFalse(is_palindrome("aaA"))

if __name__ == '__main__':
    unittest.main()
