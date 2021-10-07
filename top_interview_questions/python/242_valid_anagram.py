#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 242_valid_anagram.py
@time: 7/10/2021 10:29 pm
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c < 0:
                return False

        return True

#         return sorted(s) == sorted(t)