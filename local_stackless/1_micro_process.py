#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/2 14:57
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


import stackless


def print_x(x):
    print(x)

stackless.tasklet(print_x)('one')
# <local_stackless.tasklet object at 0x00A45870>
stackless.tasklet(print_x)('two')
# <local_stackless.tasklet object at 0x00A45A30>
stackless.tasklet(print_x)('three')
# <local_stackless.tasklet object at 0x00A45AB0>

stackless.run()


