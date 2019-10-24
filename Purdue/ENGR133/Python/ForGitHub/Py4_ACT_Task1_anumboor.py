#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py4_ACT Task 1
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
a = input('Enter your last name: \n')
b = input('Enter your first name: \n')
c = int(input('Enter your age in whole years: \n'))
d = int(input('Enter the days elapsed since your last birthday: \n'))
     
remainder=d/365.242199
year_total= remainder + c
minute_total = year_total * 365.242199 * 24 * 60

with open('Py4_ACT_Task1_output.txt', 'w') as test_file:
    test_file.write(f'{b} {a}\nYou are {round(year_total,9)} years old.\nYou are {int(minute_total)} minutes old.')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''