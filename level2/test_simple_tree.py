#!/usr/bin/env python3

import unittest
from simple_tree import *


class TestSimpleTreeMethods(unittest.TestCase):

    def test_AddChild(self):
        S = SimpleTree(None)
        self.assertEqual(S.GetAllNodes(), [])

        n1 = SimpleTreeNode(1, None)
        S.AddChild(None, n1)
        self.assertEqual(S.GetAllNodes(), [n1])
        self.assertIsNone(n1.Parent)
        self.assertEqual(S.Root, n1)

        # new root
        n2 = SimpleTreeNode(2, None)
        S.AddChild(None, n2)
        self.assertEqual(S.GetAllNodes(), [n2])
        self.assertEqual(S.Root, n2)

        S.AddChild(None, n1)
        S.AddChild(n1, n2)
        self.assertEqual(S.GetAllNodes(), [n1, n2])
        self.assertEqual(S.Root, n1)
        self.assertEqual(n2.Parent, n1)
        self.assertEqual(n1.Children, [n2])

        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(n1, n3)
        S.AddChild(n2, n4)
        self.assertEqual(S.GetAllNodes(), [n1, n2, n4, n3])
        self.assertEqual(n1.Children, [n2, n3])
        self.assertEqual(n3.Parent, n1)
        self.assertEqual(n2.Children, [n4])

    def test_DeleteNode(self):
        S = SimpleTree(None)
        n1 = SimpleTreeNode(1, None)
        n2 = SimpleTreeNode(2, None)
        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(None, n1)
        S.AddChild(n1, n2)
        S.AddChild(n2, n3)
        S.AddChild(n3, n4)
        S.DeleteNode(n3)
        self.assertEqual(S.GetAllNodes(), [n1, n2])
        S.DeleteNode(n2)
        self.assertEqual(S.GetAllNodes(), [n1])
        S.DeleteNode(n1)
        self.assertEqual(S.GetAllNodes(), [])
        self.assertEqual(n1.Children, [])
        self.assertIsNone(S.Root)

    def test_GetAllNodes(self):
        S = SimpleTree(None)
        self.assertEqual(S.GetAllNodes(), [])
        root = SimpleTreeNode(0, None)
        S.AddChild(None, root)
        n1 = SimpleTreeNode(1, None)
        S.AddChild(root, n1)
        n2 = SimpleTreeNode(2, None)
        S.AddChild(root, n2)
        n11 = SimpleTreeNode(11, None)
        n12 = SimpleTreeNode(12, None)
        S.AddChild(n1, n11)
        S.AddChild(n1, n12)
        n21 = SimpleTreeNode(21, None)
        n22 = SimpleTreeNode(22, None)
        S.AddChild(n2, n21)
        S.AddChild(n2, n22)
        self.assertEqual(S.GetAllNodes(), [root, n1, n11, n12, n2, n21, n22])

    def test_FindNodesByValue(self):
        S = SimpleTree(None)
        n1 = SimpleTreeNode(1, None)
        n2 = SimpleTreeNode(2, None)
        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(None, n1)
        S.AddChild(n1, n2)
        S.AddChild(n1, n3)
        S.AddChild(n2, n4)
        self.assertEqual(S.FindNodesByValue(1), [n1])
        self.assertEqual(S.FindNodesByValue(2), [n2])
        self.assertEqual(S.FindNodesByValue(3), [n3])
        self.assertEqual(S.FindNodesByValue(4), [n4])

        n33 = SimpleTreeNode(3, None)
        S.AddChild(n2, n33)
        self.assertEqual(S.FindNodesByValue(3), [n33, n3])

    def test_MoveNode(self):
        S = SimpleTree(None)
        n1 = SimpleTreeNode(1, None)
        n2 = SimpleTreeNode(2, None)
        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(None, n1)
        S.AddChild(n1, n2)
        S.AddChild(n2, n3)
        S.AddChild(n3, n4)
        self.assertEqual(len(n1.Children), 1)
        self.assertIsNone(n1.Parent)
        self.assertEqual(len(n2.Children), 1)
        self.assertEqual(n2.Parent, n1)
        self.assertEqual(len(n3.Children), 1)
        self.assertEqual(n3.Parent, n2)
        self.assertEqual(len(n4.Children), 0)
        self.assertEqual(n4.Parent, n3)
        S.MoveNode(n3, n1)
        self.assertEqual(len(n2.Children), 0)
        self.assertEqual(len(n1.Children), 2)
        self.assertEqual(len(n3.Children), 1)
        self.assertEqual(n3.Parent, n1)
        self.assertEqual(len(n4.Children), 0)
        self.assertEqual(n4.Parent, n3)

    def test_Count(self):
        S = SimpleTree(None)
        self.assertEqual(S.Count(), 0)

        n1 = SimpleTreeNode(1, None)
        n2 = SimpleTreeNode(2, None)
        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(None, n1)
        self.assertEqual(S.Count(), 1)

        S.AddChild(n1, n2)
        S.AddChild(n1, n3)
        S.AddChild(n2, n4)
        self.assertEqual(S.Count(), 4)

    def test_LeafCount(self):
        S = SimpleTree(None)
        self.assertEqual(S.LeafCount(), 0)

        n1 = SimpleTreeNode(1, None)
        n2 = SimpleTreeNode(2, None)
        n3 = SimpleTreeNode(3, None)
        n4 = SimpleTreeNode(4, None)
        S.AddChild(None, n1)
        self.assertEqual(S.LeafCount(), 1)

        S.AddChild(n1, n2)
        S.AddChild(n1, n3)
        S.AddChild(n2, n4)
        self.assertEqual(S.LeafCount(), 2)

    def testEvenTrees(self):
        S = SimpleTree(None)
        self.assertEqual(S.EvenTrees(), [])
        ns = []
        for i in range(11):
            n = SimpleTreeNode(i, None)
            ns.append(n)
        S.AddChild(None, ns[1])
        S.AddChild(ns[1], ns[2])
        S.AddChild(ns[1], ns[3])
        S.AddChild(ns[1], ns[6])
        S.AddChild(ns[2], ns[5])
        S.AddChild(ns[2], ns[7])
        S.AddChild(ns[3], ns[4])
        S.AddChild(ns[6], ns[8])
        S.AddChild(ns[8], ns[9])
        self.assertEqual(S.EvenTrees(), [])
        S.AddChild(ns[8], ns[10])
        self.assertEqual(S.EvenTrees(), [ns[1], ns[3], ns[1], ns[6]])

    def testEvenTrees2(self):
        S = SimpleTree(None)
        ns = []
        for i in range(10):
            n = SimpleTreeNode(i, None)
            ns.append(n)
        S.AddChild(None, ns[0])
        S.AddChild(ns[0], ns[1])
        S.AddChild(ns[0], ns[2])
        S.AddChild(ns[0], ns[3])
        S.AddChild(ns[1], ns[4])
        S.AddChild(ns[2], ns[6])
        S.AddChild(ns[3], ns[7])
        S.AddChild(ns[4], ns[5])
        S.AddChild(ns[7], ns[8])
        S.AddChild(ns[7], ns[9])
        self.assertEqual(S.EvenTrees(), [ns[1], ns[4], ns[0], ns[2], ns[0], ns[3]])

if __name__ == '__main__':
    unittest.main()
