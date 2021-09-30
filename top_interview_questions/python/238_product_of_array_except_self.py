#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 238_product_of_array_except_self.py
@time: 30/09/2021 11:21 pm
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for l in range(1, len(nums)):
            ans.append(ans[l - 1] * nums[l - 1])

        R = 1
        for r in reversed(range(len(nums) - 1)):
            R *= nums[r + 1]
            ans[r] *= R
        return ans

#         lList = [1]
#         for l in range(1, len(nums)):
#             lList.append(lList[l-1] * nums[l-1])
#         print(lList)

#         rList = [1]
#         k = len(nums)
#         for i in range(1, k):
#             rList.append(rList[i-1] * nums[k-i])
#         rList.reverse()
#         print(rList)