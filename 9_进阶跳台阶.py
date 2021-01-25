#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/1 11:34
# 工具：PyCharm
# Python版本：3.7.0

""""""


"""

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""

"""
输入3

输出4

"""



class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            list1 = [1,2]
            for i in range(number-2):
                print(sum(list1))
                # +1  一步登顶
                list1.append(sum(list1)+1)
            print("end:",list1[-1])
            print(list1)
            return list1[-1]



if __name__ == "__main__":

    s= Solution()

    print(s.jumpFloorII(5))