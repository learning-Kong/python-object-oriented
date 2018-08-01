# -*- coding:utf-8 -*-

#python 中的隐藏属性

class A:
    __x = 100       #类的私有数据属性
    y = 200
    def __init__(self,name):
        self.__name = name  #对象的私有属性
    def __foo(self):    #类的私有方法
        print ('run foo')

print(A.y)
print (A.__dict__)
print(A._A__x)

a = A('Kong')
print(a.__dict__)

#-------------------------------- 私有方法的实质--------------------------------
#其实仅仅是一种变形操作
#类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：
#这类形变的特点：
#       1.在类的外部无法直接使用obj.__AttrName
#       2.在类内部可以直接使用obj.__AttrName
#       3.子类无法覆盖父类__开头的属性
# eg：
class A:
    __N=0 #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
    def __init__(self):
        self.__X=10 #变形为self._A__X
    def __foo(self): #变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo() #只有在类内部才可以通过__foo的形式访问到.

#A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形

#-----------------------------------封装的意义-----------------------------------------

#封装数据属性，明显区分内外
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def tell_info(self):
        print('%s - %s'%(self.__name, self.__age))
    def set_info(self,name,age):
        self.__name = name
        self.__age = age
p = People('kong',23)
print(People.__dict__)
print(p.__dict__)
p.tell_info()

p.set_info('jack',33)
print (People.__dict__)
print(p.__dict__)
p.tell_info()

#封装方法：目的是隔离复杂度
#取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱
#对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做
#隔离了复杂度,同时也提升了安全性

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()
