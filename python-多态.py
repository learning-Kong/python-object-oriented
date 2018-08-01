# -*- coding:utf-8 -*-

import abc

#多态：同一类事物的多种形态
class Animal(metaclass=abc.ABCMeta):     #同一类事物：动物
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal):           #动物的形态之一：人
    def talk(self):
        print ('people say')

class Dog(Animal):          #动物形态之二：狗
    def talk(self):
        print('dog say')

class Cat(Animal):          # 动物形态之三：猫
    def talk(self):
        print('cat say')

class Pig(Animal):          #可自由添加类，动物形态之四：猪
    def talk(self):
        print ('pig say')

# 多态性：指的是可以在不考虑对象类型的情况下而直接使用对象

alex = People()
dog1 = Dog()
tom = Cat()
pig1 = Pig()        #自动添加对象

#peo、dog、pig都是动物,只要是动物肯定有talk方法
#于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
alex.talk()
dog1.talk()
tom.talk()


#更进一步,我们可以定义一个统一的接口来使用
def func(obj):          #同一个接口
    obj.talk()

func(alex)
func(dog1)
func(tom)
func(pig1)          #自定义添加调用