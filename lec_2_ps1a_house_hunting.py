# -*- coding: utf-8 -*-
"""
Program name: ps1a - House Hunting
Author: dsubdsub
Creation date: Fri Dec 15 07:55:30 2023
Description: Write a program to calculate how many months it will take 
you to save up enough money for a down payment
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\nHOUSE HUNTING")
annual_salary = float(input("\n1. Enter your annual salary: "))
portion_saved = float(input("2. Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("3. Enter the cost of your dream home: "))

# constants
portion_down_payment = 0.25
r = 0.04

# variables
current_savings, month = 0, 0

while current_savings < total_cost*portion_down_payment:
    current_savings += (current_savings*r/12) + (portion_saved*annual_salary)/12
    month += 1

print(f"\nNumber of months: {month}")