# -*- coding: utf-8 -*-
"""
Program name: Empire State and the eggs
Author: dsubdsub
Creation date: Thu Jan  4 12:06:46 2024
Description: Lecture 2 - 3.1 Bisection Search / Finger exercise 3/3 / p. 79
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\n3.2 BISECTION SEARCH - FINGER EXERCISE 3/3, PAGE 79\n")

#Empire State has 102 stories high
high = 102
low = 0
egg_guesses = 1

high_floor_no_break = (high + low)/2 #o andar mais alto sem que o ovo tenha quebrado
while egg_guesses <= 7:
    ans = input(f'\nIs the egg {egg_guesses} broken on the floor {high_floor_no_break}?\nUse "y" for yes and "n" for not: ')
    print('low =', low, 'high =', high,'ans =', high_floor_no_break)
    egg_guesses += 1
    if ans == "n": #se a resposta for "sim"
        low = high_floor_no_break
    else: #se a resposta for "não" 
        high = high_floor_no_break
    high_floor_no_break = int((high + low)/2)

print(f"\nThe highest floor from which you could drop an egg without the egg breaking is {high_floor_no_break}.")