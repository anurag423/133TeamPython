#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py3_ACT Task 4B
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
max_value = int(input('Target value= '))
if max_value == 3:
    x = [3,0]
    y = len(x)
    print(x)
    print(f'The series contains {y-1} term before the target of {max_value} is exceeded.')
elif max_value > 3:
    x = [3,0,2]
    while max_value >= x[-1]:
        term_added=(x[-2]+x[-3])
        if term_added <= max_value:
            x.append(term_added)
        else:
            x.append(term_added)
            break
    y = len(x)
    print(x)
    print(f'The series contains {y-1} terms before the target of {max_value} is exceeded.')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''