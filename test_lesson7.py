#!/usr/bin/env python3

import unittest
from lesson7 import *


class TestOrderedListMethods(unittest.TestCase):

    def test_compare(self):
        L = OrderedList(asc=True)
        self.assertEqual(L.compare(42, 42), 0)
        self.assertEqual(L.compare(1, 2), -1)
        self.assertEqual(L.compare(2, 1), 1)

    def test_add_ascending(self):
        L = OrderedList(asc=True)
        L.add(42)
        self.assertEqual(L.get_all()[0].value, 42)
        self.assertIsNotNone(L.head)
        self.assertIsNotNone(L.tail)
        L.add(43)
        self.assertIsNotNone(L.head)
        self.assertIsNotNone(L.tail)
        self.assertEqual(len(L.get_all()), 2)
        self.assertEqual(L.head.value, 42)
        self.assertEqual(L.tail.value, 43)
        L.add(43)
        self.assertEqual(len(L.get_all()), 3)
        self.assertEqual(L.head.next.next.value, 43)
        self.assertEqual(L.tail.prev.prev.value, 42)
        L.add(44)
        self.assertEqual(len(L.get_all()), 4)
        self.assertEqual(L.head.next.next.next.value, 44)
        self.assertEqual(L.tail.prev.prev.prev.value, 42)
        L.add(41)
        self.assertEqual(len(L.get_all()), 5)
        self.assertEqual(L.head.value, 41)
        self.assertEqual(L.head.next.value, 42)
        self.assertIsNone(L.head.prev)

    def test_add_descending(self):
        L = OrderedList(asc=False)
        L.add(3)
        L.add(2)
        L.add(4)
        L.add(1)
        L.add(5)
        self.assertEqual(len(L.get_all()), 5)
        self.assertEqual(L.head.value, 5)
        self.assertEqual(L.tail.value, 1)
        self.assertEqual(L.head.next.value, 4)
        self.assertEqual(L.head.next.next.value, 3)
        self.assertEqual(L.head.next.next, L.tail.prev.prev)

    def test_delete(self):
        L = OrderedList(asc=True)
        # delete empty
        L.delete(42)

        L.add(1)
        L.add(2)
        L.add(3)
        L.add(4)
        L.add(5)

        # delete head
        L.delete(1)
        self.assertEqual(L.head.value, 2)
        self.assertIsNone(L.head.prev)
        self.assertEqual(len(L.get_all()), 4)

        # delete tail
        L.delete(5)
        self.assertEqual(L.tail.value, 4)
        self.assertIsNone(L.tail.next)
        self.assertEqual(len(L.get_all()), 3)

        # delete middle
        L.delete(3)
        self.assertEqual(L.head.value, 2)
        self.assertEqual(L.tail.value, 4)
        self.assertEqual(L.head.next, L.tail)
        self.assertEqual(L.tail.prev, L.head)
        self.assertEqual(len(L.get_all()), 2)
        self.assertEqual(L.len(), 2)

        # delete rest
        L.delete(4)
        self.assertEqual(L.head.value, 2)
        self.assertEqual(L.tail.value, 2)
        L.delete(2)
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

        # delete on descending
        L.clean(asc=False)
        L.add(5)
        L.add(4)
        L.add(3)
        L.add(2)
        L.add(1)
        L.delete(4)
        self.assertEqual(len(L.get_all()), 4)
        self.assertEqual(L.head.next.value, 3)
        self.assertEqual(L.head.next.prev.value, 5)
        L.delete(42)  # nothing
        self.assertEqual(len(L.get_all()), 4)

        # delete multiple
        L.clean(asc=False)
        for _ in range(5):
            L.add(42)
        for _ in range(5):
            L.add(12)
        self.assertEqual(L.len(), 10)
        self.assertEqual(L.head.value, 42)
        self.assertEqual(L.tail.value, 12)
        L.delete(42)
        L.delete(42)
        L.delete(42)
        L.delete(42)
        L.delete(42)
        self.assertEqual(L.len(), 5)
        self.assertEqual(L.head.value, 12)
        self.assertEqual(L.tail.value, 12)
        L.delete(12)
        L.delete(12)
        L.delete(12)
        L.delete(12)
        L.delete(12)
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

    def test_len(self):
        L = OrderedList(asc=True)
        L.add(1)
        L.add(2)
        L.add(3)
        self.assertEqual(len(L.get_all()), L.len())
        self.assertEqual(3, L.len())

    def test_find(self):
        L = OrderedList(asc=True)
        for i in range(10):
            L.add(i)
        self.assertIsNone(L.find(42))
        for i in range(10):
            self.assertEqual(L.find(i).value, i)
        # descending
        L.clean(asc=False)
        for i in range(10):
            L.add(i)
        self.assertEqual(L.head.value, 9)
        for i in range(10):
            self.assertEqual(L.find(i).value, i)

    def test_add_and_del_complex(self):
        L = OrderedList(asc=True)
        L.add(123)
        L.add(123)
        L.add(124)
        L.add(0)
        self.assertEqual(L.len(), 4)
        L.delete(123)
        L.delete(123)
        self.assertEqual(L.len(), 2)
        self.assertEqual(L.head.value, 0)
        self.assertEqual(L.tail.value, 124)
        self.assertEqual(L.head.next, L.tail)
        self.assertEqual(L.tail.prev, L.head)
        self.assertIsNone(L.head.prev)
        self.assertIsNone(L.tail.next)
        L.add(0)
        L.add(0)
        L.add(0)
        self.assertEqual(L.len(), 5)
        L.add(124)
        self.assertEqual(L.len(), 6)
        self.assertEqual(L.tail.prev.value, 124)


class TestOrderedStringListMethods(unittest.TestCase):

    def test_compare(self):
        L = OrderedStringList(asc=True)
        self.assertEqual(L.compare("123", "    123    "), 0)
        self.assertEqual(L.compare("  124", "    123    "), 1)
        self.assertEqual(L.compare("  12", "    123    "), -1)
        self.assertEqual(L.compare("  1", "     "), 1)

    def test_all(self):
        L = OrderedStringList(asc=True)
        # add & find
        L.add("123")
        L.add("   123   ")
        L.add("  124  ")
        L.add("  000  ")
        self.assertEqual(L.len(), 4)
        self.assertEqual(L.head.value, "  000  ")
        self.assertEqual(L.find("123").value, "123")
        self.assertEqual(L.find("000").value, "  000  ")

        # delete
        L.delete("123")
        L.delete("                 123")
        self.assertEqual(L.len(), 2)
        self.assertEqual(L.head.value.strip(), "000")
        L.add("    ")
        L.add("   ")
        L.add("     ")
        self.assertEqual(L.len(), 5)

if __name__ == '__main__':
    unittest.main()
