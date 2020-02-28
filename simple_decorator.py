#! /usr/bin/python3 

def our_decorator(func):  # our_decorator amends/enriches the behaviour of foo 
    def some_inner_func(x): # argument must have the same name as the argument of func ?!
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return some_inner_func

def foo(x):
    print("Hi, foo has been called with '%s'" % str(x)) # str serves to convert every data type to string 

foo( "call foo directly" )
foo( 123 )

#print("We now decorate foo with f:")
#foo = our_decorator(foo)

print("****** after decoration:")
foo(x= 42)

# we do not need to change the behaviour of foo for good. Instead we can create a "new" function 
# which 
foo1 = our_decorator(foo)
foo1( "foo1")

foo("foo")

our_decorator(123) # this line yields nothing in stdout !
print( type(our_decorator(123) ) )
