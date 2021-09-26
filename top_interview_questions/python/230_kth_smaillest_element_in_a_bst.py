#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 230_kth_smaillest_element_in_a_bst.py
@time: 26/09/2021 10:53 pm
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans, stack = 0, []

        while ((stack or root) and k):
            while root:
                stack.append(root)
                root = root.left
            ans = stack[-1].val
            k -= 1
            root = stack.pop().right

        return ans