#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/2/24 9:44
# 工具：PyCharm
# Python版本：3.7.0


""""""


"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

"""



class Solution:
    def __init__(self):
        self.Stack = []
        self.minValue = []

    def push(self, node):
        self.Stack.append(node)
        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)

    def pop(self):
        # write code here
        if self.Stack == []:
            return None
        self.minValue.pop()
        return self.Stack.pop()

    def top(self):
        # write code here
        if self.Stack == []:
            return None
        return self.Stack[-1]

    def min(self):
        # write code here
        if self.minValue == []:
            return None
        return self.minValue[-1]
