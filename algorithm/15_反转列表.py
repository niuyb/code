#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/25 10:11
# 工具：PyCharm
# Python版本：3.7.0


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return None
        prev, cur = None, pHead
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev