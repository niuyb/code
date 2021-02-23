#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/19 9:35
# 工具：PyCharm
# Python版本：3.7.0





class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_listnode(List):
    # List = List[::-1]
    print(List)
    # 输入一个列表
    # 输出链表的第一个元素
    head = ListNode(List[0])  # 创建一个头节点并将list第一个值赋值给头结点
    p = head  # 创建头指针
    for i in range(1, len(List)):  # list从第二位开始遍历
        p.next = ListNode(List[i])  # 下一个结点p.next指向list值
        p = p.next  # 指针往下移动
    return head  # 返回头结点



# 输出链表顺序
def print_listnode(head):
    listnode = []
    p = head
    while True:
        if p:
            listnode.append(p.val)
            p = p.next
        else:
            print(listnode)
            return listnode


