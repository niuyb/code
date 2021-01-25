#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/8 16:10
# 工具：PyCharm
# Python版本：3.7.0
""""""



"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""


"""


"""


class Solution:
    def reOrderArray(self, array):
        # 类似于快速排序 根据index交换值
        for i in range(1, len(array)):
            if array[i] % 2 == 1:
                j = i - 1
                value = array[i]
                while j >= 0:
                    if array[j] % 2 == 0:
                        array[j+1] = array[j]
                    else:
                        break
                    j -= 1
                array[j+1] = value
        return array

    def reOrderArray_1(self , array ):
        odd = []
        even = []
        for i in array:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        for j in even:
            odd.append(j)
        return odd



if __name__ == "__main__":

    s= Solution()
    print(s.reOrderArray([2,3,4,5]))