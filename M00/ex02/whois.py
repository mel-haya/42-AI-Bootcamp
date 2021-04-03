#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print("ERROR")
    exit()
if not sys.argv[1].isdigit():
    print("ERROR")
    exit()

i = int(sys.argv[1])

if i == 0:
    print("I'm Zero.")
elif i % 2 == 0:
    print("I'm Even.")
elif i % 2 == 1:
    print("I'm Odd.")