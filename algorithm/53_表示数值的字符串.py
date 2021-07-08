#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/1 16:22
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
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

"""
input:  "123.45e+6"

:return True

"""



class Solution:
    def isNumeric(self , str ):
        if len(str)<=0:
            return False
        flag_e = False
        flag_sign = False
        flag_dot = False
        for i in range(len(str)):
            if str[i]=='E' or str[i]=="e":
                if flag_e==True:
                    return False
                if i==len(str)-1:
                    return False
                flag_e=True
            elif str[i]=="+" or str[i]=="-":
                if flag_sign==True:
                    if str[i-1]!="E" and str[i-1]!="e":
                        return False
                elif i!=0 and str[i-1]!="E" and str[i-1]!="e":
                    return False
                flag_sign=True
            elif str[i]==".":
                if flag_dot==True or flag_e==True:
                    return False
                flag_dot=True
            else:
                if str[i]<'0' or str[i]>'9':
                    return False
        return True