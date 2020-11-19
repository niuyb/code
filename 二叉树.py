#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/19 9:26
# 工具：PyCharm
# Python版本：3.7.0
from collections import deque


class TreeNode:
    def __init__(self, value, l_node = None, r_node = None):
        # l_node: TreeNode = None, r_node: TreeNode = None
        self.value = value
        self.l_node = l_node
        self.r_node = r_node


def gen_tree(values):
    # (values: list) -> Union[TreeNode, None]
    if not values:
        return None
    iter_value = iter(values)
    root = TreeNode(next(iter_value))
    d = deque()
    d.append(root)
    while 1:
        head = d.popleft()
        try:
            head.l_node = TreeNode(next(iter_value))
            d.append(head.l_node)
            head.r_node = TreeNode(next(iter_value))
            d.append(head.r_node)
        #next()迭代器完成会引发StopIteration异常
        except StopIteration:
            break
    return root


def pre_traverse_tree(node):
    # node: TreeNode
    if node is None:
        return
    yield node.value
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)


def in_traverse_tree(node):
    # node: TreeNode
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield node.value
    yield from pre_traverse_tree(node.r_node)


def post_traverse_tree(node):
    # node: TreeNode
    if node is None:
        return
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)
    yield node.value


tree = gen_tree(list(range(10)))
# print(tree)

print(list(pre_traverse_tree(tree)))
print(list(in_traverse_tree(tree)))
print(list(post_traverse_tree(tree)))


"""前序遍历"""

""" node1  0  node2"""

""" node3  1  node4   node2"""

""" node7  3  node8   node4  node2"""

""" 7  8   node4  node2"""

""" node9  4   none   node2"""

""" 9  node2"""

""" node5  2  node6"""

""" 5   6  """

""" 数字出现次序就是前序遍历过程"""
"""
前序遍历：根结点 —> 左子树 —> 右子树（先遍历根节点，然后左右）
    yield node.value
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)

中序遍历：左子树—> 根结点 —> 右子树（在中间遍历根节点）
    yield from pre_traverse_tree(node.l_node)
    yield node.value
    yield from pre_traverse_tree(node.r_node)

后序遍历：左子树 —> 右子树 —> 根结点（最后遍历根节点）
    yield from pre_traverse_tree(node.l_node)
    yield from pre_traverse_tree(node.r_node)
    yield node.value

"""




"""
gen_tree建立树顺序

1234567


   1
  2  3
4 5  6 7

前序

    1
  2   5
3  4 6  7
 
中序
    4
   1  5
 2 3 6 7

后序
    7
  3   6
 1 2 4 5
"""