#! /usr/bin/python3 
""" Demonstrate that we can define a class and then instantiate the class to several 
object variables and each of the objects can be treated like a function 
"""

class Fibonacci:

	def __init__(self):
		self.cache = {}

	def __call__(self, n):
		if n not in self.cache:
			if n == 0:
				self.cache[0] = 0
			elif n == 1:
				self.cache[1] = 1
			else:
				self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
		return self.cache[n]

fib1 = Fibonacci()

for i in range(3):
	print(fib1(i), end=", ")
print() # force a newline, since end paramter defaults to newline

fib2 = Fibonacci()
print( fib2( 6 ) )