#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 2_add_two_numbers.py
@time: 2021/3/25 20:48
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode()
        p = newHead
        indi = 0
        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            temp_sum = first + second + indi
            node = ListNode(temp_sum % 10)
            p.next = node
            p = p.next
            indi = temp_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            p.next = ListNode(indi) if indi else None
        return newHead.next