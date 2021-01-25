#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/25 15:00
# 工具：PyCharm
# Python版本：3.7.0



# 队列在表的前端进行删除操作(队头)，后端进行插入操作(队尾)

class Queue():
    def __init__(self,size):
        self.size=size
        self.tail=0
        self.head=0
        self.que = []

    def append(self,data):
        if self.isfull():
            return 'The Queue is full'
        else:
            self.que.append(data)
            self.tail=self.tail+1
            return self.que
    def pop(self):
        if self.isempty():
            return 'The Queue is empty'
        else:
            self.que.pop(0)
            self.head=self.head+1
            return self.que
    def length(self):
        return len(self.que)

    def isfull(self):
        if self.tail-self.head==self.size:
            return True

    def isempty(self):
        if self.tail==self.head:
            return True
    def string(self):
        return str(self.que)
