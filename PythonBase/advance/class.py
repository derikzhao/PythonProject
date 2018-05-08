# encoding: UTF-8

class Employee:
    "员工类"
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count = 3

    def getCount(self):
        print Employee.count

    def getName(self):
        print self.name


e = Employee("com", 20)
e.getName()
e.getCount()
e.name = "casdfs"
e.getName()
print hasattr(e, "name")

delattr(e, "name")
print hasattr(e, "name")

print e.__doc__
print e.__class__
print e.__module__
print e.__dict__

print id(e)


# ----------------类的继承----------------------

class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'


c = Child()
c.childMethod()
c.setAttr(34)
c.getAttr()


# ----------------类的属性和方法----------------------

