import inspect
def f0():
	# stack = 
	print( '0: %s ' % inspect.stack()[1][0] )
	print( '1: %s ' % inspect.stack()[1][1] )
	print( '2: %s ' % inspect.stack()[1][2] )
	print( '3: %s ' % inspect.stack()[1][3] )

def f1():
    frame = inspect.currentframe()
    print ("Function name:", inspect.getframeinfo(frame.f_back)[2] )
    print ("0:", inspect.getframeinfo(frame.f_back)[0] )
    print ("1:", inspect.getframeinfo(frame.f_back)[1] )
    print (inspect.getframeinfo(frame.f_back) )

def f2():
    f1()
    f0()

f2()
