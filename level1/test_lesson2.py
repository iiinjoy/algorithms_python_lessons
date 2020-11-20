#!/usr/bin/env python3

import unittest
from lesson2 import *


class TestLinkedList2Methods(unittest.TestCase):

    def test_find(self):
        L = LinkedList2()
        self.assertIsNone(L.find(42))
        n1 = Node(1)
        L.add_in_tail(n1)
        self.assertIsNone(L.find(42))
        self.assertEqual(L.find(1), n1)
        n2 = Node(2)
        n3 = Node(3)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        self.assertEqual(L.find(3), n3)
        self.assertEqual(L.find(2), n2)

    def test_find_all(self):
        L = LinkedList2()
        self.assertEqual(L.find_all(42), [])
        n1 = Node(1)
        n2 = Node(2)
        n31 = Node(3)
        n32 = Node(3)
        L.add_in_tail(n1)
        L.add_in_tail(n2)
        L.add_in_tail(n31)
        L.add_in_tail(n32)
        self.assertEqual(L.find_all(1), [n1])
        self.assertEqual(L.find_all(3), [n31, n32])

    def test_delete_nothing(self):
        L = LinkedList2()
        L.add_in_tail(Node(1))
        L.add_in_tail(Node(2))
        L.delete(42)
        self.assertEqual(L.head.value, 1)
        self.assertEqual(L.tail.value, 2)

    def test_delete_in_head(self):
        L = LinkedList2()
        L.add_in_tail(Node(1))
        L.add_in_tail(Node(2))
        L.add_in_tail(Node(3))
        L.delete(1)
        self.assertEqual(L.head.value, 2)
        self.assertIsNone(L.head.prev)
        self.assertEqual(L.head.next.value, 3)
        self.assertEqual(L.tail.value, 3)

    def test_delete_in_tail(self):
        L = LinkedList2()
        L.add_in_tail(Node(1))
        L.add_in_tail(Node(2))
        L.add_in_tail(Node(3))
        L.delete(3)
        self.assertEqual(L.head.value, 1)
        self.assertIsNone(L.tail.next)
        self.assertEqual(L.head.next.value, 2)
        self.assertEqual(L.tail.value, 2)

    def test_delete_in_middle(self):
        L = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        L.add_in_tail(n1)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        self.assertEqual(L.head, n1)
        self.assertEqual(L.tail, n3)
        L.delete(2)
        self.assertEqual(L.head, n1)
        self.assertEqual(L.tail, n3)
        self.assertEqual(L.head.next, n3)
        self.assertIsNone(L.head.prev)
        self.assertEqual(L.tail.prev, n1)
        self.assertIsNone(L.tail.next)

    def test_delete_all(self):
        L = LinkedList2()
        n1 = Node(5)
        n2 = Node(5)
        n3 = Node(5)
        L.add_in_tail(n1)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        L.delete(5, all=True)
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

    def test_delete_first_of_equals(self):
        L = LinkedList2()
        n1 = Node(5)
        n2 = Node(5)
        n3 = Node(5)
        L.add_in_tail(n1)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        L.delete(5, all=False)
        self.assertEqual(L.head, n2)
        self.assertEqual(L.tail, n3)
        self.assertIsNone(L.head.prev)
        self.assertIsNone(L.tail.next)

    def test_clean(self):
        L = LinkedList2()
        L.add_in_tail(Node(1))
        L.add_in_tail(Node(2))
        L.add_in_tail(Node(3))
        self.assertEqual(L.len(), 3)
        L.clean()
        self.assertEqual(L.len(), 0)
        self.assertIsNone(L.head)
        self.assertIsNone(L.tail)

    def test_len(self):
        L = LinkedList2()
        self.assertEqual(L.len(), 0)
        L.add_in_tail(Node(1))
        self.assertEqual(L.len(), 1)
        L.add_in_tail(Node(2))
        self.assertEqual(L.len(), 2)
        L.add_in_tail(Node(3))
        self.assertEqual(L.len(), 3)

    def test_insert_empty(self):
        L = LinkedList2()
        L.insert(None, Node(5))
        self.assertEqual(L.head, L.tail)
        self.assertEqual(L.head.value, 5)
        self.assertIsNone(L.head.next)
        self.assertIsNone(L.head.prev)

    def test_insert_in_middle(self):
        L = LinkedList2()
        L.insert(None, Node(1))
        n2 = Node(2)
        L.insert(None, n2)
        L.insert(None, Node(4))
        n3 = Node(3)
        L.insert(n2, n3)
        self.assertEqual(L.head.value, 1)
        self.assertEqual(L.tail.value, 4)
        self.assertEqual(L.head.next, n2)
        self.assertEqual(L.tail.prev, n3)

    def test_insert_in_tail(self):
        L = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        L.add_in_tail(n1)
        L.add_in_tail(n2)
        L.add_in_tail(n3)
        n4 = Node(4)
        L.insert(n3, n4)
        self.assertEqual(L.tail, n4)
        self.assertEqual(L.tail.prev, n3)
        self.assertEqual(n3.next, n4)
        self.assertEqual(L.len(), 4)

    def test_add_in_head(self):
        L = LinkedList2()
        L.add_in_head(Node(1))
        self.assertEqual(L.head, L.tail)
        self.assertEqual(L.head.value, 1)
        L.add_in_head(Node(0))
        self.assertEqual(L.head.value, 0)
        self.assertEqual(L.tail.value, 1)
        self.assertEqual(L.head.next, L.tail)
        self.assertEqual(L.tail.prev, L.head)
        self.assertIsNone(L.head.prev)
        self.assertIsNone(L.tail.next)

if __name__ == '__main__':
    unittest.main()
