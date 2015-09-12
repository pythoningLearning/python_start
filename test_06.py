try:
    fobj = open("text.txt", "r")
except IOError, e:
    print "*** file open error:", e
else:
    for eachLine in fobj:
        print eachLine,  # 注意,
finally:
    fobj.close()
