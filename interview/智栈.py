#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/13 11:49
# 工具：PyCharm
# Python版本：3.7.0
""""""
import copy


"""
第一题

某企业拥有4条流⽔⽣产线A、B、C、D，每条流⽔线⽬前每⽉的⽣产量在10、7、
5、4吨。现企业需要优化各流⽔线，故实⾏每⽉末从⽣产最多的流⽔线中抽出3吨
的⽣产⼒，分配到剩余的3条流⽔线⾥，既其余每条流⽔线多⽣产1吨，这称为⼀次
⽣产⼒优化（既经过第⼀个⽉后的优化，各流⽔线⽣产吨数在：7、8、6、5）
那么请问，经过五年的⽣产⼒优化调整后，哪个流⽔线⽣产⼒最⾼，可每⽉⽣产多
少吨
编程求解该问题，并思考是否为最优解。

"""



"""
思路:
找最大生产力的值
找最大打生产线
最大生产线 -3 
其余生产力 +1 
执行 5* 12 次

"""

if __name__ == "__main__1":
    p_dict = {
        "a": 10,
        "b": 7,
        "c": 5,
        "d": 4
    }


    for _ in range(5*12 - 1):
        # 找最大
        max_index = max(p_dict, key=lambda k: p_dict[k])
        for key in p_dict.keys():
            if key == max_index:
                p_dict[key] -=3
            else:
                p_dict[key] += 1

    # 输出结果
    max_index = max(p_dict, key=lambda k: p_dict[k])
    print("最高生产力:",max_index,"每月{}吨".format(p_dict[max_index]))

"""
优化思路:
观察发现 
在第一次分配生产力之后
四个月一循环

即 第5年分配生产力与 第3个月分配生产力 结果相同

故只需执行四次

对比上例,减少了大量的循环

"""





"""
第⼆题

给定⼀个数组，例如[15, 2, 8, 13]，找到符合下⾯⽅式的结果，并打印出来
例如：
1）从数组每位元素当前位置开始，往后找到⼤于⾃⼰本身的第⼀位元素，并返回
1）如果没有找到，返回-1
结果如下
15 -> -1
2 -> 8
8 -> 13
13 -> -1
返回结果：
要求：写出解题思路并给出时间复杂度，并说明最坏情况（可考虑栈)

"""


"""
思路1:
结果集的key 为列表各个元素
从后向前寻找遍历每个元素
若该元素大于key 更新结果集
直到列表倒叙遍历完毕


思路2:
结果集的key 为列表各个元素
从前向后遍历每个元素
在元素剩余结果中找出第一个大于key的值并且保存到结果集 break
直到列表遍历完毕


思路2可以比思路1 少做判断
下列代码为思路2 的代码实现

时间复杂度 O(n*n)

"""

if __name__ == "__main__1":

    temp_list = [15, 2, 8, 13]
    # 结果集
    result_dict=dict(zip(temp_list,[-1]*len(temp_list)))
    # 遍历元素
    for index in range(len(temp_list)):
        # 遍历剩余元素
        for key in temp_list[index:]:
            # 判断
            if temp_list[index] < key:
                result_dict[temp_list[index]] = key
                break

    # 输出结果
    for key,values in result_dict.items():
        print(key,"-->",values)


"""
有⼀段12组成的字符串，例如"1212111212"，可进⾏0或多次的⼀下规律：从某⼀位
置分隔成两个字符串，两个字符串同时翻转后在拼接。找出最⻓的连续12相间的⻓度
~~ 
例如: 
1212111212  假设从第五、六位分隔 12121, 11212 翻转后 12121 , 21211 拼接后
1212121211 这个时候的连续12相间的⻓度为9，也是最⻓的连续12相间的

"""


"""
思路:
按位数切割数组
反转字符串元素,组合
按固定字符串分割组合字符串
根据分割字符串列表找出最大数组

"""


if __name__ == "__main__1":


    def find_max_len(match_str,p_str,split_index=5):
        max_len=0
        index = 0
        #反转字符串
        temp_str2 = match_str[split_index:]
        temp_str1 = match_str[:split_index]
        fin_str = temp_str1[::-1] + temp_str2[::-1]
        # 处理特殊情况
        if fin_str.find(p_str) <0 :
            return 0
        temp_fin_list = fin_str.split(p_str)
        # 匹配最长字符串
        for i in range(len(temp_fin_list)-1):
            per_num = 0
            if temp_fin_list[i] == "":
                index += 1
                # 判断下一元素
                if temp_fin_list[i+1] != "":
                    # 找出元素内符合字符串的长度
                    for per in range(1,len(p_str)):
                        if temp_fin_list[i + 1][:per] == p_str[:per]:
                            per_num += 1
                temp_max = index * len(p_str) + per_num
                max_len = temp_max if max_len < temp_max else max_len
            else:
                index = 0
        return max_len



    match_str = "1212111212"
    p_str = "12"
    split_index=5

    max_len = find_max_len(match_str,p_str,split_index)
    print("最长长度为%d"%max_len)



"""
有两组数，第⼀组数顺序固定，请编程实现让第⼆组数 相邻数字间的⼤⼩关系和第⼀
组数相同，且第⼆组相邻数字间的差值之和最⼤
下⾯给出⼀个示例
第⼀组数： 5 7 4 9 
第⼆组数：1 2 3 4 
第⼆组数排序结果：2 4 1 3 
第⼆组数排序后的差值之和：7 = abs(2-4) + abs(4-1) + abs(1-3)

"""

"""
思路:
找出数字间相邻大小关系
列出所有组合情况
筛选出最大差值情况

"""
if __name__ == "__main__":

    def all_sorted(l_list):
        len_list = len(l_list)
        if len_list == 1:
            return l_list
        result = []
        for i in range(len_list):
            res_list = l_list[:i] + l_list[i + 1:]
            s = l_list[i]
            per_result = all_sorted(res_list)
            if len(per_result) == 1:
                result.append(l_list[i:i + 1] + per_result)
            else:
                result += [[s] + j for j in per_result]
        return result

    def math_sort(f_list,s_list):
        jud_str ="{}"
        f_dict = dict(zip([i for i in range(len(f_list))],f_list))

        result_list= []
        max_abs = 0

        # 总结相邻大小关系
        for key, value in f_dict.items():
            if f_dict.get(key + 1, None):
                if value == max(value, f_dict.get(key + 1)):
                    jud_str += '>{}'
                else:
                    jud_str += '<{}'
        # 所有情况
        all_list = all_sorted(s_list)
        #找出最大差值情况
        for temp_list in all_list:
            temp_str = jud_str.format(*temp_list)
            if eval(str(temp_str)):
                temp_abs = 0
                for index in range(len(temp_list)-1):
                    temp_abs += abs(temp_list[index]-temp_list[index+1])
                if temp_abs > max_abs:
                    max_abs = temp_abs
                    result_list = temp_list
            else:
                pass
        return max_abs,result_list


    # 输出结果
    max_abs,result_list = math_sort([5,7,4,9],[1,2,3,4])
    print(max_abs,result_list)



#     ===========================方法二 动态规划==================================

    arr1 = [5, 7, 4, 9]
    arr2 = [1, 2, 3, 4]



    # arrFlag
    # > true
    # < false

    def findCombo(arrList, retList, maxAbs, tempIndex=1):
        if not arrList:
            if len(arr2) == len(retList):
                ret = 0
                for i in range(1, len(retList)):
                    ret += abs(retList[i - 1] - retList[i])

                print "===>", retList, ret
                if maxAbs < ret:
                    return ret
                else:
                    return None
            return None

        arrFlag = arr1[tempIndex - 1] > arr1[tempIndex]

        for tempArr in arrList:

            tempFlag = retList[tempIndex - 1] > tempArr

            if tempFlag == arrFlag:
                tempArrList = copy.deepcopy(arrList)
                tempArrList.remove(tempArr)
                tempRetList = copy.deepcopy(retList)
                tempRetList.append(tempArr)
                tempMax = findCombo(tempArrList, tempRetList, maxAbs, tempIndex + 1)
                if isinstance(tempMax, int):
                    maxAbs = tempMax
                else:
                    continue
        return maxAbs


    maxAbs = 0
    for topArr in arr2:
        tempArr2 = copy.deepcopy(arr2)
        tempArr2.remove(topArr)
        maxAbs = findCombo(tempArr2, [topArr], maxAbs)
    print "最大为", maxAbs

    #     ===========================方法三 栈代替递归==================================
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






    # arr1 = [5,7,4,9]
    # arr2 = [1,2,3,4]
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




















