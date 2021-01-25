#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/1 13:16
# 工具：PyCharm
# Python版本：3.7.0
""""""



"""
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

"""

"""
in:10

out:2

"""


class Solution:
    def NumberOf1(self, n):
        count=0
        for i in range(32):
            count+=1 if n&1==1 else 0
            n = n//2
        return count




if __name__ == "__main__":

    s= Solution()

    print(s.NumberOf1(10))