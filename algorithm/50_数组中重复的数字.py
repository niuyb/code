#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/1 10:01
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
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中第一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，
那么对应的输出是第一个重复的数字2。没有重复的数字返回-1。

"""

"""
input:  [2,3,1,0,2,5,3]


:return   2
"""



# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def duplicate(self , numbers ):
        # write code here
        record = set()
        for num in numbers:
            if num in record:
                return num
            record.add(num)
        return -1

    def duplicate2(self , numbers ):
        # write code here
        L=[]
        for num in numbers:
            if num in L:
                return num
            else:
                L.append(num)
        return -1












