#!/usr/bin/env python


import json

data = {'r1':42,'r2':100,'r3':20}
data2 = {}

with open('data.txt', 'w') as file:
     file.write(json.dumps(data))

with open('data.txt', 'r') as file:
    data2= json.loads(file.read())

print(data2)
