#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Take input from user and calculate Parellel and Series Resistance using
    user input and a given second resistance. Format into a table

Assignment Information
	Assignment:     Py1_PA Task 2
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

First_Resistance = round(float(input("Input the first resistance value [ohm] : ")),1)
#Second_Resistance = round(math.sqrt(5.6 * math.pi),1)
Second_Resistance = 50

print('Type\t\tFirst\t\tSecond\t\tEquivalent Resistance')
a = 1/(First_Resistance) + 1/(Second_Resistance)
Parallel_Resistance = 1/a
Parallel_Resistance = round(Parallel_Resistance,1)

Series_Resistance = (First_Resistance) + (Second_Resistance)
Series_Resistance = round(Series_Resistance,1)

print(f'Parallel\t{First_Resistance} ohms\t{Second_Resistance} ohms\t{Parallel_Resistance} ohms')
print(f'Series\t\t{First_Resistance} ohms\t{Second_Resistance} ohms\t{Series_Resistance} ohms')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''