#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao
@file: 23_merge_k_sorted_lists.py
@time: 2021/3/25 20:31
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(list1, list2):
            head = ListNode()
            p = head

            while list1 and list2:
                if list1.val <= list2.val:
                    p.next = list1
                    p = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    p = list2
                    list2 = list2.next

            p.next = list1 if list1 else list2
            return head.next

        n = len(lists)
        intervel = 1

        while intervel < n:
            for i in range(0, n - intervel, intervel * 2):
                lists[i] = merge2Lists(lists[i], lists[i + intervel])
            intervel *= 2

        return lists[0] if lists else None
