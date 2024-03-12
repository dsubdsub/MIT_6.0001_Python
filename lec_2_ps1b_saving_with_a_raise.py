# -*- coding: utf-8 -*-
"""
Program name: ps1b - Saving, with a raise
Author: dsubdsub
Creation date: Fri Dec 15 10:48:48 2023
Description: Write a program to calculate how many months it will take you save up enough money for a down
payment, with a raise on the annual salary
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\nHOUSE HUNTING - SAVING WITH A RAISE")
annual_salary = float(input("\n1. Enter your annual salary: "))
portion_saved = float(input("2. Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("3. Enter the cost of your dream home: "))
semi_annual_raise = float(input("4. Enter the semi­annual raise, as a decimal: "))

# constants
portion_down_payment = 0.25
r = 0.04

# variables
current_savings, month = 0, 0

while current_savings < total_cost*portion_down_payment:
    current_savings += (current_savings*r/12) + ((portion_saved*annual_salary)/12)
    month += 1
    #Loop for the raise
    if month%6 == 0 and month > 0:
        annual_salary += annual_salary*semi_annual_raise

print(f"\nNumber of months: {month}")