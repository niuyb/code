#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/2 11:11
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
题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？

例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

"""


"""
input  8

out  18
"""


class Solution:
    def cutRope(self, number):
        if number == 2:
            return 1
        if number == 3:
            return 2

        n = number // 3
        if number - n * 3 == 1:
            n = n - 1
        return 3 ** n * ((number - n * 3) if number - n * 3 else 1)



if __name__ == "__main__":


    a =8 // 3
    print(a)

    n = 2
    number = 8

    b = 3 ** 2
    print(b)


    a = ((number - n * 3) if number - n * 3 else 1)
    print(a)





