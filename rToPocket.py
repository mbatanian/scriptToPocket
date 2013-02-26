#!/usr/bin/python

import sys, imp
import pocket

if len(sys.argv) != 2:
	print 'Invalid # of arguments'
	print '  ./rToPocket {runner.py}'

addFunc = imp.load_source('adder', sys.argv[1])
print addFunc

# adder = __import__(sys.argv[1], 'addItems')
# print adder