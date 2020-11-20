#!/usr/bin/env python3

import unittest
from balancedBST import *


class TestBalancedBSTMethods(unittest.TestCase):

    def test_all(self):
        B = BalancedBST()
        # emptyTree
        B.GenerateTree([])
        self.assertIsNone(B.Root)
        self.assertTrue(B.IsBalanced(B.Root))

        # one-element tree
        B.GenerateTree([42])
        self.assertIsNotNone(B.Root)
        self.assertEqual(B.Root.NodeKey, 42)
        self.assertIsNone(B.Root.Parent)
        self.assertIsNone(B.Root.LeftChild)
        self.assertIsNone(B.Root.RightChild)
        self.assertEqual(B.Root.Level, 1)
        self.assertTrue(B.IsBalanced(B.Root))

        # [0..7]
        B.GenerateTree(list(range(0, 8)))
        self.assertIsNotNone(B.Root)
        self.assertEqual(B.Root.NodeKey, 4)
        self.assertIsNone(B.Root.Parent)
        self.assertIsNotNone(B.Root.LeftChild)
        self.assertEqual(B.Root.LeftChild.NodeKey, 2)
        self.assertEqual(B.Root.LeftChild.Level, 2)
        self.assertIsNotNone(B.Root.RightChild)
        self.assertEqual(B.Root.RightChild.NodeKey, 6)
        self.assertEqual(B.Root.RightChild.Level, 2)
        self.assertTrue(B.IsBalanced(B.Root))

        # [1, 2, 3, 3, 4]
        B.GenerateTree([4, 3, 3, 2, 1])
        self.assertIsNotNone(B.Root)
        self.assertEqual(B.Root.NodeKey, 3)
        self.assertIsNone(B.Root.Parent)
        self.assertIsNotNone(B.Root.LeftChild)
        self.assertEqual(B.Root.LeftChild.NodeKey, 2)
        self.assertEqual(B.Root.LeftChild.Level, 2)
        self.assertIsNotNone(B.Root.RightChild)
        self.assertEqual(B.Root.RightChild.NodeKey, 4)
        self.assertEqual(B.Root.RightChild.Level, 2)
        self.assertTrue(B.IsBalanced(B.Root))
        self.assertEqual(B.Root.RightChild.LeftChild.NodeKey, 3)
        self.assertIsNone(B.Root.RightChild.RightChild)

        # [1, 2, 4, 4, 4, 5]
        B.GenerateTree([1, 2, 4, 4, 4, 5])
        self.assertIsNotNone(B.Root)
        self.assertEqual(B.Root.NodeKey, 4)
        self.assertIsNone(B.Root.Parent)
        self.assertIsNotNone(B.Root.LeftChild)
        self.assertEqual(B.Root.LeftChild.NodeKey, 2)
        self.assertEqual(B.Root.LeftChild.Level, 2)
        self.assertIsNotNone(B.Root.RightChild)
        self.assertEqual(B.Root.RightChild.NodeKey, 4)
        self.assertEqual(B.Root.RightChild.Level, 2)
        self.assertFalse(B.IsBalanced(B.Root))
        self.assertEqual(B.Root.RightChild.RightChild.NodeKey, 5)
        self.assertEqual(B.Root.RightChild.RightChild.LeftChild.NodeKey, 4)
        # B.printTree(B.Root, 0)

if __name__ == '__main__':
    unittest.main()
