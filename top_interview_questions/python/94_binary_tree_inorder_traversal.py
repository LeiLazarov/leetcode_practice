#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 94_binary_tree_inorder_traversal.py
@time: 20/09/2021 10:21 pm
'''


# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(ans, root)
        return ans

    def inorder(self, ans, root):
        if not root:
            return
        self.inorder(ans, root.left)
        ans.append(root.val)
        self.inorder(ans, root.right)

    # iterating method
    def iteratingInorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []

        while (root or stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans