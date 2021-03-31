#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/31 17:02
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
from data_structure.二叉树 import gen_tree, pre_traverse_tree

"""

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

"""


"""
input:  {5,4,#,3,#,2,#,1}

:return  [5,4,3,2,1]

"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            tmp = stack
            stack = []
            for i in tmp:
                res.append(i.val)
                if i.left:
                    stack.append(i.left)
                if i.right:
                    stack.append(i.right)
        return res



