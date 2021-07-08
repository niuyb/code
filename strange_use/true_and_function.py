#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/9 15:27
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
enumerate()
input: ['Spring', 'Summer', 'Fall', 'Winter']

:return [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

"""

"""
effects_ and todoEffects.append(effects_)

只有 effects_ 为 true 
todoEffects.append(effects_) 才会执行

"""

todoEffects=[]
skills=['Spring', 'Summer', 'Fall', 'Winter']
for i, skill in enumerate(skills):
    print  i,skill
    effects_ = i
    effects_ and todoEffects.append(effects_)

print todoEffects
