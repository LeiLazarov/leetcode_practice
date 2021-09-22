#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 78_subsets.py
@time: 22/09/2021 10:58 pm
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            self.backtrack(ans, nums, [], i, 0)
        return ans

    def backtrack(self, ans, nums, temp, k, start):
        if len(temp) == k:
            ans.append(temp)
        for i in range(start, len(nums)):
            self.backtrack(ans, nums, temp + [nums[i]], k, i + 1)