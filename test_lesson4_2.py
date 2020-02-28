#!/usr/bin/env python3

import unittest
from lesson4_2 import *


class TestStackMethods(unittest.TestCase):

    def test_pop(self):
        S = Stack()
        self.assertEqual(S.size(), 0)
        S.push(42)
        self.assertEqual(S.size(), 1)
        item = S.pop()
        self.assertEqual(item, 42)
        self.assertEqual(S.size(), 0)
        S.push(1)
        S.push(2)
        self.assertEqual(S.size(), 2)
        item1 = S.pop()
        item2 = S.pop()
        self.assertEqual(item1, 2)
        self.assertEqual(item2, 1)
        self.assertEqual(S.size(), 0)
        item_none = S.pop()
        self.assertIsNone(item_none)

    def test_push(self):
        S = Stack()
        for i in range(10):
            S.push(i)
        self.assertEqual(S.size(), 10)
        while(S.size() > 0):
            S.pop()
        self.assertEqual(S.size(), 0)

    def test_peek(self):
        S = Stack()
        item_none = S.peek()
        self.assertIsNone(item_none)
        for i in range(10):
            S.push(i)
        item9 = S.peek()
        self.assertEqual(item9, 9)
        for i in range(9):
            S.pop()
        self.assertEqual(S.peek(), 0)

if __name__ == '__main__':
    unittest.main()
