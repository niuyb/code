#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/18 10:15
# 工具：PyCharm
# Python版本：3.7.0

''''''

"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


"""
7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

14,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        num = len(array)
        flag = "false"
        if num <= 0:
            return flag
        for i in range(num):
            if len(array[i]) <=0:
                continue
            if array[i][-1] < target or array[i][0] > target:
                continue
            if target in array[i]:
                flag = "true"
                break
        return flag

s = Solution()
while True:
    try:
        input_str = eval(input())
        target = input_str[0]
        array = input_str[1]
        print(s.Find(target, array))
    except:
        break