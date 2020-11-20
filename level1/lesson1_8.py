#!/usr/bin/env python3

from lesson1 import *


def LL_to_list(LL):
    L = []
    node = LL.head
    while node is not None:
        L.append(node.value)
        node = node.next
    return L


def zipWithAdd(LL1, LL2):
    L1 = LL_to_list(LL1)
    L2 = LL_to_list(LL2)
    if len(L1) == len(L2):
        return [x + y for (x, y) in zip(L1, L2)]
