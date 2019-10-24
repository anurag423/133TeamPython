1#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Python 2 CFU
	Author:         Anurag Numboori, anumboor@purdue.edu
	Team ID:       003-10 (e.g. 001-14 for section 1 team 14)
	
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

x = float(input('Input X distance in ft: '))
y = float(input('Input Y distance in ft: '))

def distance_target():
    a = x**2
    b = y**2
    distance = math.sqrt(a+b)
    return(distance)

distance = distance_target()

if (0 <= distance <= 4):
    color = 'yellow'
    score = 10
elif (4 < distance <= 8):
    color = 'red'
    score = 8
elif (8 < distance <= 12):
    color = 'blue'
    score = 6
else:
    color = 'white'
    score = 0 

print(f'Ball landed in the {color} zone for {score} points.')



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''