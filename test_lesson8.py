#!/usr/bin/env python3

import unittest
from lesson8 import *


class TestHashTableMethods(unittest.TestCase):

    def test_hash_function(self):
        H = HashTable(17, 3)
        for i in ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]:
            for j in ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]:
                slot = H.hash_fun(i+j)
                self.assertTrue(slot >= 0)
                self.assertTrue(slot < H.size)
                # print("{} = {}".format(i+j, slot))
        for i in "ABCDEF":
            self.assertEqual(H.hash_fun([i]*6), 9)

    def test_seek_slot(self):
        H = HashTable(17, 3)
        # first found
        self.assertEqual(H.seek_slot("AAAAAA"), 9)
        H.slots[9] = "AAAAAA"
        H.slots[12] = "AAAAAA"
        H.slots[15] = "AAAAAA"
        # seek empty slot
        self.assertEqual(H.seek_slot("AAAAAA"), 1)
        H.slots[1] = "AAAAAA"
        H.slots[4] = "AAAAAA"
        H.slots[7] = "AAAAAA"
        H.slots[10] = "AAAAAA"
        H.slots[13] = "AAAAAA"
        H.slots[16] = "AAAAAA"
        self.assertEqual(H.seek_slot("AAAAAA"), 2)
        H.slots[2] = "AAAAAA"
        H.slots[5] = "AAAAAA"
        H.slots[8] = "AAAAAA"
        H.slots[11] = "AAAAAA"
        H.slots[14] = "AAAAAA"
        H.slots[0] = "AAAAAA"
        H.slots[3] = "AAAAAA"
        H.slots[6] = "AAAAAA"
        # full
        self.assertEqual(H.seek_slot("AAAAAA"), None)

    def test_put(self):
        H = HashTable(17, 3)
        self.assertEqual(H.put("AAAAAA"), 9)
        self.assertIsNotNone(H.put("abcdef"))
        for i in range(17):
            H.slots[i] = "filled"
        self.assertIsNone(H.put("AAAAAA"))

    def test_find(self):
        H = HashTable(17, 3)
        s1 = H.put("AAAAAA")
        self.assertEqual(s1, 9)
        self.assertEqual(s1, H.find("AAAAAA"))
        self.assertIsNone(H.find("BBBBBB"))

    def test_find2(self):
        H = HashTable(31, 13)
        sequence = "abcdefghijklmnopqrstuvwxyz12345"
        for elem in sequence:
            self.assertIsNotNone(H.put(elem))
        self.assertIsNone(H.find("12345"))
        sequence2 = ""
        for elem in sequence:
            slot = H.find(elem)
            self.assertIsNotNone(slot)
            sequence2 += H.slots[slot]
        self.assertEqual(sequence, sequence2)


if __name__ == '__main__':
    unittest.main()
