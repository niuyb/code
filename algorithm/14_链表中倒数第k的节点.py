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
        # 参数异常返回None
        if k <= 0:
            return None
        # 找出链表长度
        len = 0
        p = head
        while p:
            len += 1
            p = p.next
        # 参数 大于 长度 异常返回None
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


    def self_FindKthToTail(self,head,k):
        # 参数异常返回None
        if k <= 0:
            return None
        # 找出链表长度
        len = 0
        p = head
        while p:
            len += 1
            p = p.next
        # 参数 大于 长度 异常返回None
        if k > len:
            return None
        q = head
        index = len - k
        for i in range(index):
            q = q.next
        return q


if __name__ == "__main__":
    head=make_listnode([0,1,2,3,4,5,6,7,8,9])
    s= Solution()
    k  =s.FindKthToTail(head,6)
    print(k.val)
    k  =s.self_FindKthToTail(head,6)
    print(k.val)







