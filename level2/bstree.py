#!/usr/bin/env python3


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def hasLeft(self):
        return self.LeftChild is not None

    def hasRight(self):
        return self.RightChild is not None

    def isFullNode(self):
        return self.hasLeft() and self.hasRight()

    def isLeafNode(self):
        return not (self.hasLeft() or self.hasRight())


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        node = self.Root
        bstfind = BSTFind()
        while node is not None:
            if node.NodeKey == key:
                bstfind.Node = node
                bstfind.NodeHasKey = True
                return bstfind
            elif key < node.NodeKey:
                if node.LeftChild is None:
                    bstfind.Node = node
                    bstfind.NodeHasKey = False
                    bstfind.ToLeft = True
                    return bstfind
                else:
                    node = node.LeftChild
            elif key > node.NodeKey:
                if node.RightChild is None:
                    bstfind.Node = node
                    bstfind.NodeHasKey = False
                    bstfind.ToLeft = False
                    return bstfind
                else:
                    node = node.RightChild
        return bstfind

    def AddKeyValue(self, key, val):
        bstfind = self.FindNodeByKey(key)
        if bstfind.NodeHasKey:
            return False  # если ключ уже есть
        parent = bstfind.Node
        node = BSTNode(key, val, parent)
        if parent is None:
            self.Root = node
        else:
            if bstfind.ToLeft:
                parent.LeftChild = node
            else:
                parent.RightChild = node
        return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        node = FromNode if FromNode is not None else self.Root
        if node is None:
            return None
        child = node.RightChild if FindMax else node.LeftChild
        if child is None:
            return node
        return self.FinMinMax(child, FindMax)

    def __RemoveLeafNodeOrWithOneChild(self, node):
        child = node.RightChild if node.hasRight() else node.LeftChild
        if child is not None:
            child.Parent = node.Parent
        if node.Parent is not None:
            if node.Parent.LeftChild is node:
                # left-side
                node.Parent.LeftChild = child
            else:
                # right-side
                node.Parent.RightChild = child
            node.Parent = None
        else:
            # deleted Root
            self.Root = child
        node.LeftChild = None
        node.RightChild = None

    def __ReplaceNode(self, node, new_node):
        new_node.LeftChild = node.LeftChild
        new_node.RightChild = node.RightChild
        new_node.Parent = node.Parent
        if node.Parent is not None:
            if node.Parent.LeftChild is node:
                # left-side
                node.Parent.LeftChild = new_node
            else:
                # right-side
                node.Parent.RightChild = new_node
            node.Parent = None
        else:
            # deleted Root
            self.Root = new_node
        if new_node.hasLeft():
            new_node.LeftChild.Parent = new_node
        if new_node.hasRight():
            new_node.RightChild.Parent = new_node
        node.LeftChild = None
        node.RightChild = None

    @staticmethod
    def FoldTree(f, acc, root_node):
        if root_node is None:
            return acc
        acc1 = f(acc, root_node)
        if root_node.hasLeft():
            acc1 = BST.FoldTree(f, acc1, root_node.LeftChild)
        if root_node.hasRight():
            acc1 = BST.FoldTree(f, acc1, root_node.RightChild)
        return acc1

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        bstfind = self.FindNodeByKey(key)
        if not bstfind.NodeHasKey:
            return False  # если узел не найден
        node = bstfind.Node
        if node.isFullNode():
            MinNode = self.FinMinMax(node.RightChild, FindMax=False)
            self.__RemoveLeafNodeOrWithOneChild(MinNode)
            self.__ReplaceNode(node, MinNode)
        else:
            self.__RemoveLeafNodeOrWithOneChild(node)
        return True

    def Count(self):
        # количество узлов в дереве
        def f(acc, x):
            return acc + 1
        return BST.FoldTree(f, 0, self.Root)

    def WideAllNodes(self):
        def children(node):
            if node is None:
                return []
            result = []
            if node.hasLeft():
                result.append(node.LeftChild)
            if node.hasRight():
                result.append(node.RightChild)
            return result

        def WideAllNodesRec(acc, curr_level_nodes):
            if len(curr_level_nodes) == 0:
                return acc
            next_level_nodes = []
            for node in curr_level_nodes:
                next_level_nodes.extend(children(node))
            acc.extend(curr_level_nodes)
            return WideAllNodesRec(acc, next_level_nodes)

        if self.Root is None:
            return []
        return WideAllNodesRec([], [self.Root])

    def DeepAllNodes(self, order):
        def DeepAllNodesRec(node):
            if node is None:
                return []
            result = []
            if order == 2:  # pre-order
                result.append(node)
            result.extend(DeepAllNodesRec(node.LeftChild))
            if order == 0:  # in-order
                result.append(node)
            result.extend(DeepAllNodesRec(node.RightChild))
            if order == 1:  # post-order
                result.append(node)
            return result
        return DeepAllNodesRec(self.Root)
