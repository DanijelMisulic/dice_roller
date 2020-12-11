#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:40:27 2020

@author: danijelmisulic
"""

from dice import *
from helper_functions import random_dice_number, random_binary_string

#generate random dice integer number
#number = random_dice_number()

#or go with random binary dice string and convert it to integer
number = int(random_binary_string(), 2)

if number == 1:
  dice1()
elif number == 2:
  dice2()
elif number == 3:
  dice3()
elif number == 4:
  dice4()
elif number == 5:
  dice5()
elif number == 6:
  dice6()
