# coding=utf-8
def myMultiply(a, b):
    'return a and b multiply'
    if isinstance(a, (int, float, long)) and isinstance(b, (int, float, long)):
        return a * b
    else:
        print "illegal number"
        return 0

# print myMultiply(10, "2.0")


def isLeapyear(year):
    '判断给定年份是否是闰年'
    if isinstance(year, (int)) and year != 0:
        __, yearto4 = divmod(year, 4)
        __, yearto100 = divmod(year, 100)
        __, yearto400 = divmod(year, 400)
        print yearto4, yearto100
        if (yearto4 == 0 and yearto100 != 0) or (yearto400 == 0):
            print "%d年是闰年" % year
        else:
            print "%d年不是闰年" % year

    else:
        print "给定的年份不合法！！！"

# isLeapyear(1992)
# isLeapyear(2000)
# isLeapyear("year")
# isLeapyear(2013)
# isLeapyear(1900)
# isLeapyear(2010)
# isLeapyear(2400)
# isLeapyear(200300)

import random


def createRandom(n1, n2):
    mList = []
    for x in xrange(0, 100):
        temp = random.randrange(0, 2 ** 10 - 1, 1)
        print temp
        mList.append(temp)

    mList2 = []
    for x in xrange(0, n2):
        mList2.append(mList[random.randrange(0, len(mList) - 1)])

    mList2.sort()
    return mList2

print createRandom(100, 10)
