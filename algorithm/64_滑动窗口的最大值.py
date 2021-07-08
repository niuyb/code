#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/20 17:38
# 工具：PyCharm
# Python版本：3.7.0
""""""




"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 

针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 

{[2,3,4],2,6,2,5,1}，{2,[3,4,2],6,2,5,1},{2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}，{2,3,4,2,[6,2,5],1}，{2,3,4,2,6,[2,5,1]}。

窗口大于数组长度的时候，返回空
"""


"""
input:  [2,3,4,2,6,2,5,1],3

:return  [4,4,6,6,6,5]

"""

class Solution:
    def maxInWindows(self, num, size):
        if len(num) < size:    return []
        elif size == 0:    return []
        elif len(num) == size:    return [max(num)]
        Max = []
        for i in range(len(num) - size + 1):
            Max.append(max(num[i:i+size]))
        return Max


if __name__ == "__main__":
    s = Solution()

    num = [2,3,4,2,6,2,5,1]
    size = 3
    print  len(num) - size + 1

    Max =s.maxInWindows(num,size)

    print Max