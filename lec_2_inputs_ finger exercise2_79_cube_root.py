# -*- coding: utf-8 -*-
"""
Program name: Finding the cube root of negative and positive numbers
Author: dsubdsub
Creation date: Thu Jan  4 10:40:26 2024
Description: Lecture 2 - 3.1 Bisection Search / Finger exercise 2/3 / p. 79
            Find an approximation to the cube root of both negative 
            and positive numbers
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\n3.2 BISECTION SEARCH - FINGER EXERCISE 2/3, PAGE 79\n")
x = float(input('Enter a number (positive or negative) you want to know the cube root: '))
epsilon = 0.01 #aproximação
num_guesses = 0
low = min(-1,x)
high = max(1,x)
ans = (high + low)/2 #primeira tentativa no meio
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high,'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else: 
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)