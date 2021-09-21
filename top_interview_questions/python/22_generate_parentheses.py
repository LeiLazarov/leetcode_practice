#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 22_generate_parentheses.py
@time: 21/09/2021 10:55 pm
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(ans, "", n, 0, 0)
        return ans

    def backtrack(self, ans, temp, n, left, right):
        if left == n and right == n:
            ans.append(temp)
        if left < n:
            self.backtrack(ans, temp + "(", n, left + 1, right)
        if right < left:
            self.backtrack(ans, temp + ")", n, left, right + 1)
