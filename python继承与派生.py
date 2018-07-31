# -*- coding: utf-8 -*-

class Class1:
    pass

class Class2:
    pass

class SubClass1(Class1):    #单继承，基类是Class1，派生类是SubClass
    pass

class SubClass2(Class2,Class1): #python支持多继承，用逗号分隔开多个继承的类
    pass


SubClass1.__bases__         #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
print (SubClass1.__bases__)

# 1.只有在python2中才分新式类和经典类，python3中统一都是新式类
# 2.在python2中，没有显式的继承object类的类，以及该类的子类，都是经典类
# 3.在python2中，显式地声明继承object的类，以及该类的子类，都是新式类
# 4.在python3中，无论是否继承object，都默认继承object，即python3中所有类均为新式类

print (Class1.__bases__)

class Hero:
    def __init__(self,nickname,aggressivity,life_value):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value

    def move_forward(self):
        print('%s move forward' %self.nickname)

    def move_backward(self):
        print('%s move backward' %self.nickname)

    def move_left(self):
        print('%s move forward' %self.nickname)

    def move_right(self):
        print('%s move forward' %self.nickname)

    def attack(self,enemy):
        enemy.life_value-=self.aggressivity
class Garen(Hero):
    pass

class Riven(Hero):
    pass

g1=Garen('草丛伦',100,300)
r1=Riven('锐雯雯',57,200)

print (g1.life_value)
print (g1.__dict__)
r1.attack(g1)
print (g1.__dict__)
print (Riven.__bases__)
print (g1.life_value)

print (Garen.__mro__)

# ------------------------检测形式类的继承方式---------------------------------------

class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    def test(self):
        print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__)    #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#-----------------------------------子类重用------------------------------
# 方式一：指名道姓，即父类名.父类方法()   (不依赖继承)
# 方式二：super()           （依赖继承）


class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Akl(Hero):
    city = 'Demacia'
    def __init__(self, nickname, life_value, aggresivity, weapon):
        # self.nickname = nickname
        # self.life_value = life_value
        # self.aggresivity = aggresivity
        # Hero.__init__(self,nickname,life_value,aggresivity) # 指名道姓
        super().__init__(nickname,life_value,aggresivity)       #super 方法
        self.weapon = weapon

class Riven(Hero):
    city = 'Noxus'

akl = Akl('暗影之拳', 100, 30, 'knife')
riven = Riven('锐萌萌', 100, 30)
print(akl.__dict__)

#根据继承关系判断输出
class C1:
    def fun1(self):
        print('form c1')
        super().fun1()   # 基于最底下子类的mor顺序查找
class C2:
    def fun1(self):
        print('form c2')

class B2(C2):
    def fun1(self):
        print('form B2')

class B1(C1):
    def fun1(self):
        print('from B1')
        super().fun1()

class A(B1, B2):
    pass

print(A.__mro__)
a = A()
a.fun1()