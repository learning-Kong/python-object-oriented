# -*- coding: utf-8 -*-

class Student:
    school='CUIT'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print ('haha')
    def learn(self):
        print('%s is learning' % self.name)
    def eat(self):
        print('is eating' % self.name)
    def sleep(self):
        print ('is sleeping' % self.name)

s1 = Student('kong','male',23)

Student.learn(s1)
s1.learn()  #等同于Student.learn(s1)

print (s1.__dict__)

#练习1：编写一个学生类，产生一堆学生对象
class Student1:
    num=0
    def __init__(self):
        Student1.num+=1
s1 = Student1()
s2 = Student1()
s3 = Student1()
print(Student1.num)

# 练习2：模仿王者荣耀定义两个英雄类， (10分钟)
class Hero:
    def __init__(self,name,attack,blood):
        self.name = name
        self.attack = attack
        self.blood = blood

    def fight(self,attacker):
        self.blood -= attacker.attack
        print (self.blood)
    def __del__(self):  #对象实例调用完类时会被调用
        if self.blood <= 0:
            print ('%s is died' % self.name)

s1 = Hero('kong',100,200)
s2 = Hero('luo',2,100)
s1.fight(s2)
s2.fight(s2)
