#imports numpy for arrays and pillow for image reading and writing
import numpy as np
from PIL import Image

#function creates output file from input with greyscale applied
def Greyscale(input_file,output_file):
    
    #opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)
    
    #checks the dimensions of created array
    height, width, rbg = np.shape(array)
    
    #creates new array that will be used for operations
    new_array = np.copy(array)
    
    #uses nested loop to convert each pixel to greyscale
    for i in range(0,height):
        for j in range(0,width):
            new_array[i][j] = 0.21 * array[i][j][0] + 0.72 * array[i][j][1] + 0.07 * array[i][j][2]
            
    #saves files as output file
    img = Image.fromarray(new_array, 'RGB')
    img.save(output_file)