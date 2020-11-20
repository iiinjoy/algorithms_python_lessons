#!/usr/bin/env python3

import unittest
from lesson6 import *


class TestDequeMethods(unittest.TestCase):

    def test_add_front(self):
        D = Deque()
        D.addFront(1)
        self.assertEqual(D.deque, [1])
        D.addFront(2)
        self.assertEqual(D.deque, [2, 1])
        self.assertEqual(D.size(), 2)

    def test_add_tail(self):
        D = Deque()
        D.addTail(3)
        self.assertEqual(D.deque, [3])
        D.addTail(4)
        self.assertEqual(D.deque, [3, 4])
        self.assertEqual(D.size(), 2)

    def test_remove_front(self):
        D = Deque()
        D.addFront(1)
        D.addFront(2)
        self.assertEqual(D.removeFront(), 2)
        self.assertEqual(D.removeFront(), 1)
        self.assertEqual(D.size(), 0)
        self.assertIsNone(D.removeFront())

    def test_remove_tail(self):
        D = Deque()
        D.addTail(3)
        D.addTail(4)
        self.assertEqual(D.removeTail(), 4)
        self.assertEqual(D.removeTail(), 3)
        self.assertEqual(D.size(), 0)
        self.assertIsNone(D.removeTail())

    def test_all(self):
        D = Deque()
        D.addFront(1)
        D.addTail(2)
        D.addFront(0)
        D.addTail(3)
        self.assertEqual(D.size(), 4)
        self.assertEqual(D.deque, [0, 1, 2, 3])
        for i in range(4):
            self.assertEqual(D.removeFront(), i)
        self.assertEqual(D.size(), 0)


if __name__ == '__main__':
    unittest.main()
