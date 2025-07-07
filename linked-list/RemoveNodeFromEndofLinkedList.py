# https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode150

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, llist: Optional[ListNode]) -> None:
        while llist:
            print(llist.val, "->", end="")
            llist = llist.next
        print("null")

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        x = self.nthNode(head, n=n)
        if not x:
            return head.next
        y = x.next.next
        x.next = y
        self.printList(head)
        return head

    def nthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Return nth node from the end of the list. 0th being the last node."""
        if not head:
            return None
        position = 0
        a = b = head
        # move 'b' n positions forward keeping 'a' at head
        while position < n:
            if b.next:
                b = b.next
                position += 1
            else:
                return None

        # move 'a' and 'b' one position, when b reaches last node, return a
        while b.next:
            a = a.next
            b = b.next
        return a
