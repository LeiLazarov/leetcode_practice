#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 169_majority_element.py
@time: 2/10/2021 8:32 pm
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution 1
        count = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] == cur):
                count += 1
            else:
                count -= 1
            if (count == 0):
                count = 1
                cur = nums[i]
        return cur

        # solution 2
        # return sorted(nums)[len(nums)//2]

        # solution 3
        # for key, value in Counter(nums).items():
        #     if (value > len(nums) / 2):
        #         return key