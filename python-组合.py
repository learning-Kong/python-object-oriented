# -*- coding:utf-8 -*-
# author:"Xianglei Kong"

class People:
    school = "CUIT"
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

class Teacher(People):
    def __init__(self,name,gender,age,level,salary):
        super().__init__(name,gender,age)
        self.level = level
        self.salary = salary

class Student(People):
    def __init__(self,name,gender,age,class_time):
        super().__init__(name,gender,age)
        self.class_time = class_time

class Course:
    def __init__(self,course_name,course_price,course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
    def tell_info(self):
        print ('课程：%s 价格：%s 周期%s ' % (self.course_name, self.course_price, self.course_period))

class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def tell_date(self):
        print('生日:%s-%s-%s' % (self.year, self.month, self.day))

teal = Teacher('alex', '男', 22, 'SSS', 99999)
stu1 = Student('张三', '男', 32, '8:45')

python = Course('python', 9999, '4mons')
linux = Course('linux', 9999, '4mons')
go = Course('go', 9999, '4mons')


teal.course = python        # 组合
stu1.course = python        # # doc1.属性  = python对象
teal.date = Date(1994,11,14)

print (python)              #python 对象
print (teal.course)         #teal的属性
print (stu1.course)

print(python.course_name)   #打印python对象的course_name属性
print(teal.course.course_name)      #打印teal.course属性的course_name的属性

teal.course.tell_info()             # #可以使用组合的类产生的对象所持有的方法
teal.date.tell_date()


teal.courses = []
teal.courses.append(python)
teal.courses.append(linux)
teal.courses.append(go)

for item in teal.courses:          # 多个对象添加到第一个对象的属性  [ ]
    item.tell_info()