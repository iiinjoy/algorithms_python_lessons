#!/usr/bin/env

import unittest
from lesson5 import *


class TestQueue(unittest.TestCase):

    def test_queue(self):
        Q = Queue()
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


if __name__ == '__main__':
    unittest.main()
