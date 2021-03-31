#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/31 17:35
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
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

"""

"""
input:  输入一个字符串,包括数字字母符号,可以为空


:return  如果是合法的数值表达则返回该数字，否则返回0


"""





class Solution:
    def StrToInt(self, s):
        numlist=['0','1','2','3','4','5','6','7','8','9']
        pn=['+','-']
        res=0
        symbol=1
        if s=='':
            return 0
        for i in s:
            if i in numlist:
                # print(res*10+numlist.index(i))
                # print(res*10,numlist.index(i))
                res=res*10+numlist.index(i)
            elif i in pn:
                    if i=='-': symbol=-1
            else:
                return 0
        return res*symbol


if __name__ == "__main__":

    s = Solution()
    res = s.StrToInt("+2147483647")

    print(res)