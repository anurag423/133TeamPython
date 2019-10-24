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
import ConversionFunction as cfunc

#sets viable values such that the while loop will start
format_viable = 'no'
location_viable = 'no'
user_answer = 'start'

#while loops check that input file exists. Also that output file and input file are both in correct formats
while location_viable == 'no' or format_viable == 'no':
    
    #asks the user for input and output files files 
    input_file = input('Enter the input file with file type attached: ')
    output_file = input('Enter the output file with file type attached: ')
    
    #typing exit in input allows user to exit loop
    if input_file =='exit' or output_file == 'exit':
        print('\n\tSorry!')
        break
    
    #if user inputs input file that exists, sets location_viable to yes
    if os.path.isfile(input_file):
        location_viable = 'yes'
        
    #if os path determines that user inputted file doesnt exist, outputs error, sets viable to no
    elif not os.path.isfile(input_file):
        location_viable = 'no'
        print('\n\tError: The input file could not be found. Please check if the file is in the correct directory.')
       
    #checks if user put in a .png or .jpg, sets viable to yes if both outputs are correct
    if ('.jpg' in input_file or  '.png' in input_file) and ('.jpg' in output_file or  '.png' in output_file):
        format_viable = 'yes'
        
    #if user put in wrong formats, sets viable to no and outputs error
    else:
        format_viable = 'no'
        print('\n\tError: You have entered a file with the wrong attachment. Please check spelling and file type')
        
#if previously prompted user inputs are both acceptable, asks user what operation to apply
if location_viable == 'yes' and format_viable == 'yes':
    
    #while loops allows code to restart if user inputs wrong information    
    while user_answer == 'start':
        
        #asks the user for input process
        user_answer = input("Do you want to Convert, Rotate, Mirror, Greyscale or Filter?: ").lower()
        
        #goes down path for user's inputs for rotation
        if user_answer == 'rotate':
            
            user_answer = input('Do you want to rotate by 90/180/270?: ').lower()
            
            if user_answer== '90':
                print('\nPlease allow function time to run.')
                ffunc.Rotation(input_file,output_file)
                print('\nComplete!')
                
            elif user_answer== '180':
                print('\nPlease allow function time to run.')
                input_file = ffunc.Rotation(input_file,output_file)
                ffunc.Rotation(input_file,output_file)
                print('\nComplete!')
                    
            elif user_answer== '270':
                print('\nPlease allow function time to run.')
                input_file = ffunc.Rotation(input_file,output_file)
                input_file = ffunc.Rotation(input_file,output_file)
                ffunc.Rotation(input_file,output_file)
                print('\nComplete!')
                
            #typing exit in input allows user to exit loop 
            elif user_answer == 'exit':
                print('\n\tSorry!')
                break
                
            else:
                user_answer = 'start'
                print('You have entered an incorrect input.')

    
        #mirrors user's input vertically
        elif user_answer == 'mirror':
            print('\nPlease allow function time to run.')
            mfunc.MirrorFunction(input_file,output_file)
            print('\nComplete!')
        
        #makes greyscale version of user's input
        elif user_answer == 'greyscale':
            print('\nPlease allow function time to run.')
            gsfunc.Greyscale(input_file,output_file)
            print('\nComplete!')
            
        #makes smoothed version of user's input
        elif user_answer == 'filter':
            print('\nPlease allow function time to run.')
            sfunc.GaussianBlur(input_file,output_file)
            print('\nComplete!')
            
        #makes converted version of user's input            
        elif user_answer == 'convert':
            print('\nPlease allow function time to run.')
            cfunc.Conversion(input_file,output_file)
            print('\nComplete!')
            
        #typing exit in input allows user to exit loop 
        elif user_answer == 'exit':
            print('\n\tSorry!')
            break
        
        #if userinput for image processing is incorrect, allows user to retry
        else:
            user_answer = 'start'
            print('You have entered an incorrect input.')
            
