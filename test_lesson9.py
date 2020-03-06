#!/usr/bin/env python3

import unittest
from lesson9 import *


class TestNativeDictionaryMethods(unittest.TestCase):

    def test_hash_fun(self):
        ND = NativeDictionary(13)
        self.assertEqual(ND.hash_fun("a"), 12)
        self.assertEqual(ND.hash_fun("n"), 12)

    def test_all(self):
        ND = NativeDictionary(13)
        # put
        ND.put("a", "Value")
        self.assertIsNotNone(ND.slots[ND.hash_fun("a")])
        self.assertIsNotNone(ND.values[ND.hash_fun("a")])
        # get
        self.assertEqual(ND.get("a"), "Value")
        # put same key
        ND.put("a", "Different")
        self.assertEqual(ND.get("a"), "Different")
        # all
        seq1 = "abcdefghij"
        seq2 = ""
        for i in seq1:
            ND.put(i, i)
        for i in seq1:
            self.assertTrue(ND.is_key(i))
            self.assertEqual(ND.get(i), i)
            seq2 += i
        self.assertEqual(seq1, seq2)

if __name__ == '__main__':
    unittest.main()
