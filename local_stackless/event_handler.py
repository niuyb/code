#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/6 16:11
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


import  stackless


class EventHandler:
    def __init__(self,*outputs):
        if outputs==None:
            self.outputs=[]
        else:
            self.outputs=list(outputs)

        self.channel = stackless.channel()
        stackless.tasklet(self.listen)()

    def listen(self):
        while 1:
            val = self.channel.receive()
            self.processMessage(val)
            for output in self.outputs:
                self.notify(output)

    def processMessage(self,val):
        pass

    def notify(self,output):
        pass

    def registerOutput(self,output):
        self.outputs.append(output)

    def __call__(self,val):
        self.channel.send(val)