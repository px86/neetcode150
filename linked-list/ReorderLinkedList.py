# https://neetcode.io/problems/reorder-linked-list?list=neetcode150

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Return the middle node of the list."""
        if not head:
            return None
        slow = fast = head
        while True:
            if not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse a given linked list."""
        if not head:
            return None
        llist = None
        node = head
        while node is not None:
            nextNode = node.next
            if nextNode is not None:
                nextToNextNode = nextNode.next
                nextNode.next = node
                node.next = llist
                llist = nextNode
                node = nextToNextNode
            else:
                node.next = llist
                llist = node
                break
        return llist

    def printList(self, llist: Optional[ListNode]) -> None:
        while llist:
            print(llist.val, "->", end="")
            llist = llist.next
        print("null")

    def reorderList(self, head: Optional[ListNode]) -> None:
        # self.printList(head)
        mid = self.findMiddle(head)
        right = mid.next
        mid.next = None
        right = self.reverseList(right)
        # self.printList(head)
        # self.printList(right)
        ptr1, ptr2 = head, right
        while ptr1 and ptr2:
            ptr1next = ptr1.next
            ptr2next = ptr2.next
            ptr1.next = ptr2
            ptr2.next = ptr1next
            ptr1 = ptr1next
            ptr2 = ptr2next
