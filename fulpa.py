#!/usr/bin/python3

import os, sys 

curPath= os.getcwd()
sep = os.path.sep

for file in sys.argv[ 1: ]:
	print( "%s%s%s" % ( curPath, sep, file) )