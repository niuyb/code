#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/23 9:09
# 工具：PyCharm
# Python版本：3.7.0
""""""




"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

"""
1 ->  1
4 ->  5
"""


class Solution:
    def jumpFloor(self, number):
        if number==1:
            return 1
        if number==2:
            return 2
        arr=[1,2]
        for i in range(2,number):
            temp=arr[i-1]+arr[i-2]
            arr.append(temp)

        print(arr)
        print(arr[-1])
        return arr[number-1]






if __name__ == "__main__":

    s = Solution()
    print(s.jumpFloor(5))

    print(self_jumpfloor(6))

