#!/usr/bin/env python

tupleone = ( 'abcd', 786 , 2.23, 'dog', 70.2 ) 

tupletwo = (123, 'dog')

print(tupleone)              # Prints complete tuple 
print(tupleone[0])           # Prints zero'th element of the tuple 
print(tupleone[1:3])         # Prints elements starting from 2nd to 4th 
print(tupleone[2:])          # Prints elements starting from 3rd element 
print(tupletwo * 2)          # Prints tuple two times 
print(tupleone + tupletwo)   # Prints concatenated tuple

# tupleone[0] = 345          # This will FAIL, immutable 
# tupleone.append('cat')     # This will FAIL, immutable
