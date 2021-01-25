#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/18 11:04
# 工具：PyCharm
# Python版本：3.7.0

""""""

"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = s.replace(" ","%20")
        return res

s =Solution()
s.replaceSpace("We Are Happy")