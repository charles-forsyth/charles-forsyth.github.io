#!/usr/bin/env python

import sys

name = input('What is your name?\n')
print('Hi, %s.' % name)

if len(sys.argv) > 1:
    print(sys.argv[1])

