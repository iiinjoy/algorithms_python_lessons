#!/usr/bin/env python3

import unittest
from lesson4_5 import *


class TestParenthesesBalanced(unittest.TestCase):

    def test_is_parentheses_balanced(self):
        self.assertTrue(is_parentheses_balanced("()"))
        self.assertFalse(is_parentheses_balanced(")("))
        self.assertTrue(is_parentheses_balanced("(()((())()))"))
        self.assertFalse(is_parentheses_balanced("(()()(()"))
        self.assertFalse(is_parentheses_balanced("())("))
        self.assertFalse(is_parentheses_balanced("))(("))
        self.assertFalse(is_parentheses_balanced("((())"))
        self.assertTrue(is_parentheses_balanced("((((((((((()))))))))))"))

if __name__ == '__main__':
    unittest.main()
