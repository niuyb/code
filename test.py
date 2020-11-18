# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        num = len(array)
        flag = "false"
        if num <= 0:
            return flag
        for i in range(num):
            if len(array[i]) <=0:
                continue
            if array[i][-1] < target or array[i][0] > target:
                continue
            if target in array[i]:
                flag = "true"
                break
        return flag
s = Solution()
while True:
    try:
        input_str = eval(input())
        target = input_str[0]
        array = input_str[1]
        print(s.Find(target, array))
    except:
        break