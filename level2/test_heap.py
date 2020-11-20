#!/usr/bin/env python3

import unittest
from heap import *


class TestHeapMethods(unittest.TestCase):

    def testMakeHeap(self):
        H = Heap()
        H.MakeHeap([1,2,3,4], 2)
        self.assertEqual(H.HeapArray, [4,3,2,1] + [None] * 3)

        H.MakeHeap([11,9,4,7,8,3,1,2,5,6], 3)
        self.assertEqual(H.HeapArray, [11,9,4,7,8,3,1,2,5,6] + [None] * 5)

    def testGetFilledSize(self):
        self.assertEqual(Heap.GetFilledSize([]), 0)
        self.assertEqual(Heap.GetFilledSize([1,2,3]), 3)
        self.assertEqual(Heap.GetFilledSize([1,2,3,None,None]), 3)
        self.assertEqual(Heap.GetFilledSize([None,None,None]), 0)

    def testGetMax(self):
        H = Heap()
        self.assertEqual(H.GetMax(), -1)
        H.MakeHeap([11,9,4,7,8,3,1,2,5,6], 3)
        elem = H.GetMax()
        self.assertEqual(elem, 11)
        self.assertEqual(H.HeapArray, [9,8,4,7,6,3,1,2,5] + [None] * 6)

    def testAdd(self):
        H = Heap()
        self.assertFalse(H.Add(42))
        H.MakeHeap([1,2,3,4], 2)
        self.assertTrue(H.Add(5))
        self.assertEqual(H.HeapArray, [5,4,2,1,3,None,None])
        self.assertTrue(H.Add(5))
        self.assertEqual(H.HeapArray, [5,4,5,1,3,2,None])
        self.assertTrue(H.Add(6))
        self.assertEqual(H.HeapArray, [6,4,5,1,3,2,5])
        self.assertFalse(H.Add(42))

if __name__ == '__main__':
    unittest.main()
