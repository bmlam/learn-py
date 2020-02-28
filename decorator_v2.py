#! /usr/bin/python3 
"""demonstrate that a decorator is the one that contains common code.
A use pattern is that when we have already defined a bunch of methods, e.g. succ and pred
in the example below and it later turns out the all these methods could use some more logic
no matter before or after the or both, we just need to re-declare them to use a common declarator
"""
def our_decorator(func):  # our_decorator amends/enriches the behaviour of foo 
	def some_inner_func(x): # argument must have the same name as the argument of func ?!
		if x < 0 or x > 11:
			raise Exception("Argument out of range!")
		print("Before calling %s x is %s" % ( func.__name__, x) )
		x= func(x)
		print("After  calling %s x is %s" % ( func.__name__, x) )
	return some_inner_func


@our_decorator
def succ(n):
	return n + 1

@our_decorator
def pred(n):
	return n - 1

succ(10)
pred(12)
