#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 817_linked_list_components.py
@time: 2021/3/25 21:20
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gset = set(G)
        ans = 0

        while head:
            if head.val in Gset and (not head.next or head.next.val not in Gset):
                ans += 1
            head = head.next
        return ans