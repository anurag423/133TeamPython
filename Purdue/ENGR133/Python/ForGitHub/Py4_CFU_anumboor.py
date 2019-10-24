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
user_input = float(input('Input the target value: '))
starting_point = 1
old_input = 1
next_input = 1
total = 1
summation_values = []

with open('myoutput.txt', 'w') as test_file:
    test_file.write(f'For a target value of {user_input}\nThe summation values at each iteration are:\n')

while user_input>total:
    next_input =old_input/starting_point

    summation_values.append(next_input)
    total = sum(summation_values)
    with open('myoutput.txt', 'a') as test_file:
        test_file.write(f'{str(total)}\n')
    starting_point = starting_point + 1
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''