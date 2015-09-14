# coding=utf-8
'''
**传统除法**
如果是整形除法，传统除法会舍去小数部分，返回一个整形(地板除)。如果操作数之一是浮点数，则执行真正的除法。
print 1 / 2  # 0
print 1.0 / 2.0  # 0.5
'''


'''
# from __future__ import division
**真正的除法**
除法运算总是返回真实的商，不管操作数是整形还是浮点型。
print 1 / 2  # 0.5
print 1.0 / 2.0  # 0.5
'''

'''
**地板除**
一个新的操作符//已经被添加进来，以执行地板除法；//除法不管操作数为何种数据类型，总是舍去小树部分，返回数字序列中比真正的商小的最接近的数字
print 1 // 2  # 0
print 1.0 // 2.0  # 0.0
print -1 // 2  # -1
'''

'''
**取余数**
import math
print 2.11 - (math.floor(2.11 / 1) * 1)
x-(math.floor(x/y)*y)
'''

'''
幂运算
'''
print 3 ** 2  # 9
print -3 ** 2  # -9 ** 优先级高于左侧的 -
print (-3) ** 2  # 9
print 4.0 ** -1.0  # 0.25 **优先级低于右侧的 -

print 30 & 45  # 12
print 30 | 45  # 63

print cmp(-6, 255)
print str(0xFF)

print int(4.2)  # 4
print long(32)  # 32
print float(4)  # 4.0
print complex(4)  # (4+0j)
print complex(2.4, -8)  # (2.4-8j)
print bool(20)  # True
print bool(None)  # False
print bool(0)  # False
print bool(0.0)  # False
print bool([])  # False


class C:
    pass
c = C()
print "没有 _nonzero__():==", bool(c)  # 没有 _nonzero__():== True


class D(object):

    def __nonzero__(self):
        return False
d = D()
print "重载__nonzero__()使他返回:", bool(d)  # 重载__nonzero__()使他返回: False

print int("10", 2)  # 2
print int("16", 8)  # 14
print float("13")  # 13.0

print abs(-1)  # 1
print abs(10.)  # 10.0


# coerce()函数返回一个元组，该元组由两个数值型参数组成。此函数将两个数值型参数转换为同一类型数字，其转换规则与算术转换规则一样
print coerce(1, 2)  # (1, 2)
print coerce(1.3, 134L)  # (1.3, 134.0)
print coerce(1j, 134L)  # (1j, (134+0j))

# divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数
# divmod()内建函数把除法和取余运算结合起来，返回一个包含商和余数的元组。对整数来说，他的返回值就是地板除法和取余数操作的结果 。
# 对浮点数来说，返回的商部分是 math.floor(num1/num2)

print divmod(10, 3)  # (3, 1)
print divmod(3, 10)  # (0, 3)
print divmod(10, 2.5)  # (4.0, 0.0)

# 内建函数round()用于对浮点数进行四舍五入运算。他有一个可选的小数位数参数。如果不提供小数位参数，它返回与第一个参数最接近的整数(但仍然是浮点类型)。第二个参数告诉round函数将结果精确到小数点后指定位数。
print round(3)
print round(3.45)  # 3.0
print round(3.4999, 3)  # 3.5

# 3.14
# 3.142
# 3.1416
# 3.14159
# 3.141593
# 3.1415927
# 3.14159265
# 3.141592654
import math
for eachNum in xrange(1, 10):
    print round(math.pi, eachNum)
print round(-4.3)  # -4.0
print math.floor(1.9)  # 1.0
print math.floor(-1.1)  # -2.0

'''
函数int()直接截去小数部分(返回值为整数)
函数floor()得到最接近原数但小于原数的整形(返回值为浮点数)
函数round()得到最接近原数的整形(返回值为浮点数)
'''
print int(0.2)  # 0
print math.floor(0.2)  # 0.0
print round(0.2)  # 0.0

print int(0.7)  # 0
print math.floor(0.7)  # 0.0
print round(0.7)  # 1.0

print int(1.2)  # 1
print math.floor(1.2)  # 1.0
print round(1.2)  # 1.0

'''
abs(num) 返回num的绝对值
coerce(num1,num2) 将num1和num2转换为同一类型，然后以一个元组的形式返回
divmod(num1,num2) 除法-取余运算的结合。返回一个元组(num1/num2,num1%num2)
round(flt,ndig=1) 接受一个浮点数flt并对其四舍五入，保存ndig位小数，若不提供ndig参数，则默认小数点后0位
'''

# 进制转换函数
print hex(255)  # 0xff 转换成16进制
print oct(255)  # 0377 转换成8进制

# ASCII 转换函数
print ord('c')  # 99
print ord("0")  # 48
print chr(99)  # c

import random

print random.randint(10, 12)  # 两个整形参数，返回两则直接的随机整形
# 他接受和range()函数一样的参数，随机返回range([start,]stop[,step])结果的一项
print random.randrange(1, 10, 1)
print random.uniform(10, 12)  # 几乎和randint()一样，不过他返回的是二者直接的一个浮点型(不包括范围上限)
print random.random()  # 类似于uniform()，只不过下限恒等于0.0，上限恒等于1.0
print random.choice([10, 2, 3, 4, 5, 1, 2])  # 随机返回给的序列的一个元素
