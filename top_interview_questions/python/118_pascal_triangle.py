#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 118_pascal_triangle.py
@time: 12/10/2021 11:46 pm
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            tool = [1] * (i + 1)
            for j in range(1, i):
                tool[j] = ans[i - 1][j] + ans[i - 1][j - 1]
            ans.append(tool)

        return ans