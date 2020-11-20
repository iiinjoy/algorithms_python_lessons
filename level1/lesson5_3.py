#!/usr/bin/env python3

from lesson5 import *


def rotate_queue(Q, N):
    while N > 0 and Q.size() > 0:
        item = Q.dequeue()
        Q.enqueue(item)
        N -= 1
