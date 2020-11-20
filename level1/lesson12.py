#!/usr/bin/env python3


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        # djb2
        acc = 5381
        for c in key:
            code = ord(c)
            acc = (acc << 5) + acc + code
        return acc % self.size

    def put(self, key, value):
        slot = self.hash_fun(key)
        free_slot = None
        slot_with_min_hit = slot
        for i in range(self.size):
            k = (slot+i*3) % self.size
            if self.slots[k] is None or self.slots[k] == key:
                free_slot = k
                break
            if self.hits[k] < self.hits[slot_with_min_hit]:
                slot_with_min_hit = k
        if free_slot is None:
            free_slot = slot_with_min_hit
        self.slots[free_slot] = key
        self.values[free_slot] = value
        self.hits[free_slot] = 0

    def get(self, key):
        slot = self.hash_fun(key)
        for i in range(self.size):
            k = (slot+i*3) % self.size
            if self.slots[k] == key:
                self.hits[k] += 1
                return self.values[k]
            if self.slots[k] is None:
                return None
