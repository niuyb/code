#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/27 13:24
# 工具：PyCharm
# Python版本：3.7.0
""""""

"""
*args 与 **kwargs 的区别，两者都是 python 中的可变参数：

*args 表示任何多个无名参数，它本质是一个 tuple
**kwargs 表示关键字参数，它本质上是一个 dict
"""


"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，

例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

1  2  3  4
5  6  7  8  
9 10 11  12
13 14 15 16 

思路:

每次打印并删除矩阵的第一行，然后将矩阵逆时针翻转90度，直至打印出全部结果

"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result=[]
        while matrix:
            # extend 在列表末端添加多个值
            result.extend(matrix.pop(0))

            # zip(*list)
            # [1,2],[3,4],[5,6]  -->  [(1, 3, 5), (2, 4, 6)]
            # zip(*list) 顺时针90旋转
            # zip(*list)[::-1]   逆时针90旋转

            matrix=list(map(list,zip(*matrix)))[::-1]
            # print(matrix)
            # print("----------------")
        return result



if __name__ == "__main__":
    temp_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    s = Solution()
    r=s.printMatrix(temp_list)
    print(r)

    # print(list(map(list,zip(*temp_list))))
