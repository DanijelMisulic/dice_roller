#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:28:26 2020

@author: danijelmisulic
"""
import unittest
from helper_functions import random_dice_number
from helper_functions import random_binary_string

class TestRandomDiceNumber(unittest.TestCase):
    
    #test if output is one of the desired integers
    def test_output(self):
        self.assertIn(random_dice_number(), [1, 2, 3, 4, 5, 6])
        

class TestRandomBinaryNumber(unittest.TestCase):
    
    #test if output is one of the desired binary strings
    def test_output(self):
        self.assertIn(random_binary_string(), ["001", "010", "011", "100", "101", "110"])