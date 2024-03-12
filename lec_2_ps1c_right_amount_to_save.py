# -*- coding: utf-8 -*-
"""
Program name: ps1c - Finding the right amount to save away
Author: dsubdsub
Creation date: Mon Dec 18 19:45:27 2023
Description: write a program to calculate the best savings rate, as a function of your starting salary
Repository: MIT_6.0001_Python
Version: 1.0
License: MIT
"""

print("\nHOUSE HUNTING - FINDINF THE RIGHT AMOUNT TO SAVE AWAY"),
annual_salary = float(input("\n1. Enter your annual salary: "))

# constants
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
tolerance = 100

# variables
current_savings, steps, month = 0, 0, 0
 
# bisection process
low = 0
high = 10000
guess = int((high + low)/2)

#Block to check if it is possible to obtain the down payment 
#from the annual salary.  
aux_annual_salary = annual_salary
percent_monthly_salary = high

# Loop to calculate the total savings considering 100% of the salary  
for month in range(36):
    # loop for the raise
    if month%6 == 0 and month > 0:
        aux_annual_salary += aux_annual_salary*semi_annual_raise
    current_savings += (r/12)*current_savings + ((aux_annual_salary*(percent_monthly_salary/10000))/12)

#print (f'\nTotal saving for percent_monthly_salary = 100%: {current_savings}')

if current_savings < (total_cost*portion_down_payment - tolerance):
   print('\nIt is not possible to pay the down payment in three years.')
   print ('Come on, maaaan! You should listen to Stef and win the lottery.')
   
else: 
    while abs(current_savings - total_cost*portion_down_payment) >= tolerance:
        steps += 1
    
        # variables
        current_savings = 0
        aux_annual_salary = annual_salary
        percent_monthly_salary = guess
        
        for month in range(36):
            # loop for the raise
            if month%6 == 0 and month > 0:
                aux_annual_salary += aux_annual_salary*semi_annual_raise
        
            current_savings += (r/12)*current_savings + ((aux_annual_salary*(percent_monthly_salary/10000))/12)
    
        # bisection process
        if current_savings > total_cost*portion_down_payment:
            high = percent_monthly_salary
        else:
            low = percent_monthly_salary
    
        guess = int((high + low)/2)
        
    #print(f"Valor economizado: {current_savings}")
    print('\nBest savings rate:', percent_monthly_salary/10000)
    print('Steps in bisection search:', steps)