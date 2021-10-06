#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 122_best_time_to_buy_and_sell_stock_ii.py
@time: 6/10/2021 11:28 pm
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        index = 0

        while (index < len(prices)):
            cur_min = prices[index]
            while (index < len(prices) - 1 and prices[index + 1] < prices[index]):
                index += 1
            min_index = index
            while (index < len(prices) - 1 and prices[index + 1] > prices[index]):
                index += 1
            profit += prices[index] - prices[min_index]
            index += 1

        return profit