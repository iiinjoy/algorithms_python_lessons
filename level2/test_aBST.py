#!/usr/bin/env python3

import unittest
from aBST import aBST


class Test_aBST_Methods(unittest.TestCase):

    def test_all(self):
        T = aBST(3)
        self.assertEqual(T.FindKeyIndex(42), 0)

        keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        for k in keys:
            T.AddKey(k)
        for i in range(len(keys)):
            self.assertEqual(i, T.FindKeyIndex(keys[i]))
            self.assertEqual(keys[i], T.Tree[i])
        self.assertIsNone(T.FindKeyIndex(42))
        self.assertEqual(T.AddKey(42), -1)

    def test_all2(self):
        T = aBST(3)
        T.AddKey(5)
        self.assertEqual(T.Tree[0], 5)
        self.assertEqual(T.FindKeyIndex(4), -1)
        self.assertEqual(T.FindKeyIndex(6), -2)
        T.AddKey(4)
        T.AddKey(6)
        self.assertEqual(T.FindKeyIndex(3), -3)
        self.assertEqual(T.FindKeyIndex(7), -6)

if __name__ == '__main__':
    unittest.main()
