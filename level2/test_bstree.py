#!/usr/bin/env python3

import unittest
from bstree import *


class TestBSTMethods(unittest.TestCase):

    def test_FindNodeByKey(self):
        B = BST(None)
        found = B.FindNodeByKey(0)
        self.assertIsNone(found.Node)
        self.assertFalse(found.NodeHasKey)

        ok = B.AddKeyValue(2, "2")
        self.assertTrue(ok)

        FL = B.FindNodeByKey(1)
        self.assertFalse(FL.NodeHasKey)
        self.assertIsNotNone(FL.Node)
        self.assertTrue(FL.ToLeft)

        FR = B.FindNodeByKey(3)
        self.assertFalse(FR.NodeHasKey)
        self.assertIsNotNone(FR.Node)
        self.assertFalse(FR.ToLeft)

        found = B.FindNodeByKey(2)
        self.assertTrue(found.NodeHasKey)
        self.assertIsNotNone(found.Node)
        self.assertEqual(found.Node.NodeKey, 2)
        self.assertEqual(found.Node.NodeValue, "2")

    def test_AddKeyValue(self):
        B = BST(None)
        not_found = B.FindNodeByKey(2)
        self.assertIsNone(not_found.Node)
        self.assertFalse(not_found.NodeHasKey)

        ok = B.AddKeyValue(2, "2")
        self.assertTrue(ok)
        found2 = B.FindNodeByKey(2)
        self.assertTrue(found2.NodeHasKey)
        self.assertIsNotNone(found2.Node)
        self.assertEqual(found2.Node.NodeKey, 2)
        self.assertEqual(found2.Node.NodeValue, "2")

        ok = B.AddKeyValue(1, "1")
        self.assertTrue(ok)
        found1 = B.FindNodeByKey(1)
        self.assertTrue(found1.NodeHasKey)
        self.assertIsNotNone(found1.Node)
        self.assertEqual(found1.Node.NodeKey, 1)
        self.assertEqual(found1.Node.NodeValue, "1")
        self.assertIsNotNone(found1.Node.Parent)
        self.assertEqual(found1.Node.Parent.NodeKey, 2)
        self.assertEqual(found1.Node.Parent.LeftChild, found1.Node)
        self.assertIsNone(found1.Node.Parent.RightChild)

        ok = B.AddKeyValue(3, "3")
        self.assertTrue(ok)
        found3 = B.FindNodeByKey(3)
        self.assertTrue(found3.NodeHasKey)
        self.assertIsNotNone(found3.Node)
        self.assertEqual(found3.Node.NodeKey, 3)
        self.assertEqual(found3.Node.NodeValue, "3")
        self.assertIsNotNone(found3.Node.Parent)
        self.assertEqual(found3.Node.Parent.NodeKey, 2)
        self.assertEqual(found3.Node.Parent.RightChild, found3.Node)

        ok = B.AddKeyValue(2, "42")
        self.assertFalse(ok)
        self.assertEqual(B.Root.NodeKey, 2)
        self.assertEqual(B.Root.NodeValue, "2")

    def test_FinMinMax(self):
        B = BST(None)
        for i in [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]:
            B.AddKeyValue(i, str(i))
        MaxInRoot = B.FinMinMax(None, FindMax=True)
        self.assertIsNotNone(MaxInRoot)
        self.assertEqual(MaxInRoot.NodeKey, 15)

        MinInRoot = B.FinMinMax(None, FindMax=False)
        self.assertIsNotNone(MinInRoot)
        self.assertEqual(MinInRoot.NodeKey, 1)

        findL = B.FindNodeByKey(4)

        MaxInLeft = B.FinMinMax(findL.Node, FindMax=True)
        self.assertIsNotNone(MaxInLeft)
        self.assertEqual(MaxInLeft.NodeKey, 7)

        MinInLeft = B.FinMinMax(findL.Node, FindMax=False)
        self.assertIsNotNone(MinInLeft)
        self.assertEqual(MinInLeft.NodeKey, 1)

        findR = B.FindNodeByKey(12)

        MaxInRight = B.FinMinMax(findR.Node, FindMax=True)
        self.assertIsNotNone(MaxInRight)
        self.assertEqual(MaxInRight.NodeKey, 15)

        MinInRight = B.FinMinMax(findR.Node, FindMax=False)
        self.assertIsNotNone(MinInRight)
        self.assertEqual(MinInRight.NodeKey, 9)

    def test_Count(self):
        B = BST(None)
        self.assertEqual(B.Count(), 0)
        for i in range(10):
            B.AddKeyValue(i, str(i))
        self.assertEqual(B.Count(), 10)

    def test_DeleteNodeByKey(self):
        B = BST(None)
        for i in [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]:
            B.AddKeyValue(i, str(i))

        def f_key(acc, bstnode):
            acc.append(bstnode.NodeKey)
            return acc
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15])
        self.assertEqual(B.Count(), 15)

        self.assertFalse(B.DeleteNodeByKey(42))
        self.assertEqual(B.Count(), 15)

        # delete Leaf node
        self.assertTrue(B.DeleteNodeByKey(15))
        self.assertEqual(B.Count(), 14)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13])

        # delete root node
        self.assertTrue(B.DeleteNodeByKey(8))
        self.assertEqual(B.Count(), 13)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [9, 4, 2, 1, 3, 6, 5, 7, 12, 10, 11, 14, 13])

        # delete node with RightChild
        self.assertTrue(B.DeleteNodeByKey(10))
        self.assertEqual(B.Count(), 12)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [9, 4, 2, 1, 3, 6, 5, 7, 12, 11, 14, 13])

        # delete node with LeftChild
        self.assertTrue(B.DeleteNodeByKey(14))
        self.assertEqual(B.Count(), 11)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [9, 4, 2, 1, 3, 6, 5, 7, 12, 11, 13])

        # delete not-root full node
        self.assertTrue(B.DeleteNodeByKey(4))
        self.assertEqual(B.Count(), 10)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [9, 5, 2, 1, 3, 6, 7, 12, 11, 13])

        # delete all
        for i in node_keys:
            self.assertTrue(B.DeleteNodeByKey(i))
        self.assertEqual(B.Count(), 0)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [])
        self.assertIsNone(B.Root)

        # another test add & delete
        for i in range(10):
            B.AddKeyValue(i, str(i))
        self.assertEqual(B.Count(), 10)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        for i in range(5):
            self.assertTrue(B.DeleteNodeByKey(i))
        self.assertEqual(B.Count(), 5)
        node_keys = BST.FoldTree(f_key, [], B.Root)
        self.assertEqual(node_keys, [5, 6, 7, 8, 9])

    def test_WideAllNodes(self):
        B = BST(None)
        self.assertEqual(B.WideAllNodes(), [])

        keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        for i in keys:
            B.AddKeyValue(i, str(i))
        wide_nodes = B.WideAllNodes()
        wide_keys = []
        for node in wide_nodes:
            wide_keys.append(node.NodeKey)
        self.assertEqual(keys, wide_keys)

    def test_DeepAllNodes(self):
        B = BST(None)
        self.assertEqual(B.DeepAllNodes(0), [])

        def f_node(acc, bstnode):
            acc.append(bstnode)
            return acc
        keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        for i in keys:
            B.AddKeyValue(i, str(i))

        # test pre-order
        fold_pre_order_nodes = BST.FoldTree(f_node, [], B.Root)
        pre_order_nodes = B.DeepAllNodes(2)
        self.assertEqual(fold_pre_order_nodes, pre_order_nodes)

        # test in-order
        in_order_nodes = B.DeepAllNodes(0)
        in_order_keys = []
        for node in in_order_nodes:
            in_order_keys.append(node.NodeKey)
        self.assertEqual(in_order_keys, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

        # test post-order
        post_order_nodes = B.DeepAllNodes(1)
        post_order_keys = []
        for node in post_order_nodes:
            post_order_keys.append(node.NodeKey)
        self.assertEqual(post_order_keys, [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8])

if __name__ == '__main__':
    unittest.main()
