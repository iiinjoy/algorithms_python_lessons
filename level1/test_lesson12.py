#!/usr/bin/env python3

import unittest
from lesson12 import *


class TestNativeCacheMethods(unittest.TestCase):

    def test(self):
        size = 26
        NC = NativeCache(size)
        for i in range(size):
            NC.put(chr(ord("a") + i), i)
        for i in range(size):
            self.assertEqual(NC.hits[i], 0)
        #for i in range(size):
        #    print("i={}  k={} hash={} v={}".format(i, NC.slots[i], NC.hash_fun(NC.slots[i]), NC.values[i]))
        #for i in range(size):
        #    k = chr(ord("A") + i)
        #    print("i={}  k={} hash={}".format(i, k, NC.hash_fun(k)))

        # hash_fun("A") == 6
        # hash_fun("x") == 9
        for i in range(size):
            key = chr(ord("a") + i)
            if key != "x":
                NC.get(key)
        NC.put("A", 42)
        self.assertIsNone(NC.get("x"))
        self.assertEqual(NC.get("A"), 42)
        for i in range(size):
            self.assertEqual(NC.hits[i], 1)
        # hash_fun("B") == 7
        # hash_fun("v") == 7
        NC.put("B", 123)
        self.assertIsNone(NC.get("v"))
        self.assertEqual(NC.get("B"), 123)

if __name__ == '__main__':
    unittest.main()
