#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao
@file: 21_merge_two_sorted_lists.py
@time: 2021/3/25 20:31
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #         solution 2 - recursive way
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#         solution 1 - iterative way
#         head = ListNode()
#         p = head

#         while l1 and l2:
#             if l1.val <= l2.val:
#                 p.next = l1
#                 l1 = l1.next
#             else:
#                 p.next = l2
#                 l2 = l2.next
#             p = p.next

#         p.next = l1 if not l2 else l2

#         return head.next
