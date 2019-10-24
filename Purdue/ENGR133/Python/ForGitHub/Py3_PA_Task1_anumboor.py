#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py3_PA Task 1
	Author:         Anurag Numboori, anumboor@purdue.edu
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
import numpy

import Py3_PA_Task1_functions_anumboor as task1

coefficients = input('Enter coefficients: ')
coefficients = coefficients.split(" ")
goal_value = float(input('Enter goal value: '))
x_value = float(input('Enter intial guess: '))
tolerance = float(input('Enter tolerance: '))
max_iterations = int(input('Enter maximum allowable iterations: '))

#takes input from user, lowers constant to find f(x) from g(x), changes all values to array
for i in range(0,len(coefficients)):
    coefficients[i] = float(coefficients[i])
task1.trim_leading_zeros(coefficients)
coefficients[-1] = (coefficients[-1] - goal_value)
coefficients = numpy.array(coefficients)
#sets up vaue lists for formatting later
derivative_list = []
f_x_list = []
x_list = []
x_list.append(x_value)
#saves first x value, establishes lists for formatting later
derivative_list_formatted = []
f_x_list_formatted = []
x_list_formatted = [] 

#calculate derivative, f_x and x for lists to be indexed later
for i in range(0, max_iterations+1):
    derivative,f_x=task1.FindDerivativeandYValue(coefficients,goal_value,x_value)
    derivative_list.append(derivative)
    f_x_list.append(f_x)
    if abs(f_x) < tolerance:
        break
    if derivative == 0:
        print('Error 2. Derivative = 0')
        break
    x_value = task1.FindNewXValue(x_value,f_x,derivative)
    x_list.append(x_value)
    if i == max_iterations+1:
        print('Error 1: too many iterations')
        break   
#inputs values for formatted value list for print 
for i in range(0,len(derivative_list)):
    derivative_list_formatted.append(derivative_list[i])
    derivative_list_formatted[i] = "{:.4e}".format(derivative_list[i])
for i in range(0,len(f_x_list)):
    f_x_list_formatted.append(f_x_list[i])
    f_x_list_formatted[i] = "{:.4e}".format(f_x_list[i])
for i in range(0,len(x_list)):
    x_list_formatted.append(x_list[i])
    x_list_formatted[i] = "{:.4e}".format(x_list[i])
#prints lines for output
for i in range(0,len(x_list)):
    print(f'    {i}: x = {x_list_formatted[i]} : f(x) = {f_x_list_formatted[i]} : f\'(x) = {derivative_list_formatted[i]}')
print(f'A solution was estimated to be {x_list_formatted[-1]}')
print(f'Total number of iterations: {i+1}')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''