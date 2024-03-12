# -*- coding: utf-8 -*-
"""
Program name: ps0 - Raising a number to a power and taking a logarithm
Author: dsubdsub
Creation date: Wed Dec 13 12:52:17 2023
Description: Write a program that does the following in order:
        1. Asks the user to enter a number “x”
        2. Asks the user to enter a number “y” 
        3. Prints out number “x”, raised to the power “y”.
        4. Prints out the log (base 2) of “x”. 
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

import numpy

restart=0
while restart==0:
    print("\nps0 - Raising a number to a power and taking a logarithm\n")
    while True:
        try:
            x = float(input("Enter a number x: "))
            break
        except ValueError:
            print("Try again and enter a valid number, please.\n")
    
    while True:
        try:
            y = float(input("Enter a number y: "))
            break
        except ValueError:
            print("Try again and enter a valid number, please.\n")
    
    print(f"\nThe number {x} raised to the power {y} = {numpy.power(x,y)}")
    
    if x>0:
        print(f"The log (base 2) of {x} = {numpy.log2(x)}\n")
    else:
        print("It is not possible to obtain the log of '0' or a negative number.\n")
    
    while True:
        try:
            restart=int(input("0 - Restart\n1 - Quit\n"))
            if restart==0 or restart==1:
                break
            else:
                print("Use only '0' or '1' to choose.\n")
        except ValueError:
            print("Use only '0' or '1' to choose.\n")
