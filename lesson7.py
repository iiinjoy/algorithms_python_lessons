#!/usr/bin/env python3


class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        return {
            v1 < v2: -1,
            v1 == v2: 0,
            v1 > v2: 1
        }[True]

    def add(self, value):
        node = self.head
        new_node = Node(value)
        asc = 1 if self.__ascending else -1
        while node is not None:
            if self.compare(node.value, value) == asc:
                new_node.prev = node.prev
                new_node.next = node
                node.prev = new_node
                break
            node = node.next
        if new_node.next is None:
            new_node.prev = self.tail
            if self.tail is not None:
                self.tail.next = new_node
            self.tail = new_node
        if new_node.prev is None:
            self.head = new_node
        else:
            new_node.prev.next = new_node

    def find(self, val):
        node = self.head
        asc = 1 if self.__ascending else -1
        while node is not None:
            comp = self.compare(node.value, val)
            if comp == 0:
                return node
            if comp == asc:
                return None
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        asc = 1 if self.__ascending else -1
        while node is not None:
            comp = self.compare(node.value, val)
            if comp == 0:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
            if comp == asc:
                return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):

    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        s1 = v1.strip()
        s2 = v2.strip()
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            return 0
