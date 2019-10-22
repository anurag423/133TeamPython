#imports numpy for arrays and pillow for image reading and writing
import numpy as np
from PIL import Image

#!!!!current problem, debug why one pixel row/column messes up before mirroring!!!!

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
    for i in range (0,width):
        for j in range(0,height):
            new_array[-i][-j] = array[j][i]
            
    #creates copy of new_array for mirroring
    finalarray = np.copy(new_array)
    
    #the loop mirrors values from new_array to final_array, creating 90 degree rotation
    for i in range(0,width):
        finalarray[i] = (new_array[abs(i-(width-1))])
 
    #saves files as jpg
    img = Image.fromarray(finalarray, 'RGB')
    img.save(output_file)
    
    return output_file