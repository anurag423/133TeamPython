#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py4_ACT Task 4
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
future_list = []
present_list = []
past_list = []

def Sort_Dates():
    with open('Py4_ACT_Task4_input.txt', 'r') as input_file:
            input_list = input_file.readlines()  
            for i in range(0,len(input_list)):
                current_date = input_list[i]
                current_date_splitup = current_date.split(" ")
                if int(current_date_splitup[1]) > 2019:
                    future_list.append(current_date)
                elif int(current_date_splitup[1]) < 2019:
                    past_list.append(current_date)
                else:
                    if str(current_date_splitup[0]) == 'November' or str(current_date_splitup[0]) == 'December':
                        future_list.append(current_date)
                    elif str(current_date_splitup[0]) == 'October':
                        present_list.append(current_date)
                    else:
                        past_list.append(current_date)

Sort_Dates()

for i in range(0,len(future_list)):
    future_list[i] = future_list[i].strip("\n")
for i in range(0,len(present_list)):
    present_list[i] = present_list[i].strip("\n")
for i in range(0,len(past_list)):
    past_list[i] = past_list[i].strip("\n")
    
with open('Py4_ACT_Task4_output.txt', 'a') as output_file:
    output_file.write(f'Future dates: {len(future_list)}\n')
    for i in range(0,len(future_list)):
        output_file.write(f'{future_list[i]}\n')
    output_file.write(f'\n')
    
    output_file.write(f'Present dates: {len(present_list)}\n')
    for i in range(0,len(present_list)):
        output_file.write(f'{present_list[i]}\n')
    output_file.write(f'\n')
    
    output_file.write(f'Past dates: {len(past_list)}\n')
    for i in range(0,len(past_list)):
        output_file.write(f'{past_list[i]}\n')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''