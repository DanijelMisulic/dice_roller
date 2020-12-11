#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:28:26 2020

@author: danijelmisulic
"""
import random

def random_dice_number():
    return random.randint(1, 6)

#001, 010, 011, 100, 101, 110, 111
def random_binary_string(): 
    binary_number_length = 3
    binary = "" 
    range_not_satisfied = True
  
    while range_not_satisfied:
        #generate three ones or zeros to create 3 digits long binary number
        for i in range(binary_number_length): 
            zero_or_one = str(random.randint(0, 1)) 
            binary += zero_or_one 
        #if it returns zero or 7 generate again
        if binary in ("111", "000"):
            range_not_satisfied = True
            binary = "" 
        else:  
            range_not_satisfied = False
    
    return binary


if __name__ == "__main__":
    print (random_dice_number())
    binary_str = random_binary_string() 
    print(binary_str) 