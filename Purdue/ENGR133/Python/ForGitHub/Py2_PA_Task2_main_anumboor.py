#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py2_PA Task 2
	Author:         NAnurag Numboori, anumboor@purdue.edu
	Team ID:        003-10
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import Py2_PA_Task2_functions_anumboor

T = float(input('Input Initial Temperature in Kelvin: '))
Vm = float(input('Input molar volume in L/mol: '))
a = 6.49
b = 0.0562
R = 0.0820573661
p = pressure(T,Vm)
rounded_pressure = round(p,4)
print(f'Intial conditions:\nMolar volume = {Vm} [L/mol]\nInitial temperature= {T} [K]\nParameter a = {a} [L^2*atm/ (mol^2)]\nParameter b = {b} [L/mol]\nResulting pressure = {rounded_pressure} [atm]')
if p > 1.2:
    print('Error! Pressure is too high!')
    t_change = temperature(1.2,Vm) - temperature(p,Vm)
    new_temperature = T + t_change
    p = pressure(new_temperature,Vm)
    t_change = round(t_change,2)
    p = round(p,2)
    new_temperature = round(new_temperature,2)
    print(f'Required temperature increment for in-range pressure = {t_change} [K]\nNew temperature = {new_temperature} [K]\nNew pressure = {p} [atm]')
elif p < 1.1:
    print('Error! Pressure is too low!')
    t_change = round(temperature(1.1,Vm) - temperature(p,Vm),2)
    new_temperature = T + t_change
    p = pressure(new_temperature,Vm)
    t_change = round(t_change,2)
    p = round(p,2)
    new_temperature = round(new_temperature,2)
    print(f'Required temperature increment for in-range pressure = {t_change} [K]\nNew temperature = {new_temperature} [K]\nNew pressure = {p} [atm]')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''