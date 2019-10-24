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
x = input('Enter the filename of the input file: ')
word = input('Enter the search word: ')
word = word.lower()
counter = 0 
total_words = 0
with open(x, 'r') as input_file:
    total_lines = input_file.readlines()
    for i in range(0,len(total_lines)):
        current_line = total_lines[i]
        current_line = current_line.split(" ")
        for i in range(0,len(current_line)):
            current_line[i] = current_line[i].strip("!")
            current_line[i] = current_line[i].strip(',')
            current_line[i] = current_line[i].strip(";")
            current_line[i] = current_line[i].strip("\n")
            current_line[i] = current_line[i].strip(",\n")
            current_line[i] = current_line[i].strip(";\n")
            current_line[i] = current_line[i].strip("?")
            current_line[i] = current_line[i].strip(".")
            current_line[i] = current_line[i].strip(":")
            current_line[i] = current_line[i].strip("'")
            current_line[i] = current_line[i].lower()
        for i in range(0,len(current_line)):
            current_word = current_line[i]
            if current_word == word:
                counter = counter + 1
            if current_word.isalpha() or '-' in current_word or "'" in current_word:
                total_words = total_words + 1
percent = ((counter) / (total_words)) * 100
print(f'The search word occurred {format(percent, ".2f")}% of the time.')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''