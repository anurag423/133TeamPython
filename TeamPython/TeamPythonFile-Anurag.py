# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:47:26 2019

@author: anumb
"""
#imports os.path module that is used for error checking if the user puts in an invalid file
import os.path

#imports functions that run for each option from user
import GreyscaleFunction as gsfunc
import SmoothingFunction as sfunc
import RotationFunction as ffunc
import MirrorFunction as mfunc

#asks the user for input and output files files 
input_file = input('Enter the input file with .png attached: ')
output_file = input('Enter the output file with .png attached: ')

#if os path determines that user inputted file doesnt exist, outputs error, sets viable to no
if not os.path.isfile(input_file):
    viable = 'no'
    print('The input file could not be found.\nPlease check spelling and if the file is in the correct directory.')
    
#if user inputs correct input files, sets viable to yes and continues with program
else:
    viable = 'yes' 
    
#checks if program should continue or stop using value of viable
if viable == 'no':
        print('Please restart the program.')
elif viable == 'yes':
    
    #asks the user for input process
    user_answer = input("Do you want to Rotate, Mirror, Greyscale or Filter?: ").lower()
    
    #goes down path for user's inputs for rotation
    if user_answer == 'rotate':
        user_answer = input('Do you want to rotate by 90/180/270?: ').lower()
        if user_answer== '90':
            ffunc.Rotation(input_file,output_file)
            print('Complete!')
        elif user_answer== '180':
            input_file = ffunc.Rotation(input_file,output_file)
            ffunc.Rotation(input_file,output_file)
            print('Complete!')
            pass
        elif user_answer== '270':
            input_file = ffunc.Rotation(input_file,output_file)
            input_file = ffunc.Rotation(input_file,output_file)
            ffunc.Rotation(input_file,output_file)
            print('Complete!')
        else:
            print('You have entered an incorrect input. Please restart the program.')
            
    #mirrors user's input vertically
    elif user_answer == 'mirror':
            mfunc.MirrorFunction(input_file,output_file)
            print('Complete!')

    #makes greyscale version of user's input
    elif user_answer == 'greyscale':
        gsfunc.Greyscale(input_file,output_file)
        print('Complete!')
    
    #makes smoothed version of user's input
    elif user_answer == 'filter':
        sfunc.GaussianBlur(input_file,output_file)
        print('Complete!')

    #if userinput for image processing is incorrect, exits program and prints error message
    else:
        print('You have entered an incorrect input. Please restart the program.')
        
