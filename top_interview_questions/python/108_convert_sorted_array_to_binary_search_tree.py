#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 108_convert_sorted_array_to_binary_search_tree.py
@time: 27/09/2021 11:57 pm
'''
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums, 0, len(nums) - 1)

    def buildBST(self, nums, left, right):
        if left > right:
            return None
        mid = (right + left + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, left, mid - 1)
        root.right = self.buildBST(nums, mid + 1, right)
        return root