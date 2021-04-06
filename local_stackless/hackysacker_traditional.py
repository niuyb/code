#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/4/6 11:06
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






import thread
import random
import sys
import Queue

class hackysacker:
    counter = 0
    def __init__(self,name,circle):
        self.name = name
        self.circle = circle
        circle.append(self)
        self.messageQueue = Queue.Queue()

        thread.start_new_thread(self.messageLoop,())

    def incrementCounter(self):
        hackysacker.counter += 1
        if hackysacker.counter >= turns:
            while self.circle:
                hs = self.circle.pop()
                if hs is not self:
                    hs.messageQueue.put('exit')
            sys.exit()

    def messageLoop(self):
        while 1:
            message = self.messageQueue.get()
            if message == "exit":
                debugPrint("%s is going home" % self.name)
                sys.exit()
            debugPrint("%s got hackeysack from %s" % (self.name, message.name))
            kickTo = self.circle[random.randint(0,len(self.circle)-1)]
            debugPrint("%s kicking hackeysack to %s" % (self.name, kickTo.name))
            self.incrementCounter()
            kickTo.messageQueue.put(self)

def debugPrint(x):
    if debug:
        print x

debug=1
hackysackers=5
turns = 5

def runit(hs=10,ts=10,dbg=1):
    global hackysackers,turns,debug
    hackysackers = hs
    turns = ts
    debug = dbg

    hackysacker.counter= 0
    circle = []
    one = hackysacker('1',circle)

    for i in range(hackysackers):
        hackysacker(`i`,circle)

    one.messageQueue.put(one)

    try:
        while circle:
            pass
    except:
        #有时我们在清理过程中会遇到诡异的错误。
        pass

if __name__ == "__main__":
    # print hackysacker.counter
    runit(dbg=1)