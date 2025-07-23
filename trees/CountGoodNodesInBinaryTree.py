# https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(node, current_max, goodcount) -> int:
            # print(node.val if node else None, current_max, goodcount)
            if node is None:
                return goodcount
            if node.val >= current_max:
                goodcount += 1
                current_max = node.val
            return (
                f(node.left, current_max, goodcount)
                + f(node.right, current_max, goodcount)
                - goodcount
            )

        return f(root, -10000, 0)
