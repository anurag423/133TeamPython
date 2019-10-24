#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Generate two random numbers, convert both to decimals and fractions and
    show how both equal the same number.

Assignment Information
	Assignment:     Py1_PA Task 1
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
import random
import fractions

random.seed(int(input("Enter the seed: ")))
x = random.uniform(0,10)
y = random.uniform(0,10)

x = round(x,4)
y = round(y,4)
print(f'First Random Number: {x}')
print(f'First Second Number: {y}')


x = round(x, 1)
y = round(y, 1)

c = x + y
c = round(c,1)

print(f'Sum of decimals: {x} + {y} = {c}')

x = fractions.Fraction(x).limit_denominator(10)
y = fractions.Fraction(y).limit_denominator(10)

d = x + y

print(f'Sum of fractions : {x} + {y} = {d}')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''