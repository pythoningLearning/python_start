#coding=utf-8

"test_05.py ---create text file"

import os
ls = os.linesep

# get fileName
while True:

    if os.path.exists("text.txt"):
        print "ERROR:'%s' already exists" %fname
    else:
        break

#get file content (text) lines
all = []

print "\n Enter lines ('.' by itself to quit). \n"

#loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open("text.txt","w")
fobj.writelines(["%s%s" % (x,ls) for x in all])
fobj.close()
print "DONE!"

