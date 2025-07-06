# https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150

# Read more here: https://cp-algorithms.com/others/tortoise_and_hare.html

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next

        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next

        return False
