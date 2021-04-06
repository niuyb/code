#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/6 10:56
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






# def ping():
#     print ("PING")
#     pong()
#
# def pong():
#     print ("PONG")
#     ping()
#
# ping()









import stackless

ping_channel = stackless.channel()
pong_channel = stackless.channel()

def ping():
    while ping_channel.receive(): #在此阻塞
        print "PING"
        pong_channel.send("from ping")

def pong():
    while pong_channel.receive():
        print "PONG"
        ping_channel.send("from pong")

stackless.tasklet(ping)()
stackless.tasklet(pong)()

# 我们需要发送一个消息来初始化这个游戏的状态
# 否则，两个微进程都会阻塞
stackless.tasklet(ping_channel.send)('startup')

stackless.run()