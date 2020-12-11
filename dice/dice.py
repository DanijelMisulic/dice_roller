#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:40:35 2020

@author: danijelmisulic
"""
from turtle import Turtle

joe = Turtle()

def create_dice():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  
def put_a_dot():
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()

def dice1():
  create_dice()
  joe.goto(50, 50)
  put_a_dot()
  joe.hideturtle()
  
def dice2():
  create_dice()
  joe.goto(30, 50)
  put_a_dot()
  joe.goto(68, 50)
  put_a_dot()
  joe.hideturtle()
  
def dice3():
  create_dice()
  joe.goto(30, 30)
  put_a_dot()
  joe.goto(50, 50)
  put_a_dot()
  joe.goto(70, 70)
  put_a_dot()
  joe.hideturtle()
  
def dice4():
  create_dice()
  joe.goto(26, 70)
  put_a_dot()
  joe.goto(69, 70)
  put_a_dot()
  joe.goto(26, 20)
  put_a_dot()
  joe.goto(69, 20)
  put_a_dot()
  joe.hideturtle()
  
def dice5():
  create_dice()
  joe.goto(50, 50)
  put_a_dot()
  joe.goto(20, 75)
  put_a_dot()
  joe.goto(78, 75)
  put_a_dot()
  joe.goto(20, 20)
  put_a_dot()
  joe.goto(78, 20)
  put_a_dot()
  joe.hideturtle()
  
def dice6():
  create_dice()
  joe.goto(20, 74)
  put_a_dot()
  joe.goto(50, 74)
  put_a_dot()
  joe.goto(80, 74)
  put_a_dot()
  joe.goto(50, 20)
  put_a_dot()
  joe.goto(20, 20)
  put_a_dot()
  joe.goto(80, 20)
  put_a_dot()
  joe.hideturtle()
 

