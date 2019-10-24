# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:51:44 2019

@author: anumb
"""

#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	

Assignment Information
	Assignment:     Py2_ACT Task 2
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
x = int(input('Enter temperature: '))
y = int(input('Enter pressure: '))

if x > 1000 or y > 20:
    print('Danger')
    if x > 1000:
        print('High Temperature')
    else:
        print('High Pressure')
elif (750 < x < 1000) and (10 < y < 20):
    print('Normal')
else:
    print('Warning')
    if x < 750:
        print('Low Temperature')
    else:
        print('Low Pressure')
  
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''