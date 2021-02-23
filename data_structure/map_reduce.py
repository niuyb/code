#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/27 14:03
# 工具：PyCharm
# Python版本：3.7.0
""""""

"""
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。



参数
function -- 函数
iterable -- 一个或多个序列


Python 2.x 返回列表。

Python 3.x 返回迭代器。

"""


def square(x) :         # 计算平方数
     return x ** 2

temp1=map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
# <map object at 0x100d3d550>     # 返回迭代器
temp2 = list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
# [1, 4, 9, 16, 25]
print(temp1)
print(temp2)



















"""
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用
function 函数运算，最后得到一个结果。

注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：



参数
function -- 函数，有两个参数
iterable -- 可迭代对象
initializer -- 可选，初始参数



返回
函数计算结果。


"""

from functools import reduce

def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y,[1,2,3,4,5])  # 使用 lambda 匿名函数
sum3 = reduce(lambda x, y: x+y,[1,2,3,4,5],6)  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
print(sum3)




#   *  ** 区别
def fun(a, b, c):
    print (a, b, c)

list1=[[1,2,3]]
dict1 = {"c":1,"b":2}
print(*list1)
fun("2",**dict1)