#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/1 17:10
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
from data_structure.二叉树 import gen_tree

"""

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""




"""
input {8,6,10,5,7,9,11}

out [[8],[6,10],[5,7,9,11]]


"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        res = []
        if not root:return res
        queue = [root]
        print(len(queue),queue)
        while queue:
            temp = []
            for _ in range(len(queue)):
                print("_______",_)
                cur = queue.pop(0)
                temp.append(cur.value)
                if cur.l_node:queue.append(cur.l_node)
                if cur.r_node:queue.append(cur.r_node)
            res.append(temp)
        return res




if __name__ =="__main__":

    tree = gen_tree(list(range(1,8)))
    s = Solution()
    print(s.Print(tree))
