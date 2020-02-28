#! /usr/bin/python3 
""" Demonstrate use of decorator to create polynomial functions of the form
  y = a * x*x + b * x + c

  visualize the function with matplotlib
""" 

import matplotlib.pyplot as plt

def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    
def polynomial_creator_unlimited_degree ( *coefficients ):
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients[::-1]):
            res += coeff * x** index
        return res
    return polynomial
    
def visualizeFunc( xStart, xEnd, func, title ):
	xData= []; yData= [] # init the data for both axis 
	for x in range(xStart, xEnd, 1):
		xData.append(x)
		yData.append( func(x) )
	plt.plot( xData, yData )
	plt.title( title )
	plt.xlabel( 'X axix' )
	plt.ylabel( 'Y axix' )
	plt.show() # pop a modal window 

class Polynom:
	""" we try to use a class as decorator , but I am not sure how to complete this exercise
	"""
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        return a * x**2 + b * x + c
    return self.f 

print( "demo 1")
p1 = polynomial_creator(2, 3, -1) # set value for a, b, c of the polynomial 
visualizeFunc( xStart=0, xEnd= 5, func= p1, title = p1.__name__ )

print( "demo 2")
p2 = polynomial_creator_unlimited_degree(1, -2, 3, -2, 7)
visualizeFunc( xStart=0, xEnd= 9, func= p2, title="p2" )


