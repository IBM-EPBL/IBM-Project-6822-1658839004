#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:10:03 2022

@author: nandhini
"""

# Calculator program in python

#Calculator function
def calculate(a, b, c):
    if(c == '+'):
        return a+b
    elif(c=='-'):
        return a-b
    elif(c=='*'):
        return a*b
    elif(c=='/'):
        return a//b
    else:
        return null

#Main program
first = int(input("Enter first number : "))     #Getting first number
second = int(input("Enter second number : "))   #Getting second number

operator = input("Enter the operation : ")[0]

print("Your result is " , calculate(first,second,operator))
