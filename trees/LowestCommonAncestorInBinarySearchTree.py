# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        ancestors_p = []
        ancestors_q = []

        node = root
        while node and node.val != p.val:
            ancestors_p.append(node)
            node = node.left if p.val < node.val else node.right
        ancestors_p.append(p)

        node = root
        while node and node.val != q.val:
            ancestors_q.append(node)
            node = node.left if q.val < node.val else node.right
        ancestors_q.append(q)

        # print(ancestors_p)
        # print(ancestors_q)

        if len(ancestors_p) > len(ancestors_q):
            while len(ancestors_p) != len(ancestors_q):
                ancestors_p.pop()

        if len(ancestors_p) < len(ancestors_q):
            while len(ancestors_p) != len(ancestors_q):
                ancestors_q.pop()

        solution = None
        for i in range(len(ancestors_p) - 1, -1, -1):
            # print(ancestors_p[i])
            # print(ancestors_q[i])
            if ancestors_p[i].val == ancestors_q[i].val:
                solution = ancestors_p[i]
                break
        return solution
