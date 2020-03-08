#!/usr/bin/env python3


class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitmask = 0

    def hash1(self, str1):
        acc = 0
        for c in str1:
            code = ord(c)
            acc = ((acc * 17) + code) % self.filter_len
        return (1 << acc)

    def hash2(self, str1):
        acc = 0
        for c in str1:
            code = ord(c)
            acc = ((acc * 223) + code) % self.filter_len
        return (1 << acc)

    def add(self, str1):
        mask = self.hash1(str1) | self.hash2(str1)
        self.bitmask |= mask

    def is_value(self, str1):
        mask = self.hash1(str1) | self.hash2(str1)
        return (self.bitmask & mask) == mask
