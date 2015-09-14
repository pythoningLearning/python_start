#!/usr/bin/python
word = ["hello", "world", "contest"]
for x in word[:]:
    print(x)
    word.insert(0, "2")
print word
