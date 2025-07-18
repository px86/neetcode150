# https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeEqual(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a == b and a is None:
            return True
        return (
            (a and b)
            and (a.val == b.val)
            and self.treeEqual(a.left, b.left)
            and self.treeEqual(a.right, b.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot and root is None:
            return True
        if not (root and subRoot):
            return False
        if root.val == subRoot.val:
            if self.treeEqual(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
