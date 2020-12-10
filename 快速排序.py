#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/8 17:22
# 工具：PyCharm
# Python版本：3.7.0



def quick_sort_back(list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(list) <= 1:
        return list
    else:
        # 将第一个值做为基准
        pivot = list[0]
        for i in list:
            # 将比急转小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准打的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more



def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:
        mid = data[len(data)//2]
        left,right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


if __name__ == "__main__":

    # s= Solution()
    # print(s.reOrderArray([2,3,4,5]))

    print(quick_sort([2,3,4,67,8,9,10,23,45]))