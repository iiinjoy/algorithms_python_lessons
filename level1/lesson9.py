#!/usr/bin/env python3


class NativeDictionary:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # djb2
        acc = 5381
        for c in key:
            code = ord(c)
            acc = (acc << 5) + acc + code
        return acc % self.size

    def is_key(self, key):
        return self.get(key) is not None

    def put(self, key, value):
        slot = self.hash_fun(key)
        free_slot = slot
        for i in range(self.size):
            k = (slot+i*3) % self.size
            if self.slots[k] is None or self.slots[k] == key:
                free_slot = k
                break
        self.slots[free_slot] = key
        self.values[free_slot] = value

    def get(self, key):
        slot = self.hash_fun(key)
        for i in range(self.size):
            k = (slot+i*3) % self.size
            if self.slots[k] == key:
                return self.values[k]
            if self.slots[k] is None:
                return None
