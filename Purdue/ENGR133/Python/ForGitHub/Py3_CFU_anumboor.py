#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py3 CFU
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
level = int(input('Please enter the level completed most recently:\n'))

if level < 0:
    level = level * (-1)
    
print(f'The level is: {level}')
print(f'The levels that have been completed are:')

candies = []

while level > 0:
    print(level)
    candies.append(level)
    level = level - 1
    
x= sum(candies)

print(f'The total number of crushed candies is {x}')



'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''