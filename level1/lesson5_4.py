#!/usr/bin/env python3

from lesson4 import *


class Queue2:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        else:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()
