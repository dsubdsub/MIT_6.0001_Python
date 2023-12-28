# -*- coding: utf-8 -*-
"""
Program name: Circle area calculation
Author: dsubdsub
Creation date: Mon Dec 11 16:47:50 2023
Description: Lecture 1 - Program for calculating the area of a circle
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""
import math

#Loop to restart the program if the user wants to
restart=0
while restart==0:
    print("\nPROGRAM TO CALCULATE THE AREA OF A CIRCLE\n")
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius >= 0:
                print(f"You choose the radius {radius}. I'm glad, this is a valid input.")
                break
            else:
                print("The radius value can't be negative.\n")
        except ValueError:
            print("Try again and enter a valid radius, please.\n")
        
    # Area of circle equation 
    circle_area = math.pi*(radius**2)
    print(f"The area of a circle of radius {radius} is roughly {circle_area:.3f}.\n")
    while True:
        try:
            restart=int(input("0 - Restart\n1 - Quit\n"))
            if restart==0 or restart==1:
                break
            else:
                print("Use only '0' or '1' to choose.\n")
        except ValueError:
            print("Use only '0' or '1' to choose.\n")
