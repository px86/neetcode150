# https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = [root] if root else []
        while len(q):
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == n - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
