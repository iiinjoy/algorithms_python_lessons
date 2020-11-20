#!/usr/bin/env python3


class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    @staticmethod
    def __GenerateTreeRec(parent, sorted_arr, work_range, level):
        range_length = len(work_range)
        if range_length == 0:
            return None
        center_index = int(range_length / 2)
        # корректировка: ключ правого потомка должен быть больше или равен ключу родителя
        while center_index > 0 and sorted_arr[work_range[center_index-1]] == sorted_arr[work_range[center_index]]:
            center_index -= 1
        range_center = work_range[center_index]
        key = sorted_arr[range_center]
        bstnode = BSTNode(key, parent)
        bstnode.Level = level

        left_range = range(work_range[0], range_center)
        bstnode.LeftChild = BalancedBST.__GenerateTreeRec(bstnode, sorted_arr, left_range, level+1)

        right_range = range(range_center+1, work_range[0] + range_length)
        bstnode.RightChild = BalancedBST.__GenerateTreeRec(bstnode, sorted_arr, right_range, level+1)

        return bstnode

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a
        sorted_arr = a.copy()
        sorted_arr.sort()
        self.Root = BalancedBST.__GenerateTreeRec(None, sorted_arr, range(0, len(a)), 1)

    def IsBalanced(self, root_node):
        # сбалансировано ли дерево с корнем root_node
        def isBalancedRec(root_node):
            if root_node is None:
                return (True, 0)
            else:
                (leftBalanced, leftDepth) = isBalancedRec(root_node.LeftChild)
                (rightBalanced, rightDepth) = isBalancedRec(root_node.RightChild)
                maxD = leftDepth if leftDepth > rightDepth else rightDepth
                minD = leftDepth if leftDepth < rightDepth else rightDepth
                diff = maxD - minD
                balanced = leftBalanced and rightBalanced and (diff <= 1)
                return (balanced, maxD + 1)
        (balanced, _) = isBalancedRec(self.Root)
        return balanced

    def printTree(self, root_node, level):
        if root_node is None:
            return
        print("{}{}".format(" "*level, root_node.NodeKey))
        self.printTree(root_node.LeftChild, level+1)
        self.printTree(root_node.RightChild, level+1)
