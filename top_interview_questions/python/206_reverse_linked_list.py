#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@file: 206_reverse_linked_list.py
@time: 23/09/2021 10:20 pm
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead = None
        while head:
            nex = head.next
            head.next = newHead
            newHead = head
            head = nex
        return newHead