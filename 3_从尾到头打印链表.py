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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_listnode(List):
    # 输入一个列表
    # 输出链表的第一个元素
    head = ListNode(List[0])  # 创建一个头节点并将list第一个值赋值给头结点
    p = head  # 创建头指针
    for i in range(1, len(List)):  # list从第二位开始遍历
        p.next = ListNode(List[i])  # 下一个结点p.next指向list值
        p = p.next  # 指针往下移动
    return head  # 返回头结点



class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        r_list=[]
        head=listNode
        while(head!=None):
            r_list.append(head.val)
            head=head.next
        r_list.reverse()
        return r_list



if __name__ == "__main__":

    s = Solution()

    list = [67,0,24,58]
    head=make_listnode(list)
    r_list=s.printListFromTailToHead(head)
    print(r_list)


