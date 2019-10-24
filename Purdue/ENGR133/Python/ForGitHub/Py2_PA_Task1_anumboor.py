#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py2_PA Task 1
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

import math

def theta_2_calculation(b):
    global theta_2_radians
    theta_2_radians = math.asin(b)
    theta_2_degrees = round(math.degrees(theta_2_radians),1)
    return theta_2_degrees
    print(f'There is refraction with a leaving angle of {theta_2_degrees} degrees.')
    
def d_3_calculation():
    d1_base = d_1 * math.tan(theta_1_radians)
    d2_base = d_2 * math.tan(theta_2_radians)
    d_3 = d1_base + d2_base
    d_3 = round(d_3,1)
    print(f'\nThe ending distance for the light ray is {d_3}cm.')
    
theta_1_degrees = float(input('Input incoming angle [degrees] : '))

n_1 = float(input('Input refractive index medium 1 [unitless] : '))

n_2 = 1.3
d_1 = 5.3
d_2 = 7.6 

theta_1_radians = math.radians(theta_1_degrees)
a = n_1 * math.sin(theta_1_radians)
b = a / n_2

index_refraction_difference = (n_2)/(n_1)
critical_angle_radians = math.asin(index_refraction_difference)
critical_angle_degrees = round(math.degrees(critical_angle_radians),1)

if theta_1_degrees > critical_angle_degrees:
    print('\nThere is reflection.')
    print(f'\nFor these two media, the critical angle is {critical_angle_degrees} degrees.')
elif theta_1_degrees == critical_angle_degrees:
    print('\nThere is a total internal reflection.')
    print(f'\nFor these two media, the critical angle is {critical_angle_degrees} degrees.')
else:
    theta_2_degrees = theta_2_calculation(b)
    print(f'\nThere is refraction with a leaving angle of {theta_2_degrees} degrees.')
    d_3_calculation()
    print(f'\nFor these two media, the critical angle is {critical_angle_degrees} degrees.')

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''