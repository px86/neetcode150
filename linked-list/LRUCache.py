# https://neetcode.io/problems/lru-cache?list=neetcode150

from typing import Optional


class ListNode:
    def __init__(
        self,
        key: int,
        val: int,
        prev: "Optional[ListNode]" = None,
        next: "Optional[ListNode]" = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.nodemap = {}

    def get(self, key: int) -> int:

        node = self.nodemap.get(key)
        if node is None:
            return -1

        if node.prev is None:
            # node is the first node
            return node.val
        if node.next is None:
            # node is the last node
            self.tail = node.prev
            node.prev.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            # move node to the front of the list
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        return self.head.val

    def put(self, key: int, value: int) -> None:

        if key in self.nodemap:
            self.get(key)  # this will bring node to the front
            self.head.val = value
            return

        while self.size >= self.capacity:
            self.nodemap.pop(self.tail.key)
            self.size -= 1
            if self.tail.prev:
                self.tail.prev.next = None
                n = self.tail.prev
                self.tail.prev = None
                self.tail = n

        node = ListNode(key=key, val=value)
        self.nodemap[key] = node
        self.size += 1

        if self.size == 1:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
