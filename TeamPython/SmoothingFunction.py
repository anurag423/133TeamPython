#imports numpy for arrays and pillow for image reading and writing
from PIL import Image
import numpy as np
#numpy outputs an error when adding rbg values goes over 255 but still continues with code, this line removes the error for readability
np.seterr(over='ignore')

#current problem, reduce runtime!

def GaussianBlur(input_file,output_file):
    #function converts input file to array for reading
    array = Image.open(input_file)
    array = np.array(array)
    #creates new array that will be used for filtering
    new_array = np.copy(array)
    #checks the height and width for the for loops
    height, width, rbg = np.shape(array)
    #uses nested loop to apply kernel one pixel at a time
    for i in range(2,height-2):
        for j in range(2,width-2):
            for k in range(0,2):
    #           numbers come from Gaussian Blur 5x5 Kernel. math is formatted like this such that is is easier to read
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
    
    #checks where to send output file to
    blur_output_file = output_file
    #saves output file
    img = Image.fromarray(new_array, 'RGB')
    img.save(blur_output_file)
