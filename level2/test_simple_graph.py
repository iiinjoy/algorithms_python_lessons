#!/usr/bin/env python3

import unittest
from simple_graph import *


class TestSimpleGraphMethods(unittest.TestCase):

    def testAddVertex(self):
        size = 5
        G = SimpleGraph(size)
        G.AddVertex("0")
        self.assertIsNotNone(G.vertex[0])
        for v2 in range(size):
            self.assertFalse(G.IsEdge(0, v2))
            self.assertFalse(G.IsEdge(v2, 0))

    def testAddEdge(self):
        size = 5
        G = SimpleGraph(size)
        G.AddVertex("0")
        G.AddVertex("1")
        self.assertFalse(G.IsEdge(0, 1))
        self.assertFalse(G.IsEdge(1, 0))

        G.AddEdge(0, 1)
        self.assertTrue(G.IsEdge(0, 1))
        self.assertTrue(G.IsEdge(1, 0))

    def testRemoveEdge(self):
        size = 5
        G = SimpleGraph(size)
        G.AddVertex("0")
        G.AddVertex("1")
        G.AddEdge(0, 1)
        self.assertTrue(G.IsEdge(0, 1))
        self.assertTrue(G.IsEdge(1, 0))

        G.RemoveEdge(0, 1)
        self.assertFalse(G.IsEdge(0, 1))
        self.assertFalse(G.IsEdge(1, 0))

    def testRemoveVertex(self):
        size = 5
        G = SimpleGraph(size)
        G.AddVertex("0")
        G.AddVertex("1")
        G.AddVertex("2")
        G.AddVertex("3")
        G.AddEdge(0, 1)
        G.AddEdge(0, 3)
        G.AddEdge(1, 2)
        self.assertTrue(G.IsEdge(1, 0))
        self.assertFalse(G.IsEdge(2, 0))
        self.assertTrue(G.IsEdge(3, 0))
        self.assertTrue(G.IsEdge(2, 1))

        G.RemoveVertex(0)
        self.assertIsNone(G.vertex[0])
        self.assertFalse(G.IsEdge(1, 0))
        self.assertFalse(G.IsEdge(2, 0))
        self.assertFalse(G.IsEdge(3, 0))
        self.assertTrue(G.IsEdge(2, 1))

    def testDepthFirstSearch(self):
        size = 9
        G = SimpleGraph(size)
        for i in range(size):
            G.AddVertex(str(i))
        G.AddEdge(0, 7)
        G.AddEdge(1, 2)
        G.AddEdge(2, 3)
        G.AddEdge(3, 4)
        G.AddEdge(3, 5)
        G.AddEdge(4, 6)
        G.AddEdge(5, 7)
        G.AddEdge(6, 7)

        self.assertEqual(G.DepthFirstSearch(1, 8), [])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(1, 2)), ["1", "2"])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(1, 3)), ["1", "2", "3"])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(1, 5)), ["1", "2", "3", "5"])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(1, 7)), ["1", "2", "3", "4", "6", "7"])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(0, 4)), ["0", "7", "5", "3", "4"])
        self.assertEqual(G.toValueList(G.DepthFirstSearch(6, 5)), ["6", "4", "3", "5"])

    def testBreadthFirstSearch(self):
        size = 9
        G = SimpleGraph(size)
        for i in range(size):
            G.AddVertex(str(i))
        G.AddEdge(0, 7)
        G.AddEdge(1, 2)
        G.AddEdge(2, 3)
        G.AddEdge(3, 4)
        G.AddEdge(3, 5)
        G.AddEdge(4, 6)
        G.AddEdge(5, 7)
        G.AddEdge(6, 7)

        self.assertEqual(G.BreadthFirstSearch(1, 8), [])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(1, 2)), ["1", "2"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(1, 5)), ["1", "2", "3", "5"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(1, 7)), ["1", "2", "3", "5", "7"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(7, 4)), ["7", "6", "4"])

    def testBreadthFirstSearch2(self):
        size = 13
        G = SimpleGraph(size)
        for i in range(size):
            G.AddVertex(str(i))
        G.AddEdge(0, 1)
        G.AddEdge(1, 2)
        G.AddEdge(1, 3)
        G.AddEdge(2, 4)
        G.AddEdge(2, 5)
        G.AddEdge(3, 6)
        G.AddEdge(3, 7)
        G.AddEdge(4, 8)
        G.AddEdge(5, 9)
        G.AddEdge(8, 10)
        G.AddEdge(9, 11)
        G.AddEdge(10, 9)
        G.AddEdge(11, 12)

        self.assertEqual(G.toValueList(G.BreadthFirstSearch(0, 6)), ["0", "1", "3", "6"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(2, 11)), ["2", "5", "9", "11"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(2, 10)), ["2", "4", "8", "10"])
        self.assertEqual(G.toValueList(G.BreadthFirstSearch(10, 2)), ["10", "8", "4", "2"])

    def testWeakVertices(self):
        size = 3
        G = SimpleGraph(size)
        for i in range(size):
            G.AddVertex(str(i))

        G.AddEdge(0, 1)
        G.AddEdge(0, 2)
        G.AddEdge(1, 2)
        self.assertEqual(G.WeakVertices(), [])

    def testWeakVertices2(self):
        size = 9
        G = SimpleGraph(size)
        for i in range(size):
            G.AddVertex(str(i))
        G.AddEdge(0, 8)
        G.AddEdge(1, 2)
        G.AddEdge(1, 3)
        G.AddEdge(2, 3)
        G.AddEdge(2, 4)
        G.AddEdge(3, 4)
        G.AddEdge(3, 6)
        G.AddEdge(4, 5)
        G.AddEdge(5, 6)
        G.AddEdge(6, 7)
        G.AddEdge(6, 8)
        G.AddEdge(7, 8)

        self.assertEqual(G.toValueList(G.WeakVertices()), ["0", "5"])

if __name__ == '__main__':
    unittest.main()
