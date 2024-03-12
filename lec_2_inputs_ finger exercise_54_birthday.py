# -*- coding: utf-8 -*-
"""
Program name: You were born in the year yyyy
Author: dsubdsub
Creation date: Tue Jan  2 13:48:06 2024
Description: Lecture 2 - 2.4.1 Inputs / Finger exercise / p. 54
            Write code that asks the user to enter their birthday in the 
            form mm/dd/yyyy, and then prints a string of the form ‘You were 
            born in the year yyyy.’
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\n2.4.1 INPUTS - FINGER EXERCISE, PAGE 54\n")
birthday = input("Enter your birthday in the form mm/dd/yyyy: ")
year = birthday[6:len(birthday)]

print(f"You were born in the year {year}.")