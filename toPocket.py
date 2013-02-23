#!/usr/bin/python

import sys
import auth, pocket

if len(sys.argv) != 2:
	print 'Invalid # of arguments'
	print '  ./toPocket {url}'

url = sys.argv[1]
pocket.add(url)

