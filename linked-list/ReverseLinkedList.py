# https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prevNode = None
        while curr is not None:
            nextNode = curr.next
            nextToNextNode = nextNode.next if nextNode is not None else None
            curr.next = prevNode
            if nextNode is None:
                return curr
            nextNode.next = curr
            prevNode = nextNode
            curr = nextToNextNode
        return prevNode
