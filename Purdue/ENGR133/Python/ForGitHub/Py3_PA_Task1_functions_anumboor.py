#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g. Py1_ACT Task 1
	Author:         Name, login@purdue.edu
	Team ID:        ###-## (e.g. 001-14 for section 1 team 14)
	
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
import math

def trim_leading_zeros(array):
    while array[0] == 0 :
        del array[0]
    print(f'The polynomial entered is of order: {len(array)-1}')
    
def FindDerivativeandYValue(coefficients,goal_value,x_value):
    #computes f(x) exponents
    exponent_list = []
    for i in reversed(range(0, len(coefficients))):
        exponent_list.append(i)    
    exponent_list = numpy.array(exponent_list)
    #calculates f(x)
    f_x_list= []
    for i in range(0,len(coefficients)):
        each_y = coefficients[i] * (math.pow(x_value, exponent_list[i]))
        f_x_list.append(each_y)
    f_x = sum(f_x_list)
    #finds f'(x) exponents and coefficients
    derivative_exponents = []
    derivative_coefficients = numpy.multiply(coefficients,exponent_list)
    for i in range(0,len(coefficients)-1):
        derivative_exponents.append(exponent_list[i] - 1)
    derivative_exponents = numpy.array(derivative_exponents)
    #finds f'(x) value
    sum_derivative_list = []
    for i in range(0,len(coefficients)-1):
        each_derivative = derivative_coefficients[i] * (math.pow(x_value, derivative_exponents[i]))
        sum_derivative_list.append(each_derivative)
    derivative = sum(sum_derivative_list)
    #returns derivative and f(x) from the calculations
    return (derivative,f_x)

def FindNewXValue(old_x,f_x,derivative):
    new_x = old_x - (f_x)/(derivative)
    old_x = new_x
    return old_x
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''