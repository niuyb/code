#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/1 11:03
# 工具：PyCharm
# Python版本：3.7.0

# python 2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python 3
# import sys
# import importlib
# importlib.reload(sys)
""""""


"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

"""

"""
input: 1,2

:return 3
"""



# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        if not num1: return num2
        if not num2: return num1
        while num2:# 加法是异或，进位是与<<1 + 越界检查
            tmp = (num1^num2)&0xffffffff
            num2 = num2&0xffffffff
            num2 = ((num1&num2)<<1)
            num1 = tmp
        return num1 if num1<=0x7fffffff else ~(num1^0xffffffff)


    def Add2(self, num1, num2):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        print("123123123",MAX,mask)
        while num2 != 0:
            print(num1,num2)
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            print(num1,num2)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)



if __name__ == "__main__":
    s = Solution()

    num=s.Add2(1,2)
    print(num)

