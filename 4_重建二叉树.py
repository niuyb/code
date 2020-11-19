#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/18 16:19
# 工具：PyCharm
# Python版本：3.7.0

""""""
from 二叉树 import gen_tree, pre_traverse_tree

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.l_node = None
        self.r_node = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not len(pre):
            return None
        root = TreeNode(pre[0])
        #  index() 方法检测字符串中是否包含子字符串 str
        index = tin.index(pre[0])
        root.l_node = self.reConstructBinaryTree(pre[1:index+1], tin[0:index])
        root.r_node = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root


if __name__ == "__main__":

    per_tree = gen_tree([1,2,5,3,4,6,7])
    # in_tree = gen_tree([4,7,2,1,5,3,8,6])


    s = Solution()
    re_tree=s.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])

    print(list(pre_traverse_tree(per_tree)))
    print(list(pre_traverse_tree(re_tree)))













