#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/20 9:39
# 工具：PyCharm
# Python版本：3.7.0

""""""

"""

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        else:
            return min(rotateArray)


while True:
    try:
        s = Solution()
        rota = list(eval(input()))
        print(s.minNumberInRotateArray(rota))
    except:
        break