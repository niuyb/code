#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/18 11:14
# 工具：PyCharm
# Python版本：3.7.0
""""""



"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


"""
{67,0,24,58}
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        num=[]
        head=listNode
        while(head!=None):
            num.append(head.val)
            head=head.next
        num.reverse()
        print(num)
        return num

s = Solution()

l1 = ListNode(67)  # 建立链表3->2->1->9->None
l1.next = ListNode(0)
l1.next.next = ListNode(24)
l1.next.next.next = ListNode(58)

s.printListFromTailToHead(l1)
