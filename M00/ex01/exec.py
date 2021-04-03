#!/usr/bin/python

import sys

sys.argv.pop(0)
str = ' '.join(sys.argv).swapcase()[::-1]

print (str)