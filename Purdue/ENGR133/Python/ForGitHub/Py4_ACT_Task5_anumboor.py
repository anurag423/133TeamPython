#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py4_ACT Task 5
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
with open('Py4_ACT_Task5_input.txt', 'r') as input_file:
    input_list = input_file.readlines()
    name = input_list[0].strip("\n")
    Path_Length = int(input_list[1].strip("\n"))
    Molar_Extinction = int(input_list[2].strip("\n"))
#   creates list for absorbances
    Absorbance_List = []
    for i in range(3,len(input_list)):
        Absorbance_List.append(input_list[i])
#   strips values from absorbance and makes them floats
    for i in range(0,len(Absorbance_List)):
        Absorbance_List[i] = float(Absorbance_List[i].strip("\n"))
        Concentration_List = []
    for i in range(0,len(Absorbance_List)):
        Concentration = (Absorbance_List[i]) /(Path_Length * Molar_Extinction)
        Concentration_List.append(Concentration)
print(name)
for i in range(0,len(Concentration_List)):
    print(f'{format(Concentration_List[i], ".7f")}')

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''