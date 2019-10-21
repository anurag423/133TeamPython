# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:47:26 2019

@author: anumb
"""
#import os.path module that is used for error checking if the user puts in an invalid file
import os.path
#imports functions that run for each option from user
import GreyscaleFunction as gsfunc
import SmoothingFunction as sfunc

#asks the user for input and output files files 
input_file = input('Enter the input file with .png attached: ')
output_file = input('Enter the output file with .png attached: ')

if not os.path.isfile(input_file):
    viable = 'no'
    print('The input file could not be found.\nPlease check spelling and if the file is in the correct directory.')

#if user inputs fine inputs, sets viable to yes and continues with program
else:
    viable = 'yes' 

#checks if program should continue or stop
if viable == 'no':
        print('Please restart the program.')

elif viable == 'yes':
    #asks the user for input process
    user_answer = input("Do you want to Rotate, Mirror, Greyscale or Filter?: ").lower()
    
    #goes down path for user's inputs for rotates
    if user_answer == 'rotate':
        user_answer = input('Do you want to rotate by 90/180/270?: ').lower()
        if user_answer== '90':
    #        read input file, run function for rotate 90 once, output
            pass
        elif user_answer== '180':
    #        read input file, run function for rotate 90 twice, output
            pass
        elif user_answer== '270':
    #    read input file, run function for rotate 90 thrice, output
            pass
        else:
            print('You have entered an incorrect input. Please restart the program.')
            
    elif user_answer == 'mirror':
    #        read, run function for mirror, output file
            pass
        
    #goes down path for user's input for greyscale
    elif user_answer == 'greyscale':
    #    read, run function for rgb changes, output file
        gsfunc.Greyscale(input_file,output_file)
        print('Complete!')
    
    #goes down path for user's input for filtering
    elif user_answer == 'filter':
    #    read, run function for filtering with smoothing, outputs file
        sfunc.GaussianBlur(input_file,output_file)
        print('Complete!')

            
#    if userinput for image processing is incorrect, exits program and prints error message
    else:
        print('You have entered an incorrect input. Please restart the program.')
        
