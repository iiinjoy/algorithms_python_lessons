#!/usr/bin/env python3

from lesson4 import *


def is_parentheses_balanced(string):
    S = Stack()
    for i in string:
        if i == '(':
            S.push(i)
        else:
            if S.pop() is None:
                return False
    return S.size() == 0
