#!/usr/bin/env python

#SBATCH --ntasks=6
#SBATCH --time=02:00:00
#SBATCH --mem=100g
#SBATCH --output=output-simple-%j.out
#SBATCH -p short,batch,intel

import os
import random
import json


if not os.path.isfile('data-big.txt'):
    data = {}
    for i in range(99999999):
        data['r'+ str(i)] = random.randint(1,99999)
    with open('data-big.txt', 'w') as file:
        file.write(json.dumps(data))

with open('data-big.txt', 'r') as file:
    data = json.loads(file.read())

l = []
for result in data:
    l.append(data[result])
average = sum(l) / len(l)
print('The sum is ', round(sum(l), 2))
print('The average is ', round(average, 2))
