#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 104_maximum_depth_of_binary_tree.py
@time: 17/09/2021 11:53 pm
'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)