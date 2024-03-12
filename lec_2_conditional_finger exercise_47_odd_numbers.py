# -*- coding: utf-8 -*-
"""
Program name: Finding the largest odd number
Author: dsubdsub
Creation date: Sat Dec 30 09:21:26 2023
Description: Lecture 2 - 2.3 Branching Programs / Finger exercise / p. 47
            Write a program that examines three variables — x, y, and z — 
            and prints the largest odd number among them. If none of them 
            are odd, it should print the smallest value of the three.
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\n2.3 BRANCHING PROGRAMS - FINGER EXERCISE, PAGE 47\n")
x = float(input("Enter a number x: "))
y = float(input("Enter a number y: "))
z = float(input("Enter a number z: "))


answer = (x if x < z else z) if (x < y) else (y if y < z else z)
flag_odd = 0
if x%2 != 0:
    answer = x
    flag_odd = 1
if y%2 != 0 and y > answer:
    answer = y
    flag_odd = 1
if z%2 != 0 and z > answer:
    answer = z
    flag_odd = 1

if flag_odd == 1:
    print(f"The largest odd number between {x}, {y} and {z} is: {answer}")
else:
    print(f"There is no odd number. The smallest value between {x}, {y} and {z} is: {answer} ")

# Other exemple
# flag_odd = 0
# flag_even = 0

# #checking x
# if x%2 != 0:
#     largest_odd = x
#     flag_odd = 1
# else:
#     smaller_value = x
#     flag_even = 1

# #checking y
# if y%2 != 0:
#     if flag_odd == 1:
#         if y > largest_odd:
#             largest_odd = y
#     else:
#         largest_odd = y
#         flag_odd = 1
# elif flag_even == 1:
#     if y < smaller_value:
#         smaller_value = y
# else:
#     smaller_value = y
#     flag_even = 1

# #checking z
# if z%2 != 0:
#     if flag_odd != 0:
#         if z > largest_odd:
#             largest_odd = z
#     else:
#         largest_odd = z
#         flag_odd = 1
        
# elif flag_even == 1:    
#     if z < smaller_value:
#         smaller_value = z
# else:
#     smaller_value = z
#     flag_even = 1

# if flag_odd != 0:
#     print(f"The largest odd number between {x}, {y} and {z} is: {largest_odd}")
# else:
#     print(f"There is no odd number. The smallest value between {x}, {y} and {z} is: {smaller_value} ")
    