#coding=utf-8
import test_03

print test_03.foo1.addMe2Me("jjjjj")

fool2 = test_03.FooClass("hh")
fool2.showName()

import sys
sys.stdout.write("Hello world\n")
print sys.platform
print sys.version

#显示对象的属性，如果没有提供参数，则显示全局变量的名字
print dir(fool2) #['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'addMe2Me', 'name', 'showName', 'showver', 'version']


# class FooClass(__builtin__.object)
#  |  my very first class: FooClass
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, nm='John doe')
#  |      constructor
#  |
#  |  addMe2Me(self, x)
#  |      apply + operation to argument
#  |
#  |  showName(self)
#  |      display instance attribute and class name
#  |
#  |  showver(self)
#  |      display class(static) attribute
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  version = 0.1
help(fool2)#以一种整齐美观的形式，显示对象的文档字符串，如果没有提供任何参数，则会进入交互式帮助

print int("1000") #将一个对象转换为整数

print len("fool2") #返回对象的长度

# open("filename",mode) 以mode("r"表示读，'w'表示写)方式打开一个文件名为filename的文件

#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(1,10) #返回一个整数列表，起始值为start,结束值为stop-1,start默认值为0，setp默认值为1

#[2, 5, 8]
print range(2,10,3)

#<test_03.FooClass object at 0x107ace150>
print str(fool2)#将一个对象转换成字符串

#<class 'test_03.FooClass'>
print type(fool2)#返回对象的类型(返回值本身是一个type对象)
