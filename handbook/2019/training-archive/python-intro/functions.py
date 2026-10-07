#!/usr/bin/env python

def my_function():
    print("Hello from a function")

def my_greet_function(name):
    print("Hello " + name + ", I am function")

def my_pi(num):
    num = num * 3.14    
    print(num)

def my_multiply(num1,num2):
    result = num1 * num2
    return result

my_function()
my_greet_function('Chuck')

for iteration in range(82, 101):
    my_pi(iteration)

print(my_multiply(566765,8503432))
