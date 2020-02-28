#!/usr/bin/env python3

import unittest
from lesson4_6 import *


class TestPostfixEval(unittest.TestCase):

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("1 2 3 4 5 ="), [5, 4, 3, 2, 1])
        self.assertEqual(postfix_eval("1 2 3 4 + + + ="), [10])
        self.assertEqual(postfix_eval("1 2 3 4 * * * ="), [24])
        self.assertEqual(postfix_eval("="), [])
        self.assertEqual(postfix_eval("8 2 + 5 * 9 + ="), [59])

if __name__ == '__main__':
    unittest.main()
