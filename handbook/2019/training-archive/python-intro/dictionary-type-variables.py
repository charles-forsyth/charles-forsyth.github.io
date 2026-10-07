#!/usr/bin/env python

dictionary = {'name':'John','code':6734,'dept':'sales',2:'a number'}
dictionary = {
    'name':'John',
    'code':6734,
    'dept':'sales',
    2:'a number'
}

print(dictionary['name'])             # Prints value for 'name' key 
print(dictionary[2])                  # Prints value for 2 key 
print(dictionary)                     # Prints complete dictionary 
print(dictionary.keys())              # Prints all the keys 
print(dictionary.values())            # Prints all the values

dictionary['name'] = 'Paul'           # Changes the value of name to Paul
dictionary['company'] = 'Big Company' # Adds new key-value pair
print(dictionary)                     # Prints all the values
