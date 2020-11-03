#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 1 23:48:57 2020

@author: pepe
"""


#%% linear search

def linear_search(element_looking_for, lst):
    
    for element in lst:
        
        if element == element_looking_for:
            
            return True
        
    return False

print(linear_search(3, [1,2,3,4,5]))

print(linear_search(7, [1,2,3,4,5]))

print(linear_search(7, [1,2,3,4,5,7]))

#%% binary search

def binary(elem, lst):

    left = 0
    right = len(lst) - 1
    
    middle = (left + right) // 2
    
    operations = 0
    
    while left <= right:
        
        operations = operations + 1
        
        middle = (left + right) // 2
        
        if lst[middle] < elem:
            
            left = middle + 1
            
        elif lst[middle] > elem:
            
            right = middle - 1
            
        else:
            print(operations)
            return True
        
    print(operations)
    return False

print(binary(3, [1,2,4]))

print(binary(10000000, range(0, 10000001)))



            





























