# https://neetcode.io/problems/binary-tree-diameter?list=neetcode150

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root, diameter=0):
            if root is None:
                return 0, diameter
            left_h, left_diameter = height(root.left, diameter)
            right_h, right_diameter = height(root.right, diameter)
            d = left_h + right_h
            diameter = max(left_diameter, right_diameter)
            if d > diameter:
                diameter = d
            return max(left_h, right_h) + 1, diameter

        _, diameter = height(root)
        return diameter
