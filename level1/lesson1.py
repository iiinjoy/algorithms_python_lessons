#!/usr/bin/env python3


class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        prev = None
        while node is not None:
            if node.value == val:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                if self.tail == node:
                    self.tail = prev
                if not all:
                    break
            else:
                prev = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if newNode.next is None:
                self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if newNode.next is None:
                self.tail = newNode
