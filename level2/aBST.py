#!/usr/bin/env python3


class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size  # массив ключей

    def __LeftChildIndex(self, i):
        return 2 * i + 1

    def __RightChildIndex(self, i):
        return 2 * i + 2

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        i = 0
        while i < self.tree_size:
            if self.Tree[i] is None:
                return -i
            if self.Tree[i] == key:
                return i
            elif key < self.Tree[i]:
                i = self.__LeftChildIndex(i)
            elif key > self.Tree[i]:
                i = self.__RightChildIndex(i)
        return None  # не найден

    def AddKey(self, key):
        # добавляем ключ в массив
        i = self.FindKeyIndex(key)
        if i is not None:
            if i <= 0:
                index = -i
                self.Tree[index] = key
                return index
            else:
                return i
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
