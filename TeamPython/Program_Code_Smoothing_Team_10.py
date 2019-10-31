'''
===============================================================================
ENGR 133 Program Description 
	Program runs operations on input images and outputs them following user
    instructions.

Assignment Information
	Assignment:     Team Python Project
	Author:         Anurag Numboori, anumboor@purdue.edu
	Team ID:        003-10
	
Contributor:    Lily Hough, lhough@purdue.edu
                Josie Carlson, carls131@purdue.edu
                Charan Jagadeeswara Krishna, cjagadee@purdue.edu
                
	My contributor(s) helped me:	
	[X] understand the assignment expectations without
		telling me how they will approach it.
	[X] understand different ways to think about a solution
		without helping me plan my solution.
	[X] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
#imports numpy for arrays and pillow for image reading and writing
import numpy as np
from PIL import Image

#numpy outputs an error when adding rbg values goes over 255 but still continues with code, this line removes the error for readability
np.seterr(over='ignore')

#function creates output file from input with smoothing applied
def GaussianBlur(input_file,output_file):
    
    #opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)
    
    #checks the dimensions of created array
    height, width, rbg = np.shape(array)
    
    #creates new array that will be used for operations
    new_array = np.copy(array)
    
    #uses nested loop to apply kernel one pixel at a time
    for i in range(2,height-2):
        for j in range(2,width-2):
            for k in range(0,2):
                #numbers come from Gaussian Blur 5x5 Kernel. math is formatted like this such that is is easier to read
                new_array[i][j][k] =    (array[i+2][j-2][k]* 1 + 
                                         array[i+2][j-1][k] * 4 +
                                         array[i+2][j][k] * 6 +
                                         array[i+2][j+1][k] * 4 +
                                         array[i+2][j+2][k] * 1 +
                                         array[i+1][j-2][k] * 4 +
                                         array[i+1][j-1][k] * 16 +
                                         array[i+1][j][k] * 24 +
                                         array[i+1][j+1][k] * 16 +
                                         array[i+1][j+2][k] * 4 + 
                                         array[i][j-2][k] * 6 +
                                         array[i][j-1][k] * 24 +
                                         array[i][j][k] * 36 +
                                         array[i][j+1][k] * 24 +
                                         array[i][j+2][k] * 6 + 
                                         array[i-1][j-2][k] * 4 +
                                         array[i-1][j-1][k] * 16 +
                                         array[i-1][j][k] * 24 +
                                         array[i-1][j+1][k] * 16 +
                                         array[i-1][j+2][k] * 4 + 
                                         array[i-2][j-2][k] * 1 +
                                         array[i-2][j-1][k] * 4 +
                                         array[i-2][j][k] * 6 +
                                         array[i-2][j+1][k] * 4 +
                                         array[i-2][j+2][k] * 1)/(256)

    #saves files as output file
    img = Image.fromarray(new_array, 'RGB')
    img.save(output_file)
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''