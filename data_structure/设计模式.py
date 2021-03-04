#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/4 9:26
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
""""""


""" 1 ---------------单例--------------- """

class A(object):
    __instance = None
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

class Singleton(object):
     def __init__(self):
         pass

     def __new__(cls, *args, **kwargs):
         if not hasattr(Singleton, "_instance"): # 反射
             Singleton._instance = object.__new__(cls)
         return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()

"""
单例模式的应用场景有哪些？
单例模式应用的场景一般发现在以下条件下：
（1）资源共享的情况下,避免由于资源操作时导致的性能或损耗等。如日志文件,应用配置。
（2）控制资源的情况下,方便资源之间的互相通信。如线程池等。 1.网站的计数器 2.应用配置 3.多线程池 4. 数据库配置,数据库连接池 5.应用程序的日志应用....
"""


"""
工厂模式与建造者模式区别

工厂模式注重的是整体对象的创建方法,而建造者模式注重的是对象的创建过程,创建对象的过程方法可以在创建时自由调用。

"""



""" ---------------2 工厂---------------"""

"""
工厂模式是一个在软件开发中用来创建对象的设计模式。

工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象,而不是决定哪个对象可以被创建。

为了实现此方法,需要创建一个工厂类创建并返回。 

当程序运行输入一个“类型”的时候,需要创建于此相应的对象。这就用到了工厂模式。在如此情形中,实现代码基于工厂模式,可以达到可扩展,可维护的代码。当增加一个新的类型,不在需要修改已存在的类,只增加能够产生新类型的子类。

简短的说,当以下情形可以使用工厂模式：
1.不知道用户想要创建什么样的对象

2.当你想要创建一个可扩展的关联在创建类与支持创建对象的类之间。

一个例子更能很好的理解以上的内容：

我们有一个基类Person ,包涵获取名字,性别的方法 。有两个子类male 和female,可以打招呼。还有一个工厂类。
 工厂类有一个方法名getPerson有两个输入参数,名字和性别。
 用户使用工厂类,通过调用getPerson方法。
在程序运行期间,用户传递性别给工厂,工厂创建一个与性别有关的对象。因此工厂类在运行期,决定了哪个对象应该被创建


根据不同的参数生成不同的对象,重点在生成

"""

class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)
        super().__init__()

class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)
        super().__init__()

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
                return Male(name)
        if gender == 'F':
            return Female(name)

factory = Factory()
person = factory.getPerson("Chetan", "M")


""" 3 ---------------建造者模式---------------"""

"""
将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示。

相关模式：思路和模板方法模式很像,模板方法是封装算法流程,对某些细节,提供接口由子类修改,建造者模式更为高层一点,将所有细节都交由子类实现

一个例子更能很好的理解以上的内容：

1. 有一个接口类,定义创建对象的方法。一个指挥员类,接受创造者对象为参数。两个创造者类,创建对象方法相同,内部创建可自定义

2.一个指挥员,两个创造者(瘦子 胖子),指挥员可以指定由哪个创造者来创造

"""

from abc import ABCMeta, abstractmethod

class Builder():
    __metaclass__ = ABCMeta
    """简单的说ABCMeta就是让你的类变成一个纯虚类,子类必须实现某个方法,这个方法在父类中用@abc.abstractmethod修饰"""
    """用于程序接口的控制,正如上面的特性,含有@abstractmethod修饰的父类不能实例化,但是继承的子类必须实现@abstractmethod装饰的方法"""
    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Thin(Builder):
    def draw_left_arm(self):
        print('画左手')

    def draw_right_arm(self):
        print( '画右手')

    def draw_left_foot(self):
        print ('画左脚')

    def draw_right_foot(self):
        print( '画右脚')

    def draw_head(self):
        print( '画头')

    def draw_body(self):
        print( '画瘦身体')


class Fat(Builder):
    def draw_left_arm(self):
        print ('画左手')

    def draw_right_arm(self):
        print ('画右手')

    def draw_left_foot(self):
        print ('画左脚')

    def draw_right_foot(self):
        print ('画右脚')

    def draw_head(self):
        print ('画头')

    def draw_body(self):
        print ('画胖身体')


class Director():
    def __init__(self, person):
        self.person=person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()


thin=Thin()
fat=Fat()
director_thin=Director(thin)
director_thin.draw()
director_fat=Director(fat)
director_fat.draw()



""" 4 ---------------原型模式---------------"""

"""
用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象。
原型模式本质就是克隆对象,所以在对象初始化操作比较复杂的情况下,很实用,能大大降低耗时,提高性能,因为“不用重新初始化对象,而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝,而字段引用的对象不会被拷贝,拷贝的对象和源对象只是名称相同,但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
"""