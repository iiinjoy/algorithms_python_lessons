#!/usr/bin/env python3

import unittest
from lesson3 import *


class TestDynArrayMethods(unittest.TestCase):

    def test_insert(self):
        DA = DynArray()
        self.assertEqual(len(DA), 0)

        DA.insert(0, 3)
        self.assertEqual(len(DA), 1)
        self.assertEqual(DA[0], 3)

        DA.insert(0, 2)
        DA.insert(0, 1)
        self.assertEqual(DA[0], 1)
        self.assertEqual(DA[1], 2)
        self.assertEqual(DA[2], 3)

        DA.insert(3, 5)
        DA.insert(3, 4)
        self.assertEqual(DA[3], 4)
        self.assertEqual(DA[4], 5)

        for i in range(6, 17):
            DA.append(i)
        self.assertEqual(DA.count, 16)
        self.assertEqual(DA.capacity, 16)

        DA.insert(0, 0)
        self.assertEqual(DA.count, 17)
        self.assertEqual(DA.capacity, 32)
        for i in range(DA.count):
            self.assertEqual(DA[i], i)

        DA.insert(17, 17)
        self.assertEqual(DA.count, 18)

        with self.assertRaises(IndexError):
            DA.insert(-1, -1)
        with self.assertRaises(IndexError):
            DA.insert(19, 19)

    def test_delete(self):
        DA = DynArray()
        with self.assertRaises(IndexError):
            DA.delete(0)

        for i in range(16):
            DA.append(i)
        self.assertEqual(DA.count, 16)
        self.assertEqual(DA.capacity, 16)

        with self.assertRaises(IndexError):
            DA.delete(16)

        DA.delete(0)
        self.assertEqual(DA.count, 15)
        for i in range(DA.count):
            self.assertEqual(DA[i], i+1)

        DA.insert(0, 0)
        self.assertEqual(DA.count, 16)
        self.assertEqual(DA.capacity, 16)
        DA.append(16)
        self.assertEqual(DA.count, 17)
        self.assertEqual(DA.capacity, 32)
        DA.delete(16)
        self.assertEqual(DA.count, 16)
        self.assertEqual(DA.capacity, 32)

        DA.delete(0)
        self.assertEqual(DA.count, 15)
        self.assertEqual(DA.capacity, 21)

        for _ in range(4):
            DA.delete(0)
        self.assertEqual(DA.count, 11)
        self.assertEqual(DA.capacity, 21)

        DA.delete(0)
        self.assertEqual(DA.count, 10)
        self.assertEqual(DA.capacity, 16)

        for _ in range(DA.count):
            DA.delete(0)
        self.assertEqual(DA.count, 0)
        self.assertEqual(DA.capacity, 16)

if __name__ == '__main__':
    unittest.main()
