#!/usr/bin/env python3


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
        else:
            if self.Root == NodeToDelete:
                self.Root = None
        NodeToDelete.Parent = None

    @staticmethod
    def FoldTree(f, acc, root_node):
        if root_node is None:
            return acc
        acc1 = f(acc, root_node)
        for elem in root_node.Children:
            acc1 = SimpleTree.FoldTree(f, acc1, elem)
        return acc1

    def GetAllNodes(self):
        def f(acc, x):
            acc.append(x)
            return acc
        return SimpleTree.FoldTree(f, [], self.Root)

    def FindNodesByValue(self, val):
        def f(acc, x):
            if x.NodeValue == val:
                acc.append(x)
            return acc
        return SimpleTree.FoldTree(f, [], self.Root)

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        if NewParent is None:
            self.Root = OriginalNode
        else:
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

    def Count(self):
        def f(acc, x):
            return acc + 1
        return SimpleTree.FoldTree(f, 0, self.Root)

    def LeafCount(self):
        def f(acc, x):
            if len(x.Children) == 0:
                return acc + 1
            return acc
        return SimpleTree.FoldTree(f, 0, self.Root)

    @staticmethod
    def CountSubTree(node):
        def f(acc, x):
            return acc + 1
        return SimpleTree.FoldTree(f, 0, node)

    def EvenTrees(self):
        def isEven(num):
            return (num % 2) == 0

        def EvenTreesRec(node, parent):
            if len(node.Children) == 0:
                return []
            edges_to_remove = []
            count = SimpleTree.CountSubTree(node)
            if isEven(count) and parent is not None:
                edges_to_remove.append((parent, node))
            for c in node.Children:
                edges_to_remove.extend(EvenTreesRec(c, node))
            return edges_to_remove

        count = self.Count()
        if not isEven(count) or count == 0:
            return []

        edge_list = EvenTreesRec(self.Root, None)
        result = []
        for e in edge_list:
            (n1, n2) = e
            result.append(n1)
            result.append(n2)
        return result
