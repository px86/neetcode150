# https://neetcode.io/problems/copy-linked-list-with-random-pointer?list=neetcode150

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes = {}
        ptr = head
        while ptr:
            nodes[ptr] = Node(x=ptr.val)
            ptr = ptr.next

        ptr = head
        root = nodes[head] if head else None
        while ptr:
            nodes[ptr].next = nodes[ptr.next] if ptr.next else None
            nodes[ptr].random = nodes[ptr.random] if ptr.random else None
            ptr = ptr.next

        return root
