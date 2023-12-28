# -*- coding: utf-8 -*-
"""
Program name: Square root deduction
Author: dsubdsub
Creation date: Sun Dec 10 15:53:39 2023
Description: Lecture 1 - Program for deducing square root of a number
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

import numpy as np

#Loop to restart the program if the user wants to
restart=0
while restart==0:
    print("\nPROGRAM TO DEDUCE THE SQUARE ROOT OF A NUMBER")
    while True:
        try:
            x = float(input("\nEnter a positive number you want to get the square root of: "))
            if x>=0:
                print(f"You choose the number {x}. I'm glad, this is a valid input.")
                break
            else:
                print("It is not possible to get a square root of a negative number.")
        except ValueError:
            print("Try again and enter a valid number, please.\n")
    g = 1
    flag=0
    while flag==0:
        # 2 - If g*g is close enough to x, stop and say g is the answer 
        if g*g >= x-0.0001 and g*g <= x + 0.0001:
            flag=1
            square_root = g
            print(f"\nThe rough square root of {x} is {square_root:.5f}.\n")
            while True:
                try:
                    restart=int(input("0 - Restart\n1 - Quit\n"))
                    if restart==0 or restart==1:
                        break
                    else:
                        print("Use only '0' or '1' to choose.\n")
                except ValueError:
                    print("Use only '0' or '1' to choose.\n")
        else:
            g = np.mean([g,(x/g)])
