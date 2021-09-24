#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 136_single_number.py
@time: 24/09/2021 9:58 pm
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans