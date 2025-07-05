# https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode150

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

    def copyList(self, llist: Optional[ListNode]) -> Optional[ListNode]:
        copied = ptr = None
        while llist:
            node = ListNode(val=llist.val)
            llist = llist.next
            if copied:
                ptr.next = node
                ptr = ptr.next
            else:
                copied = ptr = node
        return copied

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = ptr = None
        rest = None
        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(val=list1.val)
                list1 = list1.next
            else:
                node = ListNode(val=list2.val)
                list2 = list2.next
            if root is not None:
                ptr.next = node
                ptr = node
            else:
                root = ptr = node
        if list1:
            rest = self.copyList(list1)

        if list2:
            rest = self.copyList(list2)

        if rest:
            if root:
                ptr.next = rest
            else:
                root = rest

        return root
