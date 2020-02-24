#!/usr/bin/env python3

import unittest
from lesson1_8 import *


class TestMethods(unittest.TestCase):

    def test_LL_to_list(self):
        LL = LinkedList()
        LL.add_in_tail(Node(1))
        LL.add_in_tail(Node(2))
        LL.add_in_tail(Node(3))
        L = LL_to_list(LL)
        self.assertEqual(L, [1, 2, 3])

    def test_LL_to_list_empty(self):
        LL = LinkedList()
        L = LL_to_list(LL)
        self.assertEqual(L, [])

    def test_zipWithAdd(self):
        LL1 = LinkedList()
        LL1.add_in_tail(Node(1))
        LL1.add_in_tail(Node(2))
        LL1.add_in_tail(Node(3))
        LL2 = LinkedList()
        LL2.add_in_tail(Node(4))
        LL2.add_in_tail(Node(5))
        LL2.add_in_tail(Node(6))
        self.assertEqual(zipWithAdd(LL1, LL2), [5, 7, 9])

    def test_zipWithAdd_diff_len(self):
        LL1 = LinkedList()
        LL1.add_in_tail(Node(1))
        LL1.add_in_tail(Node(2))
        LL1.add_in_tail(Node(3))
        LL2 = LinkedList()
        LL2.add_in_tail(Node(4))
        LL2.add_in_tail(Node(5))
        LL2.add_in_tail(Node(6))
        LL2.add_in_tail(Node(7))
        self.assertIsNone(zipWithAdd(LL1, LL2))

if __name__ == '__main__':
    unittest.main()
