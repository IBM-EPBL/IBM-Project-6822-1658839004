#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:10:03 2022

@author: nandhini
"""

#Program for String concatenation
str1 = input("Enter the first string: ")
str2 = input("Enter the second strng: ")
new_str = str1 + str2

print("Concatenated string is :",new_str) #Prints the result of concatenation

#Code for String Slicing
length = len(new_str)

slicey = input("Enter the number of charaacters to be sliced :")
if(length<slicey):
    print("Length is exceeded")
else:
    new_str = new_str[0:slicey]
    print("Sliced string is :",new_str) #Result for slicing
    
#Code for Strig reverse
new_str = new_str.reverse()
print("Reversed string is : ",new_str) #Result for String reverse
