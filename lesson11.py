#!/usr/bin/env python3

from lesson8 import *


class PowerSet:

    def __init__(self):
        self.capacity = 20000
        self.ht = HashTable(self.capacity, 223)
        self.count = 0

    def size(self):
        # количество элементов в множестве
        return self.count

    def put(self, value):
        # всегда срабатывает
        if self.ht.find(value) is None:
            self.count += 1
            self.ht.put(value)

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        return self.ht.find(value) is not None

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        slot = self.ht.find(value)
        if slot is not None:
            self.ht.slots[slot] = None
            self.count -= 1
            return True
        return False

    def intersection(self, set2):
        s = PowerSet()
        for i in range(self.capacity):
            value = self.ht.slots[i]
            if value is not None and set2.get(value):
                s.put(value)
        return s

    def union(self, set2):
        # объединение текущего множества и set2
        s = PowerSet()
        for i in range(self.capacity):
            if self.ht.slots[i] is not None:
                s.put(self.ht.slots[i])
            if set2.ht.slots[i] is not None:
                s.put(set2.ht.slots[i])
        return s

    def difference(self, set2):
        # разница текущего множества и set2
        s = PowerSet()
        for i in range(self.capacity):
            value = self.ht.slots[i]
            if value is not None and set2.get(value) is False:
                s.put(value)
        return s

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for i in range(self.capacity):
            value = set2.ht.slots[i]
            if value is not None and self.get(value) is False:
                return False
        return True
