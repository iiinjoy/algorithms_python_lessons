#!/usr/bin/env python3

import unittest
from lesson1 import *


class TestLinkedListMethods(unittest.TestCase):

    def test_delete_1(self):
        L1 = LinkedList()
        L1.add_in_tail(Node(42))
        self.assertEqual(L1.head, L1.tail)
        self.assertEqual(L1.head.value, 42)
        L1.delete(42)
        self.assertIsNone(L1.head)
        self.assertIsNone(L1.tail)

    def test_delete_nothing(self):
        L1 = LinkedList()
        L1.add_in_tail(Node(1))
        self.assertEqual(L1.head, L1.tail)
        self.assertEqual(L1.head.value, 1)
        L1.delete(42)
        self.assertEqual(L1.head, L1.tail)
        self.assertEqual(L1.head.value, 1)
        self.assertIsNone(L1.head.next)

    def test_delete_in_head(self):
        L2 = LinkedList()
        L2.add_in_tail(Node(1))
        L2.add_in_tail(Node(2))
        self.assertEqual(L2.head.value, 1)
        self.assertEqual(L2.tail.value, 2)
        L2.delete(1)
        self.assertEqual(L2.head, L2.tail)
        self.assertEqual(L2.head.value, 2)
        self.assertIsNone(L2.head.next)

    def test_delete_in_tail(self):
        L2 = LinkedList()
        L2.add_in_tail(Node(1))
        L2.add_in_tail(Node(2))
        self.assertEqual(L2.head.value, 1)
        self.assertEqual(L2.tail.value, 2)
        L2.delete(2)
        self.assertEqual(L2.head, L2.tail)
        self.assertEqual(L2.head.value, 1)
        self.assertIsNone(L2.head.next)

    def test_delete_in_middle(self):
        L3 = LinkedList()
        L3.add_in_tail(Node(1))
        L3.add_in_tail(Node(2))
        L3.add_in_tail(Node(3))
        self.assertEqual(L3.head.value, 1)
        self.assertEqual(L3.head.next.value, 2)
        self.assertEqual(L3.tail.value, 3)
        L3.delete(2)
        self.assertEqual(L3.head.value, 1)
        self.assertEqual(L3.head.next, L3.tail)
        self.assertEqual(L3.tail.value, 3)
        self.assertIsNone(L3.tail.next)

    def test_delete_all(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n53 = Node(5)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n53)
        L.delete(5, all=True)
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

    def test_delete_first(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n53 = Node(5)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n53)
        L.delete(5, all=False)
        self.assertEqual(L.head, n52)
        self.assertEqual(L.tail, n53)
        self.assertEqual(L.head.next, n53)
        self.assertIsNone(L.tail.next)

    def test_clean(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n53 = Node(5)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n53)
        L.clean()
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

    def test_find_all(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n42 = Node(42)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n42)
        self.assertEqual(L.find_all(5), [n51, n52])

    def test_find_all_nothing(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n53 = Node(5)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n53)
        self.assertEqual(L.find_all(42), [])

    def test_find_all_empty(self):
        L = LinkedList()
        self.assertEqual(L.find_all(42), [])

    def test_len(self):
        L = LinkedList()
        self.assertEqual(L.len(), 0)
        n51 = Node(5)
        n52 = Node(5)
        n42 = Node(42)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.add_in_tail(n42)
        self.assertEqual(L.len(), 3)

    def test_insert_middle(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n42 = Node(42)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.insert(n51, n42)
        self.assertEqual(L.head, n51)
        self.assertEqual(L.head.next, n42)
        self.assertEqual(L.head.next.next, n52)
        self.assertEqual(L.tail, n52)

    def test_insert_last(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n42 = Node(42)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.insert(n52, n42)
        self.assertEqual(L.head, n51)
        self.assertEqual(L.head.next, n52)
        self.assertEqual(L.head.next.next, n42)
        self.assertEqual(L.tail, n42)

    def test_insert_after_none(self):
        L = LinkedList()
        n51 = Node(5)
        n52 = Node(5)
        n42 = Node(42)
        L.add_in_tail(n51)
        L.add_in_tail(n52)
        L.insert(None, n42)
        self.assertEqual(L.head, n42)
        self.assertEqual(L.head.next, n51)
        self.assertEqual(L.head.next.next, n52)
        self.assertEqual(L.tail, n52)

if __name__ == '__main__':
    unittest.main()
