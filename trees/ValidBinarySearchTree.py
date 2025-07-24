# https://neetcode.io/problems/valid-binary-search-tree?list=neetcode150

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root: Optional[TreeNode], minval: int, maxval: int) -> bool:
            print(root.val, minval, maxval)
            if root is None:
                return True
            if not root.left and not root.right:
                return minval < root.val < maxval

            if not root.left:
                if root.val < root.right.val:
                    return f(root.right, minval=root.val, maxval=maxval)
                else:
                    return False

            if not root.right:
                if root.val > root.left.val:
                    return f(root.left, minval=minval, maxval=root.val)
                else:
                    return False

            if root.left.val < root.val < root.right.val:
                return f(root.left, minval=minval, maxval=root.val) and f(
                    root.right, minval=root.val, maxval=maxval
                )
            else:
                return False

        return f(root, -1001, 1001)
