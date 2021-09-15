#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 01_two_sum.py
@time: 15/09/2021 9:53 pm
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            if (target - nums[i]) in d:
                return [d[target - nums[i]], i]
            if nums[i] not in d:
                d[nums[i]] = i