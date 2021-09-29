#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 347_top_k_frequent_elements.py
@time: 29/09/2021 11:56 pm
'''
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (k == len(nums)):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), count.get)