#!/usr/bin/env python3

from lesson4_2 import *


def postfix_eval(string):
    s1 = string.split()
    s2 = Stack()
    while len(s1):
        elem = s1.pop(0)
        if elem.isdecimal():
            s2.push(int(elem))
        elif elem == "+":
            s2.push(s2.pop() + s2.pop())
        elif elem == "*":
            s2.push(s2.pop() * s2.pop())
        elif elem == "=":
            return s2.stack

if __name__ == '__main__':
    print(postfix_eval("8 2 + 5 * 9 + ="))
