'''
===============================================================================
ENGR 133 Program Description 
	Program runs operations on input images and outputs them following user
    instructions.

Assignment Information
	Assignment:     Team Python Project
	Author:         Josie Carlson, carls131@purdue.edu
	Team ID:        003-10
	
Contributor:    Lily Hough, lhough@purdue.edu
                Anurag Numboori, anumboor@purdue.edu
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

#function creates output file from input with rotation applied
def Rotation(input_file,output_file):
    
    #opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)
    
    #checks the dimensions of created array
    height, width, rbg = np.shape(array)
    
    #creates new array that will be used for operations
    new_array = np.copy(array)
    
    #changes new array's dimensions so it can be used for rotations
    new_array = np.reshape(new_array, (width,height,3))
    
    #nested loop changes value of the new array along a diagonal line
    for i in range(0,height):
        for j in range(0,width):
            new_array[-j-1][-i-1] = array[i][j]
            
    #creates copy of new_array for mirroring
    finalarray = np.copy(new_array)
    
    #the loop mirrors values from new_array to final_array, creating 90 degree rotation
    for i in range(0,width):
        finalarray[i] = (new_array[abs(i-(width-1))])
 
    #saves files as output file
    img = Image.fromarray(finalarray, 'RGB')
    img.save(output_file)

    #returned output_file is used in master when rotating 180 or 270 degrees
    return output_file
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''