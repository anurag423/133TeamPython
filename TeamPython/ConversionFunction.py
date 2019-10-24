#imports numpy for arrays and pillow for image reading and writing
import numpy as np
from PIL import Image

#function creates output file from input with file conversion applied
def Conversion(input_file,output_file):
    
    #opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)

    #saves files as output file
    img = Image.fromarray(array, 'RGB')
    img.save(output_file)