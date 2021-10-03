#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 215_kth_largest_element_in_an_array.py
@time: 3/10/2021 11:49 pm
'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums)-k]