#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/2 10:03
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
动态规划原理
动态规划算法将待求解问题拆分成一系列相互交叠的子问题，通过递推关系定义各子问题的求解策略，并随时记录子问题的解，最终获得原始问题的解，避免了对交叠子问题的重复求解。

动态规划要领
在动态规划算法中有三要素，即最优子结构、边界和状态转移函数。
最优子结构：每个阶段的最优状态可以从之前某个阶段的某个或某些状态直接得到；
边界：问题最小子集的解；
状态转移函数：从一个阶段向另一个阶段过渡的具体模式，描述的是两个相邻子问题之间的关系。





我所理解的动态规划，就两个词：动态、规划。
动态我自己理解为：一个问题可以拆分为若干个子问题，然后通过逐步递推，得到最终的结果。
规划就是最优问题，整体的最优细分到每个递推环节的最优。

"""


"""
题目描述：一个人去偷东西，他的背包容量最大为20kg，然后有重量、价值不等的物品，比如重量为2、价值为3的物品，每件物品只能拿一件，求小偷能偷到的物品最大的价值。


物品重量与价值对应关系：
w   v
2   3
3   4
5   8
9   10
背包容量：20
"""

"""
物品重量与价值对应关系：
w   v
2   3
3   4
5   8
9   10
背包容量：20
"""


import numpy as np
def func(pack, cap):
    max_value_arr = np.zeros([len(pack)+1, cap+1])
    print(max_value_arr)
    # 第一列与第一排全为0，这样为后续能递推max_value_arr的值
    max_value_arr[:,0] = 0
    max_value_arr[0,:] = 0
    # i代表pack物品的序号
    for i in range(1, len(pack)+1):
        # j代表包中剩余的空间
        for j in range(1, cap+1):
            # 第一种情况，包中剩余空间不足
            if j < pack[i-1][0]:
                max_value_arr[i, j] = max_value_arr[i-1, j]
            # 第二种情况，包中空间足够
            else:
                # a代表放入当前物品后包中总价值，w是当前物品的所占空间
                w = pack[i-1][0]
                """
                下面这行是关键！！！为什么是i-1，这里必须用i-1才能推出当前的max_value_arr的值，
                然后再加上单独的value
                """
                a = max_value_arr[i-1, j-w] + pack[i-1][1]
                # b代表不放当前物品包中的总价值，两者求最大值
                b = max_value_arr[i-1, j]
                max_value_arr[i, j] = max(a, b)

    print(max_value_arr[-1, -1])


test_pack = [[2, 3],
             [3, 4],
             [4, 5],
             [5, 8],
             [9, 10]]


# func(test_pack, 20)




"""
最小路径和（Leetcode64）
题目描述：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。注意：每次只能向下或者向右移动一步。


输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""



def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j == 0:
                continue
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[-1][-1]


print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))











