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
import Py2_ACT_Task5_Discriminant_anumboor

a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))

discriminant_calculation = discriminant(a, b, c)
print(f'Discriminant = {discriminant_calculation}')

print(f'The inputs are: {a}, {b}, {c}')

if discriminant_calculation > 0:
    print('No real roots: False')
    print('One real roots: False')
    print('Two real roots: True')
elif discriminant_calculation == 0:
    print('No real roots: False')
    print('One real roots: True')
    print('Two real roots: False')
elif discriminant_calculation < 0:
    print('No real roots: True')
    print('One real roots: False')
    print('Two real roots: False')

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''