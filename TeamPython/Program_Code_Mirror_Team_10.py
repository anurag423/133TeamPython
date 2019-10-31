'''
===============================================================================
ENGR 133 Program Description 
	Program runs operations on input images and outputs them following user
    instructions.

Assignment Information
	Assignment:     Team Python Project
	Author:         Charan Jagadeeswara Krishna, cjagadee@purdue.edu
	Team ID:        003-10
	
Contributor:    Lily Hough, lhough@purdue.edu
                Josie Carlson, carls131@purdue.edu
                Anurag Numboori, anumboor@purdue.edu
                
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

#function creates output file from input with vertical mirror applied
def MirrorFunction(input_file,output_file):
    
    #opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)
    
    #checks the dimensions of created array
    height, width, rbg = np.shape(array)
    
    #creates new array that will be used for operations
    new_array = np.copy(array)
    
    #the loop mirrors values vertically
    for i in range(0,height):
        new_array[i] = (array[abs(i-(height-1))])
        
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