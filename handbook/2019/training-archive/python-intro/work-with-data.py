#!/usr/bin/env python

import os
import random
import json


if not os.path.isfile('data.txt'):
    data = {}
    for i in range(1234567):
        data['r'+ str(i)] = random.randint(1,314)
    with open('data.txt', 'w') as file:
        file.write(json.dumps(data))

with open('data.txt', 'r') as file:
    data = json.loads(file.read())

l = []
for result in data:
    l.append(data[result])
average = sum(l) / len(l)
print('The sum is ', round(sum(l), 2))
print('The average is ', round(average, 2))

