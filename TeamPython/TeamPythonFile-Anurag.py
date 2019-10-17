# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:47:26 2019

@author: anumb
"""

#asks the user for input and output files files 
input_file = input('Enter the input file with .jpg attached: ')
output_file = input('Enter the output file with .jpg attached: ')
#checks if user inputs .jpg in file. if jpg isn't included sets viable to no and doesn't continue
if not '.jpg' in input_file or not '.jpg' in output_file:
        print('Please make sure there is a .jpg at the end of your input and output files.')
        viable = 'no'
#if user inputs fine inputs, sets viable to yes and continues with program
else:
    viable = 'yes'

    
#checks if program should continue or stop
if viable == 'no':
        print('You have entered an incorrect input. Please restart the program.')

#    
elif viable == 'yes':
    #asks the user for input process
    user_answer = input("Do you want to Rotate, Mirror, Greyscale or Filter?: ").lower()
    
    #goes down path for user's inputs for rotates and mirror
    if user_answer == 'rotate':
        user_answer = input('Do you want to rotate by 90/180/270 or Mirror?: ').lower()
        if user_answer== '90':
    #        read input file, run function for rotate 90 once, output
            pass
        if user_answer== '180':
    #        read input file, run function for rotate 90 twice, output
            pass
        if user_answer== '270':
    #    read input file, run function for rotate 90 thrice, output
            pass
        elif user_answer =='mirror':
    #        read, run function for mirror, output file
            pass
    #goes down path for user's input for greyscale
    elif user_answer == 'greyscale':
    #    read, run function for rgb changes, output file
        pass
    #goes down path for user's input for filtering
    elif user_answer == 'filter':
        user_answer = input(' Your options are lorem1,lorem2,lorem3, and lorem4: ').lower()
        if user_answer == 'lorem1':
    #       read, run function for filtering, output file
            pass
#    if userinput is incorret, exits program and prints error message
    else:
        print('You have entered an incorrect input. Please restart the program.')
        
