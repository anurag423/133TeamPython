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
        
    #saves output file
    img = Image.fromarray(new_array, 'RGB')
    img.save(output_file)