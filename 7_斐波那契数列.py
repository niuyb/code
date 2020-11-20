#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/20 9:44
# 工具：PyCharm
# Python版本：3.7.0

""""""


"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39

"""


class Solution:
    def Fibonacci(self, n):
        nums=[]
        x = [x for x in range(n+1)]
        for index in x:
            if index==0 or index==1:
                nums.append(index)
            else:
                nums.append(nums[-1]+nums[-2])

        return nums[-1],nums



if __name__ == "__main__":

    # s = Solution()
    # num,num_list=s.Fibonacci(40)
    # print(num,num_list)

    print(hash("永安行"))
    print(hash("永安行"))
    print(hash("百灵时代（北京）文化传媒有限公司"))
    print(hash("太子地产（柬埔寨）集团有限公司"))