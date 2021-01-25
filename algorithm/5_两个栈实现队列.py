#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/20 9:27
# 工具：PyCharm
# Python版本：3.7.0


""""""


"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()