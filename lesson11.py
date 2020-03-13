#!/usr/bin/env python3


class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # djb2
        acc = 5381
        for c in value:
            code = ord(c)
            acc = ((acc << 5) + acc) + code
        return acc % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        i = slot
        while self.slots[i] is not None:
            i = (i + self.step) % self.size
            if i == slot:
                return None
        return i

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)
        i = slot
        while self.slots[i] is not None:
            if self.slots[i] == value:
                return i
            i = (i + self.step) % self.size
            if i == slot:
                break
        return None


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
