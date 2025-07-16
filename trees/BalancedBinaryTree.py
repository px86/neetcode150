# https://neetcode.io/problems/balanced-binary-tree?list=neetcode150

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(root: Optional[TreeNode]):
            if root is None:
                return 0, True
            left_h, isBalanced_l = f(root.left)
            right_h, isBalanced_r = f(root.right)
            if not (isBalanced_l and isBalanced_r):
                return -1, False
            if abs(left_h - right_h) > 1:
                return -1, False
            return max(left_h, right_h) + 1, True

        _, isBalanced = f(root)
        return isBalanced
