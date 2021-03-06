#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/25 10:11
# 工具：PyCharm
# Python版本：3.7.0
""""""
from data_structure.链表 import make_listnode, print_listnode

"""
输入一个链表，反转链表后，输出新链表的表头。

"""


"""
:input
{1,2,3}

:return
{3,2,1}

"""

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



if __name__ == "__main__":

    head=make_listnode([0,1,2,3,4,5,6,7,8,9])

    print_listnode(head)

    s= Solution()
    k  =s.ReverseList(head)

    print_listnode(k)

