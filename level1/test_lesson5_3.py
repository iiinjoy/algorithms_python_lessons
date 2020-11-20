#!/usr/bin/env

import unittest
from lesson5_3 import *


class TestRotateQueue(unittest.TestCase):

    def test_rotate_queue(self):
        Q = Queue()
        Q.enqueue(1)
        rotate_queue(Q, 10)
        item = Q.dequeue()
        self.assertEqual(item, 1)
        for i in range(10):
            Q.enqueue(i)
        rotate_queue(Q, 5)
        for i in range(5, 10):
            self.assertEqual(Q.dequeue(), i)
        for i in range(5):
            self.assertEqual(Q.dequeue(), i)
        self.assertEqual(Q.size(), 0)


if __name__ == '__main__':
    unittest.main()
