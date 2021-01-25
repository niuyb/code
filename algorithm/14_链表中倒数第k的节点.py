#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/8 17:28
# 工具：PyCharm
# Python版本：3.7.0

""""""
from data_structure.链表 import make_listnode

"""
输入一个链表，输出该链表中倒数第k个结点。
"""

"""
in:   1,{1,2,3,4,5}

out:  {5}
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0:
            return None
        len = 0
        p = head
        while p:
            len += 1
            p = p.next
        if k > len:
            return None
        q = head
        r = head
        for i in range(k - 1):
            q = q.next
        while q:
            q = q.next
            if q:
                r = r.next
        return r


if __name__ == "__main__":
    head=make_listnode([0,1,2,3,4,5,6,7,8,9])
    s= Solution()
    k  =s.FindKthToTail(head,2)
    print(k.val)








