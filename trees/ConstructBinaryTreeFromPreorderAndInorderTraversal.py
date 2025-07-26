# https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal?list=neetcode150

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert len(inorder) == len(preorder)
        if not len(inorder):
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root = TreeNode(val=inorder[i])
                if i != 0:
                    root.left = self.buildTree(preorder[1 : i + 1], inorder[:i])
                root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])
                return root
