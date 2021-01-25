#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/1 13:17
# 工具：PyCharm
# Python版本：3.7.0

""""""


"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：

"""

"""
in:4

out:5

"""


class Solution():
    def rectCover(self, n):
        ## 非递归方法换一种写法
        if n == 0:
            return n
        a,b = 0,1
        # i有n个数,每个数都是前两项之和
        for i in range(n):
            a,b = b, a+b
        return b

    def rectCover2(self, number):
        res = [0, 1, 2]
        for i in range(number):
            res.append(res[-1] + res[-2])
        return res[number]

    def rectCover3(self, number):
            res = [0,1,2]
            while len(res)<=number:
                res.append(res[-1]+res[-2])
            return res[number]


if __name__ == "__main__":

    s= Solution()

    print(s.rectCover3(4))