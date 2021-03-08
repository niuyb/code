#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/4 13:18
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
python 私有属性的访问   
__age 无法访问

方法age 返回 

property装饰器  
装饰器之后可以当做普通属性进行访问

"""
class person:
 def __init__(self,x):
    self.local_age="aaa"
    self.__age = 10
 def age(self):
    return self.__age

 # def __setattr__(self,name,value):
 #     self.name = value
 @property
 def get_age(self):
     return self.__age

t = person(22)
# 私有属性访问不到
t.__age = 100
print(t.local_age)
print(t.age())
print(t.get_age)
# 私有属性无法修改
setattr(t,"__age","new")
setattr(t,"local_age","bbb")
print(t.local_age)
print(t.get_age)
