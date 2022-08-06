#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@time: 6/08/2022 01:00 am
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        
        return False