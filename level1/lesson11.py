#!/usr/bin/env python3


class PowerSet:

    def __init__(self):
        self.powerset = []

    def size(self):
        return len(self.powerset)

    def put(self, value):
        if not self.get(value):
            self.powerset.append(value)

    def get(self, value):
        return value in self.powerset

    def remove(self, value):
        if self.get(value):
            self.powerset.remove(value)
            return True
        return False

    def intersection(self, set2):
        s = PowerSet()
        for elem in self.powerset:
            if set2.get(elem):
                s.put(elem)
        return s

    def union(self, set2):
        s = PowerSet()
        s.powerset = self.powerset.copy()
        for elem in set2.powerset:
            s.put(elem)
        return s

    def difference(self, set2):
        s = PowerSet()
        s.powerset = self.powerset.copy()
        for elem in set2.powerset:
            s.remove(elem)
        return s

    def issubset(self, set2):
        for elem in set2.powerset:
            if not self.get(elem):
                return False
        return True
