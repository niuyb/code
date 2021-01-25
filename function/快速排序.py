#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/12/8 17:22
# 工具：PyCharm
# Python版本：3.7.0
import random


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



def quick_sort_back2(data):
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




# def quick_sort(nums: list, left: int, right: int) -> None:
def quick_sort(nums,left,right):
    if left < right:
        i = left
        j = right
        # 取第一个元素为游标
        pivot = nums[left]
        while i != j:
            # 交替扫描和交换
            # 从右往左找到第一个比枢轴量小的元素，交换位置
            while j > i and nums[j] > pivot:
                j -= 1
            if j > i:
                # 如果找到了，进行元素交换
                nums[i] = nums[j]
                i += 1
            # 从左往右找到第一个比枢轴量大的元素，交换位置
            while i < j and nums[i] < pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        # 至此完成一趟快速排序，枢轴量的位置已经确定好了，就在i位置上（i和j)值相等
        nums[i] = pivot
        # 以i为枢轴进行子序列元素交换
        quick_sort(nums, left, i-1)
        quick_sort(nums, i+1, right)
    else:
        return False

if __name__ == "__main__":

    # s= Solution()
    # print(s.reOrderArray([2,3,4,5]))

    # print(quick_sort([2,3,4,67,8,9,10,23,45]))

    data = [random.randint(1, 100) for _ in range(10)]
    print(data)
    quick_sort(data, 0, len(data) - 1)
    print(data)