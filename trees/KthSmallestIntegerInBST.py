# https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.node_counter: int = 0
        self.solution: Optional[int] = None
        self.k: Optional[int] = None

    def inOrderTraversal(self, root: Optional[TreeNode]):
        if root is None or self.solution is not None:
            return
        self.inOrderTraversal(root.left)
        self.node_counter += 1
        if self.node_counter == self.k:
            self.solution = root.val
            return
        self.inOrderTraversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.node_counter = 0
        self.solution = None
        self.inOrderTraversal(root)
        return self.solution
