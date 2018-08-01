# -*- coding:utf-8 -*-

# 方法当做属性调用

class People:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


p = People('kong',60,170)

print (p.bmi)       # 类的特征方法转换为类的数据属性，调用的时候
#p.bmi = 3333  # 不能赋值，不是真的数据属性

#-----------------------------------setter 和 deleter方法---------------------------
class People:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            print ('name must be str')
            return
        else:
            self.__name = name
    @name.deleter
    def name(self):
        print ('Not allow delete')

p = People('Kong')
print (p.name)
p.name = 14
p.name = 'KONG'
print (p.__dict__)
print(p.name)
del p.name