# one comment
print 'Hello world!'


def foo():
    "this is a doc string"
    return True


print -2 * 4 + 3 ** 2

counter = 0
miles = 1000.0
name = "Bob"
counter = counter + 1
kilometers = 1.609 * miles

print "%f miles is te same as %f km" % (miles, kilometers)

pystr = "python"
iscool = "is cool !"
print "pystr[0]:", pystr[0]  # pystr[0]: p
print "pystr[2:5]", pystr[2:5]  # pystr[2:5] tho
print "iscool[:2]", iscool[:2]  # iscool[:2] is
print "iscool[3:]", iscool[3:]  # iscool[3:] cool
print "iscool[-1]", iscool[-1]  # iscool[-1] !

print pystr + iscool  # pythonis cool !
print pystr + " " + iscool  # python is cool !
print pystr * 2  # pythonpython
# -+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
print "-+-" * 20

pystr = '''python
    is cool'''
print pystr

aList = [1, 2, 3, 4]
print aList
print aList[0]
print aList[2:]
print aList[:3]
aList[1] = 5
print aList

aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[:3]
# aTuple[1] = 5

aDict = {'host': 'earth'}
aDict['port'] = 80
print aDict  # {'host': 'earth', 'port': 80}
print aDict.keys()  # ['host', 'port']
print aDict.values()  # ['earth', 80]
print aDict.items()  # [('host', 'earth'), ('port', 80)]
for key in aDict:
    print key, aDict[key]

counter = 0
while counter < 3:
    print 'loop #%d' % (counter)
    counter += 1
aInternetList = ["e-mail", "net-surfing", "homework", "chat"]
print "I like to use the internet for:"
for x in xrange(1, len(aInternetList)):
    print aInternetList[x]

print "---" * 20
for x in aInternetList:
    print x

for eachNum in range(1, 10):
    print eachNum

foo = "abc"
for c in foo:
    print c

for i, ch in enumerate(foo):
    print ch, "(%d)" % i

squared = [x ** 2 for x in range(4)]
for x in squared:
    print x

try:
    fobj = open("test_01.py", "r")
    for eachLine in fobj:
        print eachLine
    fobj.close()
except IOError, e:
    # file open error: [Errno 2] No such file or directory: 'test_013.py'
    print 'file open error:', e


def addMe2Me(x):
    "apply + operation to argument"
    return (x + x)

print addMe2Me(20)  # 40
print addMe2Me("python")  # pythonpython
print addMe2Me([-1, "abc", ])  # [-1, 'abc', -1, 'abc']
print addMe2Me.func_doc  # apply + operation to argument
print addMe2Me.func_name  # addMe2Me
print addMe2Me.__doc__  # apply + operation to argument
print addMe2Me.__class__  # <type 'function'>
# <method-wrapper '__getattribute__' of function object at 0x105ca8b90>
print addMe2Me.__getattribute__


def fooTest(debug=True):
    "determine if in debug mode with default argument"
    if debug:
        print "in debug mode"
    print "done"

fooTest()
print "+++" * 20
fooTest(False)
