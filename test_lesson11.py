#!/usr/bin/env python3

import unittest
from lesson11 import *


class TestPowerSetMethods(unittest.TestCase):

    def test_size(self):
        p = PowerSet()
        self.assertEqual(p.size(), 0)
        p.put("123")
        self.assertEqual(p.size(), 1)
        p.put("123")
        self.assertEqual(p.size(), 1)
        p.put("1233")
        self.assertEqual(p.size(), 2)

    def test_put(self):
        p = PowerSet()
        self.assertEqual(p.size(), 0)
        p.put("42")
        self.assertEqual(p.size(), 1)
        p.put("42")
        self.assertEqual(p.size(), 1)
        p.put("41")
        self.assertEqual(p.size(), 2)
        p.put("41")
        self.assertEqual(p.size(), 2)

    def test_remove(self):
        p = PowerSet()
        self.assertFalse(p.remove("42"))
        p.put("42")
        self.assertEqual(p.size(), 1)
        self.assertTrue(p.remove("42"))
        self.assertEqual(p.size(), 0)
        self.assertFalse(p.remove("42"))
        self.assertEqual(p.size(), 0)
        p.put("1")
        p.put("1")
        self.assertEqual(p.size(), 1)
        self.assertTrue(p.remove("1"))
        self.assertFalse(p.remove("1"))
        self.assertFalse(p.get("42"))
        self.assertFalse(p.get("1"))
        self.assertEqual(p.size(), 0)

        for i in range(20000):
            p.put(str(i))
        self.assertEqual(p.size(), 20000)
        for i in range(20000):
            self.assertTrue(p.get(str(i)))
        for i in range(20000):
            self.assertTrue(p.remove(str(i)))
            self.assertFalse(p.remove(str(i)))
        self.assertEqual(p.size(), 0)
        for i in range(20000):
            self.assertFalse(p.get(str(i)))

    def test_intersection(self):
        set1 = PowerSet()
        set1.put("1")
        set1.put("2")
        set1.put("3")

        set2 = PowerSet()
        set2.put("4")
        set2.put("5")
        set2.put("6")

        set3 = set1.intersection(set2)
        self.assertEqual(set3.size(), 0)

        set1.put("4")
        set2.put("3")
        set4 = set1.intersection(set2)
        self.assertEqual(set4.size(), 2)
        self.assertTrue(set4.get("3"))
        self.assertTrue(set4.get("4"))

    def test_union(self):
        set1 = PowerSet()
        set2 = PowerSet()

        set3 = set1.union(set2)
        self.assertEqual(set3.size(), 0)

        set1.put("1")
        set1.put("2")
        set1.put("3")

        set2.put("3")
        set2.put("4")
        set2.put("5")
        set4 = set1.union(set2)
        self.assertEqual(set4.size(), 5)
        self.assertTrue(set4.get("1"))
        self.assertTrue(set4.get("2"))
        self.assertTrue(set4.get("3"))
        self.assertTrue(set4.get("4"))
        self.assertTrue(set4.get("5"))

    def test_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        # 0 - 0
        set3 = set1.difference(set2)
        self.assertEqual(set3.size(), 0)

        # 3 - 0
        set1.put("1")
        set1.put("2")
        set1.put("3")
        set4 = set1.difference(set2)
        self.assertEqual(set4.size(), 3)

        # 3 - 2
        set2.put("1")
        set2.put("2")
        set5 = set1.difference(set2)
        self.assertEqual(set5.size(), 1)
        self.assertFalse(set5.get("1"))
        self.assertFalse(set5.get("2"))
        self.assertTrue(set5.get("3"))

        # 3 - 3
        set2.put("3")
        set6 = set1.difference(set2)
        self.assertEqual(set6.size(), 0)

    def test_issubset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        # empty in empty
        self.assertTrue(set1.issubset(set2))

        # empty in non-empty
        set1.put("1")
        set1.put("2")
        set1.put("3")
        self.assertTrue(set1.issubset(set2))

        # {4,5,6} not in {1,2,3}
        set2.put("4")
        set2.put("5")
        set2.put("6")
        self.assertFalse(set1.issubset(set2))

        # {2,3} in {1,2,3}
        set3 = PowerSet()
        set3.put("2")
        set3.put("3")
        self.assertTrue(set1.issubset(set3))

if __name__ == '__main__':
    unittest.main()
