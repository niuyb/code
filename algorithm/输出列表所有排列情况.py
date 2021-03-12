#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/12 11:01
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


def all_sorted(li):
    len_list = len(li)
    if len_list == 1:
        return li
    result = []
    for i in range(len_list):
        res_list = li[:i] + li[i + 1:]
        print(li[:i],li[i + 1:])
        s = li[i]
        per_result = all_sorted(res_list)
        if len(per_result) == 1:
            print("aaaaa",li[i:i + 1] + per_result)
            result.append(li[i:i + 1] + per_result)
        else:
            print("bbbb",[[s] + j for j in per_result])
            result += [[s] + j for j in per_result]

        print("resres",result)
    return result



if __name__ == "__main__":
    all_sorted([1,2,3,4])
