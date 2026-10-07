#!/usr/bin/env python

listone = [ 'abcd', 786 , 2.23, 'dog', 70.2 ] 

listtwo = [123, 'dog'] 

print(listone)            # Prints complete list 
print(listone[0])         # Prints first element of the list 
print(listone[1:3])       # Prints elements starting from 2nd to 4th 
print(listone[2:])        # Prints elements starting from 3rd element 
print(listtwo * 2)        # Prints list two times 
print(listone + listtwo)  # Prints concatenated lists

print(len(listtwo))       # Prints # of elements in listtwo
print(listtwo)            # Print listtwo

listtwo[0] = 456          # Replaces zeroth element
listtwo.append('cat')     # Appends cat to listtwo

print(len(listtwo))       # Prints # of elements in listtwo
print(listtwo)            # Print listtwo
