#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/1 13:21
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
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为 O(n).

"""

"""
input:  [1,-2,3,10,-4,7,2,-5]

:return  18
"""


"""
输入的数组为{1,-2,3,10,—4,7,2,一5}，和最大的子数组为{3,10,一4,7,2}，因此输出为该子数组的和 18。

"""

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
            a, dp = array[0], []
            for i in array[1:]:
                a = max(a + i, i)
                dp.append(a)
            return max(dp)

    def FindGreatestSumOfSubArray2(self, array):
        # write code here
        if not array:
            return None
        maxNum = array[0]
        for i in range(1,len(array)):
            if array[i-1] > 0:
                array[i] = array[i-1] + array[i]
            maxNum = max(maxNum, array[i])
            print(maxNum)
        return maxNum






if __name__ == "__main__":

    s = Solution()
    max_num=s.FindGreatestSumOfSubArray2([1,-2,3,10,-4,7,2,-5])

    print(max_num)

















