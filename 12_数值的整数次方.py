#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/7 10:12
# 工具：PyCharm
# Python版本：3.7.0
""""""


"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""

"""
in:2,3

out:8

"""




class Solution:
    def Power(self, base, exponent):
        # temp
        temp=1
        if exponent>0:
            n=exponent
        elif exponent<=0:
            if base==0:
                return "error"
            n=-exponent
        else:
            return 1
        while n!=0:
            if n&1!=0:
                temp*=base
            n>>=1
            base=base*base
        if exponent<0:
            temp=1/temp
        return temp

    def Power_1(self, base, exponent):
        if base or exponent:
            return base**exponent



if __name__ == "__main__":

    s= Solution()
    print(s.Power(2,3))


    print("123",2&1)


