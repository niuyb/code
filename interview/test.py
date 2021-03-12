#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/3 9:52
# 工具：PyCharm
# Python版本：3.7.0






class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass


# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x)






A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
# A1=["1",1]
A2 = [i for i in A1 if i in A0]
# for s in A0:
#     print(s)
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

# print(A0)
# print(A1)
# print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)




d={'a':24,'g':52,'i':12,'k':33}
d=sorted(d.items(),key = lambda x:x[1])
# print(d)



def multipliers():
 return (lambda x : i * x for i in range(4))

a = (m(2) for m in multipliers())
print(next(a))
print(next(a))
print(next(a))
print(next(a))



# x=1
# b =( i * x for i in range(4))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
