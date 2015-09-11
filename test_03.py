class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1 #class (data) attribute
    def __init__(self, nm="John doe"):
        "constructor"
        self.name=nm
        print "create a class instance for ",nm

    def showName(self):
        "display instance attribute and class name"
        print "you name is ",self.name
        print "my name is",self.__class__.__name__

    def showver(self):
        "display class(static) attribute"
        print self.version

    def addMe2Me(self,x):
        "apply + operation to argument"
        return x+x

foo1 = FooClass()
# print foo1.name
# print foo1.version
# foo1.showver()
# foo1.showName()
# print foo1.addMe2Me("hellopython")
