#!/usr/bin/env python3

import unittest
from lesson10 import *


class TestBloomFilterMethods(unittest.TestCase):

    def test_all(self):
        B = BloomFilter(32)
        test_strings = []
        for i in range(10):
            test_string = ""
            for j in range(10):
                test_string += str((i + j) % 10)
            test_strings.append(test_string)
        for ts in test_strings:
            B.add(ts)
        for ts in test_strings:
            self.assertTrue(B.is_value(ts))

        seq = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        fail_count = 0
        for i in seq:
            if B.is_value(i*10):
                fail_count += 1
        m = 32
        n = 10
        P_fail = 0.6931 ** (m / n)
        # print("fail_count/n = {}".format(fail_count/len(seq)))
        # print("P_fail = {}".format(P_fail))
        self.assertTrue(fail_count/len(seq) < P_fail)


if __name__ == '__main__':
    unittest.main()
