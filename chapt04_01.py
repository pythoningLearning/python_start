#coding=utf-8
'''
    python对象拥有三个特性：身份，类型和值。
    身份：每一个对象都有一个唯一的身份标识自己，任何对象的身份可以使用内建函数id()来得到。
    这个值可以被认为是该对象的内存地址。
    类型:对象的类型决定了该对象可以保持什么类型的值，可以进行什么样的操作，以及遵循什么样的规则。可以用内建函数type()查看python对象的类型。因为在python中类型也是对象，所以type()返回的是对象而不是简单的字符串
    值：对象表示的数据项
    python用句点(.)标记法来访问属性

    标准类型

    。数字(分为几个子类型，其中有三个整数)
    。Integer 整数
    。Boolean 布尔型
    。Long integer 长整形
    。Floating point real number 浮点型
    。Complex number 复数型
    。String 字符串
    。List 列表
    。Tuple 元组
    。Dictionary 字典
'''
print type(42) #<type 'int'>
print type(type(42)) #<type 'type'>

'''
Python 有一个特殊的类型，被称为Null对象或者NoneType,它只有一个值，那就是None.它不支持任何运算也没用任何内建方法。
所有标准对象均可用于布尔测试，同类型的对象之间可以比较大小。每个对象天生具有布尔True或False值。
下列对象的布尔值是False:
。None;
。False(布尔类型);
。所有的值为0的数；
。0(整行);
。0.0(浮点类型)
。0L(长整类型)
。0.0+0.0j(复数)
。""(空字符串)
。[](空列表)
。()(空元组)
。{}(空字典)
值不是上面列出来的任何值的对象的布尔值都是True
'''

#sequence[起始索引：结束索引：步进值]
foostr= "abcde"
print foostr[::-1] #edcba
print foostr[1:5:2] #bd
print foostr[::-2] #eca
foolist=[123,"xba",342.34,"abc"]
print foolist[::-1] #['abc', 342.34, 'xba', 123]


#xrange()是内建函数range()的兄弟版本，用于需要节省内存使用或range()无法完成的超大数据集场合

'''
。对象值的比较
    比较操作符用来判断同类型对象是否相等，所有的内建类型均支持比较运算，比较运算返回布尔值True或False.
'''
print 2==2 #True
print [3,"abc"] == ["abc",3] #False
print [3,"abc"] == [3,"abc"] #True

'''
。对象身份比较
每个对象都天生具有一个计数器，记录它自己的引用次数。这个数目表示有多少个变量指向该对象。python提供了is和is not 操作符来测试两个变量是否指向同一个对象。a is b 等价于 id(a) == id(b)
'''
a=[5,'hat',-9.3]
b=a
print id(a) #4455497672
print id(b) #4455497672
print a is b #True

'''
    cmp(obj1,obj2) 比较obj1和obj2，根据比较结果返回整数i：
    i<0 if obj1<obj2
    i>0 if obj1>obj2
    i==0 if obj1 == obj2

    repr(obj)或'obj' 返回一个对象的字符串表示
    str(obj)返回对象适合可读性好的字符串表示
    type(obj)得到一个对象的类型，并返回相应的type对象
'''

a,b=-4,12
print cmp(a,b) #-1
print cmp(b, a)# 1
b=-4
print cmp(a, b)#0
a,b="acb","xyz"
print cmp(a, b)

print str(4.53-2j) #(4.53-2j)
print str(2e10) #20000000000.0
print repr([0,4,9,9]) #[0, 4, 9, 9]
print repr((3,4,5)) #(3, 4, 5)
print repr({"object":123}) #{'object': 123}


'''
python 不支持方法或者函数重载
'''
print type('') #<type 'str'>
print type(100) #<type 'int'>
print type(0.0) #<type 'float'>
print type([]) #<type 'list'>
print type(()) #<type 'tuple'>
print type({}) #<type 'dict'>
print type(type("")) #<type 'type'>

class Foo : pass

print type(Foo) #<type 'classobj'>

class Bar(object):pass

print type(Bar) #<type 'type'>

foo = Foo()

print type(foo) #<type 'instance'>

bar = Bar()

print type(bar) #<class '__main__.Bar'>

'''
isinstance() 判断是否是实例
'''


