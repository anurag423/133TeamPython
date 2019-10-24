#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Py4_ACT Task 2
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
#opens file. converts text file to list of strings per line
with open('Py4_ACT_Task2_input.txt', 'r') as input_file:
    grades = input_file.readlines()  
def Avg_Std(grades):
    #removes name from strings per line
    grade_list=[]
    for i in range(0,len(grades)):
        i_term = grades[i]
        i_term = i_term.split(' ')
        i_term = i_term[1]
        i_term = i_term.split('\n')
        i_term = i_term[0]
        grade_list.append(i_term)
    #changes grades from str to float for operations
    for i in range(0,len(grade_list)):
        grade_list[i] = float(grade_list[i])
    #calculates average for each float value
    average_grade = sum(grade_list)/len(grade_list)
    #calculates standard deviation
    total_sum_list = []
    for i in range(0,len(grade_list)):
        each_sum = math.pow((grade_list[i]-average_grade),2)
        total_sum_list.append(each_sum)
    standard_deviation = round(math.sqrt(sum(total_sum_list)/(len(grade_list))),2)
#   return stdev and average
    return average_grade,standard_deviation,grade_list
Average,Standard_Deviation,Grade_List, = Avg_Std(grades)
#calculates minimum and maximum
def Hi_Lo(grade_list):
    maximum_value = max(grade_list)
    minimum_value = min(grade_list)
    return(maximum_value,minimum_value)
High_Score,Low_Score = Hi_Lo(Grade_List)
with open('Py4_ACT_Task2_output.txt', 'w') as output_file:
    output_file.write(f'Exam 1:\nAverage = {format(Average, ".2f")}\nStandard Deviation = {format(Standard_Deviation, ".2f")}\nHigh Score = {format(High_Score, ".2f")}\nLow Score = {format(Low_Score, ".2f")}')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''