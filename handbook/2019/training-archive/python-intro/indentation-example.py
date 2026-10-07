#!/usr/bin/env python

myvar = 42
#myvar = 0

if myvar == 42:
    print('Condition was True')
    mylist = ['red','green','blue']
    for var in mylist:
        print(var)
    print('done true list')
else:
    print('Condition was False')
    mylist = [1,2,3]
    for var in mylist:
        print(var)
    print('done false list')
print(myvar)
