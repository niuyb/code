#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/11 10:40
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



import copy
var = {"k1":1,"k2":2,"k3":[1,2,3]}
var1 = copy.deepcopy(var)
print(var)
#{'k1': 1, 'k2': 2, 'k3': [1, 2, 3]}
var1["k1"] = 100
print(var1)
#{'k1': 100, 'k2': 2, 'k3': [1, 2, 3]}
var1["k3"].append(4)
print(var)
#{'k1': 1, 'k2': 2, 'k3': [1, 2, 3]}
print(var1)
#{'k1': 100, 'k2': 2, 'k3': [1, 2, 3, 4]}
"""
结论：字典套列表情形，
做深拷贝时，
对可变类型的列表做赋值改变，不影响原来的数据，因为变量的内存地址不一样
对不可变类型的数字做赋值改变，不影响原来的数据，因为变量的内存地址不一样
因此，这种情况下，深拷贝保证了原来数据的完整性。因为变量的内存地址不一样
"""
var2 = copy.copy(var)
print(var)
#{'k1': 1, 'k2': 2, 'k3': [1, 2, 3, 2500]}
var2["k1"] = 250
var2["k3"].append(2500)
print(var2)
#{'k1': 250, 'k2': 2, 'k3': [1, 2, 3, 2500]}
"""
结论：字典套列表情形，
做浅拷贝时，
对不可变类型的数字做赋值改变，不影响原来的数据，说明变量的内存地址不同。
对可变类型的列表做赋值改变，影响原来的数据，说明可变类型的变量和原来的可变类型的变量内存地址相同。
"""

