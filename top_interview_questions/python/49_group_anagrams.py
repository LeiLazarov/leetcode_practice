#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 49_group_anagrams.py
@time: 1/10/2021 11:54 pm
'''
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

#         ans = defaultdict(list)

#         for s in strs:
#             ans[tuple(sorted(s))].append(s)

#         return ans.values()