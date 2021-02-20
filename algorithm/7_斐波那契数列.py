#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2020/11/20 9:44
# 工具：PyCharm
# Python版本：3.7.0

""""""


"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39

"""


class Solution:
    def Fibonacci(self, n):
        nums=[]
        x = [x for x in range(n+1)]
        for index in x:
            # print(index)
            if index==0 or index==1:
                nums.append(index)
            else:
                nums.append(nums[-1]+nums[-2])

        return nums[-1],nums



    def recur_fibo(self,n):
       """递归函数
       输出斐波那契数列"""
       if n <= 1:
           # print(n)
           return n
       else:
           # print(n-1,n-2)
           return(self.recur_fibo(n-1) + self.recur_fibo(n-2))


    def fibo(self):
        nterms = int(input("您要输出几项? "))

        # 检查输入的数字是否正确
        if nterms <= 0:
            print("输入正数")
        else:
            print("斐波那契数列:")
            for i in range(1,nterms+1):
                print(self.recur_fibo(i))


    # def recur_fibo(self,n):
    #    """递归函数
    #    输出斐波那契数列"""
    #    out_list=[]
    #    if n <= 1:
    #        print(n)
    #        out_list.append(n)
    #        print(out_list)
    #        return n
    #    else:
    #        # print(n-1,n-2)
    #        return(self.recur_fibo(n-1) + self.recur_fibo(n-2))


if __name__ == "__main__":

    s = Solution()
    # num,num_list=s.Fibonacci(10)
    # print(num,num_list)

    # fib=s.recur_fibo(7)
    # print(fib)

    s.fibo()
