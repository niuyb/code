#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/27 9:32
# 工具：PyCharm
# Python版本：3.7.0
""""""
from data_structure.二叉树 import gen_tree

"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

"""

"""
{8,8,#,9,#,2,#,5},{8,9,#,2}


true
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return False

        return self.helper(pRoot1, pRoot2)

    def helper(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False

        temp = self.helper(pRoot1.left, pRoot2) or self.helper(pRoot1.right, pRoot2)
        if pRoot1.val != pRoot2.val:
            return temp
        else:
            return (self.helper(pRoot1.left, pRoot2.left) and self.helper(pRoot1.right, pRoot2.right)) or temp


if __name__ == "__main__":

    tree1 = gen_tree(list(range(1, 8)))
    tree2 = gen_tree(list(range(1, 4)))
    s = Solution()

    k = s.HasSubtree(tree1,tree2)
    print(k)












