#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 412_fizz_buzz.py
@time: 25/09/2021 9:56 pm
'''
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if (i % 3 == 0 and i % 5 == 0):
                ans.append('FizzBuzz')
            elif (i % 3 == 0):
                ans.append('Fizz')
            elif (i % 5 == 0):
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans