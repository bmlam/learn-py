#! /usr/bin/python3 
""" demonstrates that if we define the __set__ and __get__ methods in a class,
    which are called descriptors,  we can set and get arbitrary attributes for 
    an instance of this class!
    it is not neccessary to explicitly inherit the class from object.
    but maybe inheritance is implicit?
"""
#class SimpleDescriptor(object):
class SimpleDescriptor:
    """
    A simple data descriptor that can set and return values
    """

    def __init__(self, name=None):
        print("__init__ of SimpleDecorator called with initval: ", name)
        self.__set__(self, name)
    def __get__(self, instance, owner):
        print(instance, owner)
        print('Getting (Retrieving) self.val: ', self.val)
        return self.val

    def __set__(self, instance, value):
        print('Setting self.val to ', value)
        self.val = value

    def __delete__(self, instance ):
        print('deleting %s ..' % instance)
    
x = SimpleDescriptor("green")
x.someVar1 = 1
x.anotherVar = 2
print(x.someVar1 )
print(x.anotherVar )
del x.someVar1     
# this line will give error: print(x.someVar1 )
if hasattr ( x, "someVar1" ) == False: print( "someVar1 is not there")
print(x.anotherVar )
    
