#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 237_delete_node_in_a_linked_list.py
@time: 18/09/2021 11:51 am
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next