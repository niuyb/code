#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/2 12:05
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
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。


"""
"""
input:  [4,5,1,6,2,7,3,8],4

:return  [1,2,3,4]
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[: k]



if __name__ == "__main__" :

    s = Solution()
    k_list = s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4)

    print("k_list",k_list)