#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/1/25 14:52
# 工具：PyCharm
# Python版本：3.7.0
""""""




"""
①堆通常是一个可以被看做一棵树的数组对象。堆总是满足下列性质：

 
   ·堆中某个节点的值总是不大于或不小于其父节点的值；

 
   ·堆总是一棵完全二叉树。

将根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常见的堆有二叉堆、斐波那契堆等。


②堆是在程序运行时，而不是在程序编译时，申请某个大小的内存空间。即动态分配内存，对其访问和对一般内存的访问没有区别。

③堆是应用程序在运行的时候请求操作系统分配给自己内存，一般是申请/给予的过程。

④堆是指程序运行时申请的动态内存，而栈只是指一种使用堆的方法(即先进后出)。







栈：什么是栈？又该怎么理解呢？

①栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。这一端被称为栈顶，相对地，把另一端称为栈底。

②栈就是一个桶，后放进去的先拿出来，它下面本来有的东西要等它出来之后才能出来（先进后出）

③栈(Stack)是操作系统在建立某个进程时或者线程（在支持多线程的操作系统中是线程）为这个线程建立的存储区域，该区域具有FIFO的特性，在编译的时候可以指定需要的Stack的大小。






堆栈：什么是堆栈？又该怎么理解呢？

注意：其实堆栈本身就是栈，只是换了个抽象的名字。

堆栈的特性： 最后一个放入堆栈中的物体总是被最先拿出来， 这个特性通常称为后进先出(LIFO)队列。 堆栈中定义了一些操作。 两个最重要的是PUSH和POP。 PUSH操作在堆栈的顶部加入一 个元素。POP操作相反， 在堆栈顶部移去一个元素， 并将堆栈的大小减一。

"""





















class Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1

    def push(self,x):
        # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top=self.top+1

    def pop(self):
        # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top+1 == self.size
    def isempty(self):
        return self.top == '-1'
    def showStack(self):
        print(self.stack)






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
            # self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return len(self.stack) == self.size
    def isempty(self):
        return len(self.stack) == 0
    def showStack(self):
        print(self.stack)






class BinaryHeap(object):
    """一个二叉堆, 小顶堆 利用列表实现"""

    def __init__(self, max_size=math.inf):
        pass

    def __len__(self):
        """求长度"""
        pass

    def insert(self, *data):
        """向堆中插入元素"""
        pass

    def _siftup(self):
        """最后插入的元素上浮"""
        pass

    def _siftdown(self, idx):
        """序号为i的元素下沉"""
        pass

    def get_min(self):
        pass

    def delete_min(self):
        """删除堆顶元素"""
        pass

    def create_heap(self, data):
        """直接创建一个小顶堆, 接收一个可迭代对象参数,效果同insert, 效率比insert一个个插入高,时间复杂度为n"""
        pass

    def clear(self):
        """清空堆"""
        pass

    def update_key(self, idx, key):
        """更新指定位置的元素, idx>=1"""
        pass

    def delete_key(self, idx):
        """删除指定位置的元素, idx>=1"""
        pass
