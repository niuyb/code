#!/usr/bin/env python
# encoding: utf-8
# author: Ksar4
# date: 2021/9/6 16:21
import copy

class Simple_Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]

    def push(self,x):
        # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)

    def pop(self):
        # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            return self.stack.pop(0)

    def isfull(self):
        return len(self.stack) == self.size
    def isempty(self):
        return len(self.stack) == 0
    def getLen(self):
        return len(self.stack)
    def showStack(self):
        return  self.stack






arr1 = [5,7,4,9]
arr2 = [1,2,3,4]
retList = []

# 定义栈
# 时间复杂度 n^2

stack = Simple_Stack(1000)


# 定义入栈存储结构
# template = {
#     "arrList":[],
#     "retList":[],
#     "tempIndex": int,
#     "maxAbs": int
# }


def findCombo(arrList, retList, stack,maxAbs,tempIndex=1):

    if not arrList:
        return maxAbs

    arrFlag = arr1[tempIndex - 1] > arr1[tempIndex]

    for tempArr in arrList:

        tempFlag = retList[tempIndex - 1] > tempArr

        if tempFlag == arrFlag:
            tempArrList = copy.deepcopy(arrList)
            tempArrList.remove(tempArr)
            tempRetList = copy.deepcopy(retList)
            tempRetList.append(tempArr)


            if len(arr2) == len(tempRetList):
                ret = 0
                for i in range(1, len(tempRetList)):
                    ret += abs(tempRetList[i - 1] - tempRetList[i])
                print "===>", tempRetList, ret
                if maxAbs < ret:
                    maxAbs = ret
                    # return  maxAbs

            # 入栈操作
            tempDict = {
                "arrList": tempArrList,
                "retList": tempRetList,
                "tempIndex": tempIndex + 1,
                "maxAbs": maxAbs
            }
            print "---->",tempDict
            # tempMax = findCombo(tempArrList, tempRetList, maxAbs, tempIndex + 1)
            stack.push(tempDict)

        else:
            continue


def dealStack(stack,maxAbs=0):

    while stack.getLen() > 0:

        DataDict = stack.pop()
        tempAbs = findCombo(stack=stack, **DataDict)
        if  maxAbs < tempAbs:
            maxAbs = tempAbs
    return maxAbs



for topArr in arr2:
    tempArr2 = copy.deepcopy(arr2)
    tempArr2.remove(topArr)
    findCombo(tempArr2, [topArr],stack,0)


retNum = dealStack(stack)
print "stack function ==> ", retNum

