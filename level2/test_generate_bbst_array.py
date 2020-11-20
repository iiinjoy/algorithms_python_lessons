#!/usr/bin/env python3

import unittest
from generate_bbst_array import *


class TestGenerateBBSTArray(unittest.TestCase):

    def test(self):
        self.assertEqual(GenerateBBSTArray([]), [None])
        self.assertEqual(GenerateBBSTArray([1]), [1])
        self.assertEqual(GenerateBBSTArray([2, 1]), [2, 1, None])
        self.assertEqual(GenerateBBSTArray([3, 2, 1]), [2, 1, 3])
        self.assertEqual(GenerateBBSTArray(list(range(1, 16))), [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
        self.assertEqual(GenerateBBSTArray(list(range(8))), [4, 2, 6, 1, 3, 5, 7, 0] + [None] * 7)

if __name__ == '__main__':
    unittest.main()
