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
