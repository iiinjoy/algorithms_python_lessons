#!/usr/bin/env python3


class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    @staticmethod
    def LeftChildIndex(i):
        return 2 * i + 1

    @staticmethod
    def RightChildIndex(i):
        return 2 * i + 2

    @staticmethod
    def ParentIndex(i):
        return int((i - 1) / 2)

    @staticmethod
    def SortTopDown(parent, heap):
        left = Heap.LeftChildIndex(parent)
        right = Heap.RightChildIndex(parent)
        if right >= len(heap):
            return
        children = []
        if heap[left] is not None:
            children.append((heap[left], 'L', left))
        if heap[right] is not None:
            children.append((heap[right], 'R', right))
        children.sort()
        if len(children) > 0:
            (_, _, child) = children[-1]
            if heap[child] > heap[parent]:
                (heap[child], heap[parent]) = (heap[parent], heap[child])
                Heap.SortTopDown(child, heap)

    @staticmethod
    def SortBottonUp(child, heap):
        if child == 0:
            return
        parent = Heap.ParentIndex(child)
        if heap[parent] < heap[child]:
            (heap[parent], heap[child]) = (heap[child], heap[parent])
            Heap.SortBottonUp(parent, heap)

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        arr_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * arr_size
        for elem in a:
            self.Add(elem)

    @staticmethod
    def GetFilledSize(heap):
        filled = 0
        for elem in heap:
            if elem is None:
                break
            else:
                filled += 1
        return filled

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        filled = Heap.GetFilledSize(self.HeapArray)
        if filled == 0:
            return -1  # если куча пуста
        maxElem = self.HeapArray[0]
        if filled > 1:
            self.HeapArray[0] = self.HeapArray[filled-1]
            self.HeapArray[filled-1] = None
            Heap.SortTopDown(0, self.HeapArray)
        else:
            self.HeapArray[0] = None
        return maxElem

    @staticmethod
    def GetFreeNodeIndex(heap):
        for i in range(len(heap)):
            if heap[i] is None:
                return i
        return None

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        index = Heap.GetFreeNodeIndex(self.HeapArray)
        if index is None:
            return False  # если куча вся заполнена
        self.HeapArray[index] = key
        Heap.SortBottonUp(index, self.HeapArray)
        return True
