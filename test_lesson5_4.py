#!/usr/bin/env

import unittest
from lesson5_4 import *


class TestQueue2(unittest.TestCase):

    def test_queue2(self):
        Q = Queue2()
        self.assertEqual(Q.size(), 0)
        Q.enqueue(1)
        Q.enqueue(2)
        self.assertEqual(Q.size(), 2)
        item1 = Q.dequeue()
        item2 = Q.dequeue()
        self.assertEqual(item1, 1)
        self.assertEqual(item2, 2)
        self.assertEqual(Q.size(), 0)
        self.assertIsNone(Q.dequeue())

        for i in range(10):
            Q.enqueue(i)
        for i in range(5):
            self.assertEqual(Q.dequeue(), i)
        for i in range(10, 15):
            Q.enqueue(i)
        for i in range(5, 15):
            self.assertEqual(Q.dequeue(), i)
        self.assertEqual(Q.size(), 0)
        self.assertIsNone(Q.dequeue())


if __name__ == '__main__':
    unittest.main()
