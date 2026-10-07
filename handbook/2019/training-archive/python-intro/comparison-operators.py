#!/usr/bin/env python

dictionary = 'yes'
list = 'yes'
threshold = 30

if dictionary == 'yes':
    print('Starting Dictionary Test')
    data = {'result-1':42,'result-2':100,'result-3':20}
    for result in data:
        if data[result] <= threshold:
            print(result, data[result])

if list == 'yes':
    print('Starting List Test')
    data = [2,4,3,6,9,100,42,20,35,68,39]
    for result in data:
        if result >= threshold:
            print(result)

print('Script Complete')
