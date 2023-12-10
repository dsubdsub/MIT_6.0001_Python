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

import random
import numpy as np

#Loop to restart the program if the user wants to
restart=0
while restart==0:
    print("\nPROGRAM TO DEDUCE THE SQUARE ROOT OF A NUMBER\n")
    try:
        x = float(input("Enter a number you want to get the square root of: "))
        print(f"\nYou choose the number {x}. I'm glad, this is a valid input.")
        flag=0
    except ValueError:
        print("\nTry again and enter a valid number, please.\n")
        
    # 1 - Start with a guess, g
    x_int = int(x)
    g = random.randint(1, x_int)
    
    while flag==0:
        # 2 - If g*g is close enough to x, stop and say g is the answer 
        if g*g >= x-0.0001 and g*g <= x + 0.0001:
            flag=1
            square_root = g
            print(f"\nThe rough square root of {x} is {square_root:.5f}.\n")
            restart=int(input("\n0 - Restart\n1 - Quit\n"))
           
        # 3 - Otherwise make a new guess by averaging g and x/g
        else:
            g = np.mean([g,(x/g)])

    # 4 - Using the new guess, repeat process until close enough