#!/usr/bin/env python3

from lesson6 import *


def is_palindrome(string):
    D = Deque()
    for c in string:
        D.addTail(c)
    while D.size() > 1:
        if D.removeFront() != D.removeTail():
            return False
    return True
