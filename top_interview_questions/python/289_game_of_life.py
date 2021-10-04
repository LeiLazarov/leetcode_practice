#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 289_game_of_life.py
@time: 5/10/2021 12:11 am
'''
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for row in range(rows):
            for column in range(columns):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = column + neighbor[1]
                    if r >= 0 and r < rows and c >= 0 and c < columns and abs(board[r][c]) == 1:
                        live_neighbors += 1
                if board[row][column] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][column] = -1
                if board[row][column] == 0 and (live_neighbors == 3):
                    board[row][column] = 2

        for row in range(rows):
            for column in range(columns):
                if (board[row][column] == -1):
                    board[row][column] = 0
                if (board[row][column] == 2):
                    board[row][column] = 1