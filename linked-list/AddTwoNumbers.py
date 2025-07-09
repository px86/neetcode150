# https://neetcode.io/problems/add-two-numbers?list=neetcode150

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = ptr = None
        carry = 0
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if sum > 9:
                node = ListNode(val=sum % 10)
                carry = 1
            else:
                node = ListNode(val=sum)
                carry = 0
            if ptr:
                ptr.next = node
                ptr = node
            else:
                root = ptr = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            ptr.next = ListNode(val=carry)

        return root
