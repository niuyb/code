#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/26 10:37
# 工具：PyCharm
# Python版本：3.7.0
""""""
from data_structure.链表 import ListNode, make_listnode, print_listnode

"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""

"""
:input
{1,3,5},{2,4,6}

:return
{1,2,3,4,5,6}

"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        cur = ListNode(0)
        p = cur
        while pHead1 and pHead2:
            # print("pHead11111111",pHead1.val)
            # print("pHead22222222222",pHead2.val)
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                # 替换 头节点继续向下比较
                pHead1 = pHead1.next

            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        # pHead1 与 pHead2 之间如有一个为空 循环停止
        #  返回的链表中需要加上不为空的一个剩余链表
        # 又因为 剩下的链表顺序已经排好所以只需要简单附加即可
        cur.next = pHead1 if pHead1 else pHead2

        print(cur.next.val)
        return p.next


if __name__ == "__main__":

    head1 = make_listnode([-1,1,2,3,5,7])
    head2 = make_listnode([0,6,8])

    s = Solution()
    r =s.Merge(head1,head2)

    print_listnode(r)

