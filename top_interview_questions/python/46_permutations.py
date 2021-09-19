#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 46_permutations.py
@time: 19/09/2021 11:41 pm
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(ans, nums, [], [0] * len(nums))
        return ans

    def backtrack(self, ans, nums, temp, visit):
        if (len(temp) == len(nums)):
            ans.append(temp)
        for i in range(0, len(nums)):
            if not visit[i]:
                visit[i] = 1
                self.backtrack(ans, nums, temp + [nums[i]], visit)
                visit[i] = 0