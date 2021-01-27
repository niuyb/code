#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/27 11:27
# 工具：PyCharm
# Python版本：3.7.0
""""""

"""
冒泡排序
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。
"""

def bubble_sort(lists):
    count =len(lists)
    for i in range(0,count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i],lists[j] =lists[j],lists[i]
    return lists